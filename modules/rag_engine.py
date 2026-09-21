from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def retrieve_relevant_requirements(
    question,
    requirements,
    top_k=3
):
    """
    Retrieve the most relevant requirements for
    a user's question using TF-IDF and cosine similarity.
    """

    if not requirements:
        return []

    texts = [
        req["text"]
        for req in requirements
    ]

    # -------------------------------------------------
    # Create TF-IDF vectors
    # -------------------------------------------------

    documents = texts + [question]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    try:

        matrix = vectorizer.fit_transform(
            documents
        )

    except ValueError:

        return []

    # Last vector represents the question
    question_vector = matrix[-1]

    requirement_vectors = matrix[:-1]

    similarities = cosine_similarity(
        question_vector,
        requirement_vectors
    )[0]

    # -------------------------------------------------
    # Get highest similarity requirements
    # -------------------------------------------------

    ranked_indices = similarities.argsort()[::-1]

    relevant_requirements = []

    for index in ranked_indices[:top_k]:

        relevant_requirements.append({
            "id": requirements[index]["id"],
            "text": requirements[index]["text"],
            "similarity": round(
                similarities[index] * 100,
                2
            )
        })

    return relevant_requirements


def build_rag_context(relevant_requirements):
    """
    Convert retrieved requirements into a context
    that can be provided to Gemini.
    """

    if not relevant_requirements:
        return "No relevant requirements were found."

    context = ""

    for req in relevant_requirements:

        context += (
            f"{req['id']}: "
            f"{req['text']}\n\n"
        )

    return context