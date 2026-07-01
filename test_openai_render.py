import os

from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

print(f"API key exists: {bool(api_key)}")
print(f"API key length: {len(api_key) if api_key else 0}")

try:
    response = client.responses.create(
        model="gpt-5-mini",
        input="Reply with OK"
    )
    print("Response:", response.output_text)
except Exception as exc:
    print("Exception:", repr(exc))
    raise
