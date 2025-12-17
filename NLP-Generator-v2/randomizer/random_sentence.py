import random

class RandomSentenceGenerator:

    def __init__(self, grammar, builder):
        self.grammar = grammar
        self.builder = builder

    # Sampling helpers

    def _sample(self, items):
        return random.choice(items)

    # Sentence generation

    def generate(self):
        sentence_type = random.choice(
            ["affirmative", "negative", "interrogative_aux", "interrogative_wh"]
        )

        if sentence_type == "affirmative":
            return self.builder.build_affirmative(
                subject=self._sample(self.grammar.subjects),
                verb=self._sample(self.grammar.verbs_positive),
                obj=self._sample(self.grammar.objects),
            )

        if sentence_type == "negative":
            return self.builder.build_negative(
                subject=self._sample(self.grammar.subjects),
                aux=self._sample(self.grammar.verbs_aux),
                verb=self._sample(self.grammar.verbs_positive),
                obj=self._sample(self.grammar.objects),
            )

        if sentence_type == "interrogative_aux":
            return self.builder.build_interrogative_aux(
                aux=self._sample(self.grammar.verbs_aux),
                subject=self._sample(self.grammar.subjects),
                verb=self._sample(self.grammar.verbs_positive),
                obj=self._sample(self.grammar.objects),
            )

        if sentence_type == "interrogative_wh":
            return self.builder.build_interrogative_wh(
                wh_word=self._sample(self.grammar.question_words),
                aux=self._sample(self.grammar.verbs_aux),
                subject=self._sample(self.grammar.subjects),
                verb=self._sample(self.grammar.verbs_positive),
            )
