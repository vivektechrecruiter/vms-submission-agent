from services.json_service import load_json

from generators.submission_generator_v3 import (
    generate_submission_sheet
)

from generators.direct_resume_generator import (
    generate_resume_docx
)

from generators.submission_package_generator import (
    generate_submission_package
)

# ==========================
# Load Data
# ==========================

candidate_data = load_json(
    "output/candidate.json"
)

recruiter_data = load_json(
    "data/recruiter_inputs.json"
)

skill_match_data = load_json(
    "output/skill_match.json"
)

# ==========================
# Generate TCS Cover Page
# ==========================

generate_submission_sheet(
    candidate_data,
    recruiter_data,
    skill_match_data,
    "output/tcs_submission_v3.docx"
)

# ==========================
# Generate Formatted Resume
# ==========================

generate_resume_docx(
    candidate_data,
    "output/direct_resume.docx"
)

# ==========================
# Generate Final Package
# ==========================

generate_submission_package(
    "output/tcs_submission_v3.docx",
    "output/direct_resume.docx",
    "output/final_submission_package.docx"
)

print(
    "Final Submission Package Generated Successfully"
)