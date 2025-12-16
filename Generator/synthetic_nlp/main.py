import os
from generator.sentence_builder import generate_sentence


def generate_dataset(n_samples=1000, save_path="data/synthetic/sentiment.csv"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, "w", encoding="utf-8") as f:
        f.write("text,label\n")
        for _ in range(n_samples):
            sentence, label = generate_sentence()
            f.write(f"\"{sentence}\",{label}\n")


if __name__ == "__main__":
    generate_dataset(n_samples=2000)
    print("Synthetic dataset generated.")
