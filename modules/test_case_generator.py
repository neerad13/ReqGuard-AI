import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-3-flash-preview"


def generate_test_cases(requirement):

    prompt = f"""
You are a Senior Software Testing Engineer.

Generate test cases for the following software requirement.

Requirement:
{requirement}

Generate exactly 3 test cases.

For each test case provide:

Test Case ID:
Description:
Precondition:
Test Steps:
Expected Result:

Rules:
- Test cases must directly relate to the requirement.
- Include both positive and negative scenarios where possible.
- Make the expected result measurable and specific.
- Do not invent unrelated functionality.
- Return ONLY the test cases.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text