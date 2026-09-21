import re


def calculate_readability(requirement):
    """
    Calculates a simple readability score for a software requirement.

    Score:
    0-100

    Higher score = easier to understand.
    """

    text = requirement.strip()

    if not text:
        return 0

    # Count words
    words = re.findall(r"\b\w+\b", text)
    word_count = len(words)

    # Count sentences
    sentences = re.split(r"[.!?]+", text)
    sentence_count = len(
        [s for s in sentences if s.strip()]
    )

    # Count long words
    long_words = 0

    for word in words:
        if len(word) > 8:
            long_words += 1

    # Start with maximum score
    score = 100

    # Penalize long requirements
    if word_count > 25:
        score -= 10

    if word_count > 40:
        score -= 10

    if word_count > 60:
        score -= 10

    # Penalize multiple sentences
    if sentence_count > 2:
        score -= 10

    if sentence_count > 4:
        score -= 10

    # Penalize excessive long words
    if word_count > 0:

        long_word_ratio = long_words / word_count

        if long_word_ratio > 0.25:
            score -= 10

        if long_word_ratio > 0.40:
            score -= 10

    # Keep score between 0 and 100
    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return score


def get_readability_level(score):
    """
    Converts readability score into a simple level.
    """

    if score >= 80:
        return "Easy"

    elif score >= 60:
        return "Moderate"

    else:
        return "Difficult"