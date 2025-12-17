class SentenceBuilder:

    def __init__(self, vocab, grammar):
        self.vocab = vocab
        self.grammar = grammar

    # Core build methods

    def build_affirmative(self, subject, verb, obj):
        tokens, label = self.grammar.affirmative(subject, verb, obj)
        return self._finalize(tokens, label)

    def build_negative(self, subject, aux, verb, obj):
        tokens, label = self.grammar.negative(subject, aux, verb, obj)
        return self._finalize(tokens, label)

    def build_interrogative_aux(self, aux, subject, verb, obj):
        tokens, label = self.grammar.interrogative_aux(aux, subject, verb, obj)
        return self._finalize(tokens, label)

    def build_interrogative_wh(self, wh_word, aux, subject, verb):
        tokens, label = self.grammar.interrogative_wh(wh_word, aux, subject, verb)
        return self._finalize(tokens, label)

    # Internal helpers

    def _finalize(self, tokens, label):
        token_ids = self.vocab.encode(tokens)
        text = " ".join(tokens)
        return {
            "tokens": tokens,
            "token_ids": token_ids,
            "text": text,
            "label": label
        }
