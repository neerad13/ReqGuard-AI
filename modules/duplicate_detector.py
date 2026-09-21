from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Similarity threshold
SIMILARITY_THRESHOLD = 0.60


def detect_duplicates(requirements):

    """
    Detect potentially duplicate requirements
    using TF-IDF and cosine similarity.

    Returns a list of duplicate requirement pairs.
    """

    if len(requirements) < 2:
        return []

    # Extract requirement text
    texts = [
        req["text"]
        for req in requirements
    ]

    # Convert requirements into TF-IDF vectors
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(texts)

    # Calculate similarity between every pair
    similarity_matrix = cosine_similarity(
        tfidf_matrix
    )

    duplicate_pairs = []

    # Compare each requirement with every other requirement
    for i in range(len(requirements)):

        for j in range(i + 1, len(requirements)):

            similarity = similarity_matrix[i][j]

            if similarity >= SIMILARITY_THRESHOLD:

                duplicate_pairs.append({
                    "requirement_1": requirements[i]["id"],
                    "requirement_2": requirements[j]["id"],
                    "similarity": round(
                        similarity * 100,
                        2
                    )
                })

    return duplicate_pairs