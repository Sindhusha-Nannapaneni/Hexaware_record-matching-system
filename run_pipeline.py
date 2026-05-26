from src.matcher import RecordMatcher
from src.loader import load_json


def main():
    print("=== RECORD MATCHING PIPELINE ===\n")

    crm_records = load_json("data/crm_events.json")
    cal_records = load_json("data/calendar_events.json")

    print(f"CRM Records Loaded: {len(crm_records)}")
    print(f"Calendar Records Loaded: {len(cal_records)}\n")

    matcher = RecordMatcher()

    print("Running matching engine...\n")
    predictions = matcher.find_matches(crm_records, cal_records)

    matched = [p for p in predictions if p["match"]]

    print(f"Predicted Matches: {len(matched)}\n")

    # If you already have evaluator
    try:
        from src.evaluator import evaluate
        print("Evaluating predictions...\n")
        evaluate(predictions)
    except:
        print("Evaluator not found, skipping metrics")


if __name__ == "__main__":
    main()