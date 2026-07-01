from services.json_service import load_json

from generators.submission_generator import (
    generate_submission_sheet
)

candidate_data = load_json(
    "output/candidate.json"
)

recruiter_data = load_json(
    "data/recruiter_inputs.json"
)
skill_match_data = load_json(
    "output/skill_match.json"
)

generate_submission_sheet(
    candidate_data,
    recruiter_data,
    skill_match_data,
    "output/tcs_submission.docx"
)

print(
    "Submission Sheet Generated Successfully"
)