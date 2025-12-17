from sklearn.feature_extraction.text import CountVectorizer

def build_vectorizer():

    return CountVectorizer(
        ngram_range=(1, 2),
        lowercase=True,
        token_pattern=r"\b\w+\b|\?"
    )
