def compute_sentiment(verb_sentiment, adverb_weight):
    score = verb_sentiment * adverb_weight
    return 1 if score > 0 else 0
