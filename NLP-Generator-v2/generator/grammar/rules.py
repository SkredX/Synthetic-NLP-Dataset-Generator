class GrammarRules:
    
    # Polarity:
        # +1 : Affirmative
        # -1 : Negative
        # 0 : Interrogative

    def __init__(self, vocab):
        self.vocab = vocab

        # Core lexical groups (must exist in tokenizer)
        self.subjects = ["i", "you", "he", "she", "we", "they"]
        self.verbs_positive = ["like", "love", "enjoy"]
        self.verbs_aux = ["do", "does", "did", "is", "are", "was", "were"]
        self.negators = ["not"]
        self.objects = ["this", "that", "it"]
        self.question_words = ["what", "why", "how"]

        self._validate_vocab()

    def _validate_vocab(self):
        
        all_tokens = (
            self.subjects
            + self.verbs_positive
            + self.verbs_aux
            + self.negators
            + self.objects
            + self.question_words
            + ["?"]
        )

        missing = [t for t in all_tokens if t not in self.vocab.word2id]
        if missing:
            raise ValueError(f"Missing tokens in vocabulary: {missing}")



    def affirmative(self, subject, verb, obj):
        
        return [subject, verb, obj], 1

    def negative(self, subject, aux, verb, obj):
        
        return [subject, aux, "not", verb, obj], -1

    def interrogative_aux(self, aux, subject, verb, obj):
       
        return [aux, subject, verb, obj, "?"], 0

    def interrogative_wh(self, wh_word, aux, subject, verb):
        
        return [wh_word, aux, subject, verb, "?"], 0
