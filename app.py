import streamlit as st
from pathlib import Path
from parsers.resume_reader import read_docx

from services.openai_service import (
    load_prompt,
    extract_resume_json
)
from services.jd_extraction_service import (
    extract_jd_json
)
from services.json_service import (
    load_json
)
from services.skill_match_service import (
    generate_skill_match
)

from generators.submission_generator_v3 import (
    generate_submission_sheet
)
from generators.direct_resume_generator import (
    generate_resume_docx
)
from generators.submission_package_generator import (
    generate_submission_package
)

st.set_page_config(
    page_title="VMS Submission Agent",
    layout="wide"
)

st.title(
    "VMS Submission Agent"
)

st.subheader(
    "Resume Submission Automation"
)

# Ensure required folders exist for all runs.
Path("input").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)

# Initialize Streamlit session state for persistent results.
if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = None

if "jd_data" not in st.session_state:
    st.session_state.jd_data = None

if "skill_match_data" not in st.session_state:
    st.session_state.skill_match_data = None

if "package_generated" not in st.session_state:
    st.session_state.package_generated = False

if "final_package_path" not in st.session_state:
    st.session_state.final_package_path = "output/final_submission_package.docx"

if "current_resume_name" not in st.session_state:
    st.session_state.current_resume_name = ""

if "current_jd_text" not in st.session_state:
    st.session_state.current_jd_text = ""


def reset_analysis_state():
    st.session_state.skill_match_data = None
    st.session_state.candidate_data = None
    st.session_state.jd_data = None
    st.session_state.package_generated = False
    st.session_state.analysis_complete = False


resume_file = st.file_uploader(
    "Upload Resume",
    type=["docx"]
)

jd_text = st.text_area(
    "Paste Job Description",
    height=300
)

current_resume_name = resume_file.name if resume_file else ""
current_jd_text = jd_text or ""

# Clear previous analysis when the app starts fresh or inputs change.
if not resume_file and not jd_text and st.session_state.analysis_complete:
    reset_analysis_state()

if current_resume_name != st.session_state.current_resume_name or current_jd_text != st.session_state.current_jd_text:
    reset_analysis_state()
    st.session_state.current_resume_name = current_resume_name
    st.session_state.current_jd_text = current_jd_text

analyze_button = st.button("Analyze Candidate")

if analyze_button:
    if not resume_file or not jd_text:
        st.warning("Please upload a resume and paste the job description before analysis.")
    else:
        reset_analysis_state()
        status_placeholder = st.empty()

        with st.spinner("Analyzing Candidate..."):
            status_placeholder.text("✓ Saving uploaded resume")
            if resume_file:
                with open(f"input/{resume_file.name}", "wb") as file:
                    file.write(resume_file.getbuffer())

            status_placeholder.text("✓ Reading resume")
            resume_text = read_docx(f"input/{resume_file.name}")

            status_placeholder.text("✓ Extracting candidate information")
            prompt = load_prompt("prompts/resume_extraction.txt")
            result = extract_resume_json(resume_text, prompt)
            with open("output/candidate.json", "w", encoding="utf-8") as file:
                file.write(result)

            status_placeholder.text("✓ Extracting job description")
            with open("input/jd.txt", "w", encoding="utf-8") as file:
                file.write(jd_text)

            jd_data = extract_jd_json(
                jd_path="input/jd.txt",
                prompt_path="prompts/jd_extraction_prompt.txt"
            )
            with open("output/jd.json", "w", encoding="utf-8") as file:
                import json

                json.dump(jd_data, file, indent=4)

            status_placeholder.text("✓ Matching candidate against JD")
            candidate_data = load_json("output/candidate.json")
            skill_match_data = generate_skill_match(
                candidate_data,
                jd_data,
                "prompts/skill_match_prompt.txt"
            )

            with open("output/skill_match.json", "w", encoding="utf-8") as file:
                import json

                json.dump(skill_match_data, file, indent=4)

            status_placeholder.text("✓ Calculating qualification results")
            st.session_state.candidate_data = candidate_data
            st.session_state.jd_data = jd_data
            st.session_state.skill_match_data = skill_match_data
            st.session_state.analysis_complete = True

            status_placeholder.text("✓ Preparing submission data")
            status_placeholder.text("✓ Analysis completed")

        status_placeholder.empty()

skill_match_data = st.session_state.skill_match_data if st.session_state.analysis_complete else None

if skill_match_data:
    st.subheader("Qualification Results")

    st.write(f"Qualification Status: {skill_match_data.get('qualification_status', '')}")
    st.write(f"Match Score: {skill_match_data.get('match_score', 0)}")
    st.write(f"Recommendation: {skill_match_data.get('recommendation', '')}")

    if skill_match_data.get("qualification_status") == "Strong Fit":
        st.subheader("Strong Matches")
        for item in skill_match_data.get("strong_matches", []):
            st.write(f"• {item}")

    if skill_match_data.get("qualification_status") == "Partial Fit":
        st.subheader("Skill Gaps")
        for item in skill_match_data.get("skill_gaps", []):
            st.write(f"• {item}")

    if skill_match_data.get("qualification_status") == "Partial Fit":
        st.subheader("Screening Questions")
        questions = skill_match_data.get("screening_questions", [])
        if questions:
            for question in questions:
                st.write(f"• {question}")
        else:
            st.write("No screening questions available.")

st.subheader("Submission Package")

generate_package = st.button("Generate Submission Package")

if generate_package:
    if not skill_match_data:
        st.warning("Please analyze the candidate first before generating the submission package.")
    else:
        status_placeholder = st.empty()
        with st.spinner("Generating Submission Package..."):
            candidate_data = st.session_state.candidate_data or load_json("output/candidate.json")
            recruiter_data = load_json("data/recruiter_inputs.json")
            skill_match_data = skill_match_data or load_json("output/skill_match.json")

            status_placeholder.text("✓ Generating Cover Page")
            generate_submission_sheet(
                candidate_data,
                recruiter_data,
                skill_match_data,
                "output/tcs_submission_v3.docx"
            )

            status_placeholder.text("✓ Formatting Resume")
            generate_resume_docx(
                candidate_data,
                "output/direct_resume.docx"
            )

            status_placeholder.text("✓ Merging Documents")
            generate_submission_package(
                "output/tcs_submission_v3.docx",
                "output/direct_resume.docx",
                st.session_state.final_package_path
            )

            st.session_state.package_generated = True
            status_placeholder.text("✓ Submission Package Ready")

        status_placeholder.empty()

if st.session_state.package_generated and Path(st.session_state.final_package_path).exists():
    st.success("Submission Package Generated Successfully")
    with open(st.session_state.final_package_path, "rb") as file:
        st.download_button(
            label="Download Submission Package",
            data=file,
            file_name="Final_Submission_Package.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
