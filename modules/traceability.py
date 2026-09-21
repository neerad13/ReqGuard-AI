import pandas as pd


def generate_rtm(requirements, test_cases):
    """
    Generate a Requirement Traceability Matrix.

    requirements:
        List of requirement dictionaries.

    test_cases:
        Dictionary where:
        key   = requirement ID
        value = generated test case text
    """

    rows = []

    for req in requirements:

        req_id = req["id"]
        req_text = req["text"]
        req_type = req.get("type", "Not Classified")

        # Check whether test cases exist for this requirement
        if req_id in test_cases and test_cases[req_id]:

            # We generated 3 test cases
            test_case_ids = [
                f"TC-{req_id}-01",
                f"TC-{req_id}-02",
                f"TC-{req_id}-03"
            ]

            test_case_text = ", ".join(test_case_ids)

            status = "Covered"

        else:

            test_case_text = "No Test Case Generated"
            status = "Not Covered"

        rows.append({
            "Requirement ID": req_id,
            "Requirement": req_text,
            "Type": req_type,
            "Test Cases": test_case_text,
            "Traceability": status
        })

    return pd.DataFrame(rows)