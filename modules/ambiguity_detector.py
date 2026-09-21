

AMBIGUOUS_WORDS = [

    "fast",
    "quick",
    "quickly",
    "efficient",
    "efficiently",
    "easy",
    "easily",
    "simple",
    "user-friendly",
    "appropriate",
    "optimal",
    "minimum",
    "maximum",
    "soon",
    "sufficient",
    "adequate",
    "normal",
    "better",
    "good",
    "bad",
    "large",
    "small"

]


def detect_ambiguity(requirement):

    """
    Returns all ambiguous words present
    inside a requirement.
    """

    found_words = []

    requirement = requirement.lower()

    for word in AMBIGUOUS_WORDS:

        if word in requirement:

            found_words.append(word)

    return found_words