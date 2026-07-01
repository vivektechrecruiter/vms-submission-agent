from services.openai_service import load_prompt

prompt = load_prompt("prompts/resume_extraction.txt")

print("Prompt Length:", len(prompt))