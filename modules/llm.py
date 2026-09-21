import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-3.6-flash"


def rewrite_requirement(requirement):

    prompt = f"""
You are a Senior Software Requirements Engineer.

Rewrite the following software requirement.

Rules:
- Remove ambiguity
- Make it measurable
- Follow IEEE SRS style
- Keep the same meaning
- Return ONLY the rewritten requirement

Requirement:
{requirement}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text