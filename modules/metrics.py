from modules.quality_score import calculate_quality_score
from modules.ambiguity_detector import detect_ambiguity


def calculate_metrics(requirements):

    total = len(requirements)

    ambiguous_count = 0

    scores = []

    for req in requirements:

        # req is now a dictionary
        ambiguous = detect_ambiguity(req["text"])

        if ambiguous:
            ambiguous_count += 1

        scores.append(
            calculate_quality_score(ambiguous)
        )

    average = 0

    if scores:
        average = sum(scores) / len(scores)

    return {
        "total": total,
        "ambiguous": ambiguous_count,
        "good": total - ambiguous_count,
        "average": round(average)
    }