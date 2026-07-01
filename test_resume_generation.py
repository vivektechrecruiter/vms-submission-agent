
from services.document_formatter import (
    format_resume_document
)
from services.json_service import load_json
from services.resume_context_builder import (
    build_resume_context
)

from generators.resume_generator import (
    generate_resume
)

candidate_data = load_json(
    "output/candidate.json"
)

context = build_resume_context(
    candidate_data
)

generate_resume(
    template_path="templates/resume_template.docx",
    output_path="output/formatted_resume.docx",
    context=context
)

print("Resume generated successfully")