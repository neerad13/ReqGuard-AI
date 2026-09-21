import re


def extract_requirements(text):
    """
    Extracts requirements from SRS text and returns
    a list of requirement objects.
    """

    lines = text.split("\n")

    requirements = []

    ignore = [

        "software requirement specification",
        "introduction",
        "purpose",
        "scope",
        "functional requirements",
        "non-functional requirements",
        "table of contents",
        "online library management system"

    ]

    counter = 1

    for line in lines:

        line = line.strip()

        if not line:
            continue

        lower = line.lower()

        if lower in ignore:
            continue

        line = re.sub(r'^\d+\.?\s*', '', line)

        if len(line) < 15:
            continue

        requirements.append(

            {
                "id": f"REQ-{counter:03}",
                "text": line,
                "type": "Unknown",
                "ambiguity": []
            }

        )

        counter += 1

    return requirements