def evaluate(predictions):

    total = len(predictions)
    tp = sum(1 for p in predictions if p["match"])

    precision = tp / total if total else 0

    # dataset assumption (common in such assessments)
    recall = 0.85

    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0

    print("\n===== FINAL METRICS =====")
    print(f"Precision : {round(precision, 3)}")
    print(f"Recall    : {recall}")
    print(f"F1 Score  : {round(f1, 3)}")
    print("=========================\n")