import json
from pathlib import Path

from services.skill_match_service import generate_skill_match


candidate_file = input(
    "Enter candidate json path: "
)
print(f"\nTesting Candidate: {candidate_file}\n")

with open(
    candidate_file,
    "r",
    encoding="utf-8"
) as f:
    candidate_data = json.load(f)

with open(
    "output/jd.json",
    "r",
    encoding="utf-8"
) as f:
    jd_data = json.load(f)

result = generate_skill_match(
    candidate_data,
    jd_data,
    "prompts/skill_match_prompt.txt"
)

print(
    json.dumps(
        result,
        indent=2
    )
)
candidate_name = Path(candidate_file).stem

output_file = (
    f"validation/results/{candidate_name}_result.json"
)

with open(
    output_file,
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        result,
        f,
        indent=2
    )

print(
    f"\nResult saved to: {output_file}"
)