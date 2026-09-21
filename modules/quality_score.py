def calculate_quality_score(ambiguous_words):

    """
    Calculates a quality score out of 100.
    More ambiguous words = lower score.
    """

    score = 100

    deduction = len(ambiguous_words) * 10

    score -= deduction

    if score < 0:
        score = 0

    return score