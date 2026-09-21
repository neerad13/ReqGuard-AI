import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-3-flash-preview"


def generate_project_health(requirements):

    text = ""

    for req in requirements:
        text += req["text"] + "\n"


    prompt = f"""
You are a Senior Software Requirements Engineering expert.

Analyze the following Software Requirements Specification.

Evaluate the overall quality of the SRS based on:

1. Requirement clarity
2. Ambiguity
3. Measurability
4. Consistency
5. Performance specifications
6. Security specifications
7. Completeness

Return ONLY plain text.

Use exactly this format:

Overall Project Score:
<score>/100

Strengths:
- strength 1
- strength 2
- strength 3

Weaknesses:
- weakness 1
- weakness 2
- weakness 3

Recommendations:
- recommendation 1
- recommendation 2
- recommendation 3


SRS Requirements:

{text}
"""


    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text