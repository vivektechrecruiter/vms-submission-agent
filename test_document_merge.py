from services.document_merge_service import (
    merge_documents
)

merge_documents(
    cover_page_path="output/tcs_submission.docx",
    resume_path="output/direct_resume.docx",
    output_path="output/final_submission.docx"
)

print(
    "Documents Merged Successfully"
)