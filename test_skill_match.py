import json

from services.json_service import (
    load_json
)

from services.skill_match_service import (
    generate_skill_match
)

candidate_data = load_json(
    "output/candidate.json"
)

jd_data = load_json(
    "output/jd.json"
)

skill_match_data = generate_skill_match(
    candidate_data,
    jd_data,
    "prompts/skill_match_prompt.txt"
)

with open(
    "output/skill_match.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        skill_match_data,
        file,
        indent=4
    )

print(
    "Skill Match Generated Successfully"
)