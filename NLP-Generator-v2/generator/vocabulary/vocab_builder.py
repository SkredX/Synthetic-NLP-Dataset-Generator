import json

class Vocabulary:
    def __init__(self, tokenizer_path: str):
        with open(tokenizer_path, "r", encoding="utf-8") as f:
            tokenizer = json.load(f)

        # WordLevel vocab: {token: id}
        self.word2id = tokenizer["model"]["vocab"]
        self.id2word = {i: w for w, i in self.word2id.items()}

        self.vocab_size = len(self.word2id)

        # Special tokens (expected to exist)
        self.pad_token = "[PAD]"
        self.unk_token = "[UNK]"
        self.sos_token = "[SOS]"
        self.eos_token = "[EOS]"

        self.pad_id = self.word2id[self.pad_token]
        self.unk_id = self.word2id[self.unk_token]
        self.sos_id = self.word2id[self.sos_token]
        self.eos_id = self.word2id[self.eos_token]

    def encode(self, words):
        return [self.word2id.get(w, self.unk_id) for w in words]

    def decode(self, ids):
        return [self.id2word.get(i, self.unk_token) for i in ids]
