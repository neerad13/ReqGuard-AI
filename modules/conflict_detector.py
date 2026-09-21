import re


def extract_constraints(text):
    """
    Extract simple numerical and constraint-related
    information from a requirement.
    """

    text = text.lower()

    constraints = []

    # ----------------------------
    # Numbers
    # ----------------------------

    numbers = re.findall(
        r"\b\d+(?:\.\d+)?\b",
        text
    )

    for number in numbers:
        constraints.append(
            ("number", float(number))
        )

    # ----------------------------
    # Time constraints
    # ----------------------------

    time_patterns = [
        r"\d+(?:\.\d+)?\s*(?:ms|milliseconds)",
        r"\d+(?:\.\d+)?\s*(?:s|sec|secs|seconds)",
        r"\d+(?:\.\d+)?\s*(?:min|mins|minutes)",
        r"\d+(?:\.\d+)?\s*(?:h|hr|hrs|hours)"
    ]

    for pattern in time_patterns:

        matches = re.findall(
            pattern,
            text
        )

        for match in matches:

            constraints.append(
                ("time", match)
            )

    # ----------------------------
    # Percentage constraints
    # ----------------------------

    percentages = re.findall(
        r"\d+(?:\.\d+)?\s*%",
        text
    )

    for percentage in percentages:

        constraints.append(
            ("percentage", percentage)
        )

    # ----------------------------
    # Constraint keywords
    # ----------------------------

    keywords = [
        "maximum",
        "minimum",
        "at most",
        "at least",
        "less than",
        "greater than",
        "less than or equal to",
        "greater than or equal to",
        "must",
        "must not",
        "shall",
        "shall not",
        "should",
        "should not",
        "enabled",
        "disabled",
        "allow",
        "not allow",
        "support",
        "not support"
    ]

    for keyword in keywords:

        if keyword in text:

            constraints.append(
                ("keyword", keyword)
            )

    return constraints


def detect_conflicts(requirements):
    """
    Detect potential conflicts between requirements.

    The detector looks for requirements that discuss
    similar constraint keywords but contain different
    numerical values or contradictory statements.

    Returns:
        List of potential conflicting requirement pairs.
    """

    conflicts = []

    for i in range(len(requirements)):

        text1 = requirements[i]["text"].lower()
        id1 = requirements[i]["id"]

        constraints1 = extract_constraints(text1)

        for j in range(i + 1, len(requirements)):

            text2 = requirements[j]["text"].lower()
            id2 = requirements[j]["id"]

            constraints2 = extract_constraints(text2)

            # --------------------------------
            # Find shared constraint keywords
            # --------------------------------

            keywords1 = {
                value
                for kind, value in constraints1
                if kind == "keyword"
            }

            keywords2 = {
                value
                for kind, value in constraints2
                if kind == "keyword"
            }

            shared_keywords = (
                keywords1.intersection(keywords2)
            )

            # --------------------------------
            # Compare numerical values
            # --------------------------------

            numbers1 = {
                value
                for kind, value in constraints1
                if kind == "number"
            }

            numbers2 = {
                value
                for kind, value in constraints2
                if kind == "number"
            }

            different_numbers = (
                numbers1
                and numbers2
                and numbers1 != numbers2
            )

            # --------------------------------
            # Check contradictory wording
            # --------------------------------

            contradictory_pairs = [
                ("must", "must not"),
                ("shall", "shall not"),
                ("should", "should not"),
                ("allow", "not allow"),
                ("support", "not support"),
                ("enabled", "disabled")
            ]

            contradiction_found = False

            for word1, word2 in contradictory_pairs:

                if (
                    word1 in text1
                    and word2 in text2
                ) or (
                    word2 in text1
                    and word1 in text2
                ):

                    contradiction_found = True
                    break

            # --------------------------------
            # Decide whether to flag
            # --------------------------------

            if (
                (shared_keywords and different_numbers)
                or contradiction_found
            ):

                if contradiction_found:

                    reason = (
                        "Contradictory requirement statements "
                        "were detected."
                    )

                else:

                    reason = (
                        "Similar constraints contain "
                        "different values."
                    )

                conflicts.append({
                    "requirement_1": id1,
                    "requirement_2": id2,
                    "reason": reason
                })

    return conflicts