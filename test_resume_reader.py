from parsers.resume_reader import read_docx

resume_text = read_docx(
    "input/MITHLESH KUSH CV NOV 2025.docx"
)

print(resume_text[:3000])