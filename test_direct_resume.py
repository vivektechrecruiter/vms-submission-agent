from services.json_service import load_json

from generators.direct_resume_generator import (
    generate_resume_docx
)

candidate_data = load_json(
    "output/candidate.json"
)

generate_resume_docx(
    candidate_data,
    "output/direct_resume.docx"
)

print(
    "Direct Resume Generated Successfully"
)