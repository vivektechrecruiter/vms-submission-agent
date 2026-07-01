import json

from services.jd_extraction_service import (
    extract_jd_json
)

jd_data = extract_jd_json(
    jd_path="data/sample_jd.txt",
    prompt_path="prompts/jd_extraction_prompt.txt"
)

with open(
    "output/jd.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        jd_data,
        file,
        indent=4
    )

print(
    "JD JSON Generated Successfully"
)
