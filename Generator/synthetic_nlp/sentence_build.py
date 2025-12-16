import random
from .lexicon import (
    SUBJECTS, OBJECTS,
    POSITIVE_VERBS, NEGATIVE_VERBS,
    ADVERBS
)
from .grammar import TEMPLATE
from .labeler import compute_sentiment


def generate_sentence():
    subject = random.choice(SUBJECTS)
    obj = random.choice(OBJECTS)

    is_positive = random.choice([True, False])

    if is_positive:
        verb = random.choice(POSITIVE_VERBS)
        verb_sentiment = 1
    else:
        verb = random.choice(NEGATIVE_VERBS)
        verb_sentiment = -1

    adverb = random.choice(list(ADVERBS.keys()))
    adverb_weight = ADVERBS[adverb]

    sentence = TEMPLATE.format(
        subject=subject,
        adverb=adverb,
        verb=verb,
        object=obj
    ).replace("  ", " ").strip()

    label = compute_sentiment(verb_sentiment, adverb_weight)

    return sentence, label
