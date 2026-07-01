from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
def test_connection():
    response = client.responses.create(
        model="gpt-5-mini",
        input="Reply with exactly: OpenAI Connection Successful"
    )

    return response.output_text

def load_prompt(prompt_path):
    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()
    
def extract_resume_json(resume_text, prompt):
    response = client.responses.create(
        model="gpt-5-mini",
        instructions=prompt,
        input=resume_text,
         
    )

    return response.output_text
    