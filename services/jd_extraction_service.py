import json

from parsers.jd_parser import (
    read_jd_text
)

from services.openai_service import (
    extract_resume_json
)


def extract_jd_json(
    jd_path,
    prompt_path
):

    jd_text = read_jd_text(
        jd_path
    )

    with open(
        prompt_path,
        "r",
        encoding="utf-8"
    ) as file:

        extraction_prompt = file.read()

    response = extract_resume_json(
    jd_text,
    extraction_prompt
)

    return json.loads(
        response
    )