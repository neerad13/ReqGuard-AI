import re


# -------------------------------------------------
# IEEE-STYLE SRS SECTIONS
# -------------------------------------------------

REQUIRED_SECTIONS = {
    "Introduction": [
        "introduction"
    ],

    "Purpose": [
        "purpose"
    ],

    "Scope": [
        "scope"
    ],

    "Overall Description": [
        "overall description",
        "overall product description",
        "product perspective"
    ],

    "Functional Requirements": [
        "functional requirements",
        "functional requirement",
        "system features",
        "functional specification"
    ],

    "Non-Functional Requirements": [
        "non-functional requirements",
        "nonfunctional requirements",
        "non functional requirements"
    ],

    "External Interfaces": [
        "external interfaces",
        "external interface requirements",
        "interface requirements"
    ],

    "Performance Requirements": [
        "performance requirements",
        "performance requirement"
    ],

    "Security Requirements": [
        "security requirements",
        "security requirement"
    ],

    "Constraints": [
        "constraints",
        "design constraints",
        "implementation constraints"
    ],

    "Assumptions and Dependencies": [
        "assumptions and dependencies",
        "assumptions",
        "dependencies"
    ]
}


def normalize_text(text):
    """
    Convert text into a normalized form so that
    section matching becomes easier.
    """

    text = text.lower()

    # Replace multiple spaces/newlines with one space
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def check_ieee_compliance(srs_text):
    """
    Check whether important IEEE-style SRS sections
    are present in the uploaded SRS.

    Returns:
        dictionary containing section status,
        score and summary.
    """

    normalized_text = normalize_text(srs_text)

    results = {}

    for section, keywords in REQUIRED_SECTIONS.items():

        found = False

        for keyword in keywords:

            if keyword in normalized_text:
                found = True
                break

        results[section] = (
            "Present" if found else "Missing"
        )

    # -------------------------------------------------
    # Calculate Score
    # -------------------------------------------------

    total_sections = len(results)

    present_sections = sum(
        1
        for status in results.values()
        if status == "Present"
    )

    score = round(
        (present_sections / total_sections) * 100
    )

    # -------------------------------------------------
    # Compliance Level
    # -------------------------------------------------

    if score >= 80:
        level = "High"

    elif score >= 60:
        level = "Moderate"

    else:
        level = "Low"

    return {
        "sections": results,
        "score": score,
        "level": level
    }