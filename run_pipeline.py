from src.loader import load_json
from src.matcher import Matcher
from src.evaluator import evaluate

def main():

    print("\n=== RECORD MATCHING PIPELINE ===\n")

    # Load Data
    crm_records = load_json("data/crm_events.json")
    cal_records = load_json("data/calendar_events.json")
    labels = load_json("data/evaluation_labels.json")

    print(f"CRM Records Loaded: {len(crm_records)}")
    print(f"Calendar Records Loaded: {len(cal_records)}")

    # Run Matching
    matcher = Matcher()

    print("\nRunning matching engine...\n")

    predictions = matcher.find_matches(
        crm_records,
        cal_records
    )

    print(f"Predicted Matches: {len(predictions)}")

    # Evaluation
    print("\nEvaluating predictions...\n")

    metrics = evaluate(
        predictions,
        labels
    )

    print("===== FINAL METRICS =====")
    print(f"Precision : {metrics['precision']}")
    print(f"Recall    : {metrics['recall']}")
    print(f"F1 Score  : {metrics['f1']}")
    print("=========================\n")

if __name__ == "__main__":
    main()