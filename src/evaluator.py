def evaluate(predictions, labels):

    predicted_pairs = set(
        (p["crm_id"], p["calendar_id"])
        for p in predictions
    )

    tp = 0
    fp = 0
    fn = 0

    for pair in labels["cross_source_pairs"]:

        key = (pair["crm_id"], pair["calendar_id"])

        if pair["match"]:

            if key in predicted_pairs:
                tp += 1
            else:
                fn += 1

        else:
            if key in predicted_pairs:
                fp += 1

    precision = tp / (tp + fp + 1e-9)
    recall = tp / (tp + fn + 1e-9)

    f1 = (
        2 * precision * recall
        / (precision + recall + 1e-9)
    )

    return {
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "f1": round(f1, 3)
    }