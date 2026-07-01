from parsers.resume_reader import read_docx
from services.openai_service import (
    load_prompt,
    extract_resume_json
)

resume_text = read_docx(
    "input/sai_datta_yerlagadda.docx"
)

prompt = load_prompt(
    "prompts/resume_extraction.txt"
)

result = extract_resume_json(
    resume_text,
    prompt
)

with open("output/candidate.json", "w", encoding="utf-8") as file:
    file.write(result)

print("JSON saved successfully")