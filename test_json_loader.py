from services.json_service import load_json

candidate_data = load_json(
    "output/candidate.json"
)

print(candidate_data["candidate_name"])