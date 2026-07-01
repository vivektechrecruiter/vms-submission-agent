import json

from services.openai_service import (
    extract_resume_json
)


def generate_skill_match(
    candidate_data,
    jd_data,
    prompt_path
):

    with open(
        prompt_path,
        "r",
        encoding="utf-8"
    ) as file:

        prompt = file.read()

    input_data = {
        "candidate": candidate_data,
        "job_description": jd_data
    }

    response = extract_resume_json(
        json.dumps(
            input_data,
            indent=2
        ),
        prompt
    )


    if not response:
        raise Exception(
            "OpenAI returned empty response"
        )

    return json.loads(response)