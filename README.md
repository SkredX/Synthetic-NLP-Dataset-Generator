# Synthetic NLP Dataset Generator (NLP-Generator-v2)

A modular, grammar-driven synthetic NLP dataset generator built to study classical NLP versus structured data behavior, with explicit control over vocabulary, grammar, polarity, and data leakage.

This project focuses on understanding why models work, not just making them work.

## Project Motivation

Most beginner NLP projects:
- Use scraped or opaque datasets
- Train models without understanding why they succeed or fail
- Jump straight to deep learning without baselines

This project was designed to reverse that approach.

Key goals:
- Build a closed-vocabulary NLP system
- Explicitly control grammar and sentence polarity
- Generate fully interpretable synthetic datasets
- Establish a perfect classical baseline
- Perform EDA and model interpretability analysis
- Identify dataset leakage and limitations

## Core Ideas Demonstrated

- Symbolic NLP (grammar and rules)
- Synthetic dataset generation
- Structural labeling (not heuristic sentiment)
- Classical NLP baselines (n-grams and logistic regression)
- Dataset leakage analysis
- Exploratory Data Analysis (EDA)
- Model interpretability

## Project Structure

NLP-Generator-v2/
│
├── analysis/
│
├── data/
│   ├── tokenizer_en.json
│   └── generated/
│       └── sentences.csv
│
├── generator/
│   ├── vocabulary/
│   ├── grammar/
│   ├── sentence_builder/
│   └── __init__.py
│
├── randomizer/
│   └── random_sentence.py
│
├── models/
│   ├── classical/
│   └── __init__.py
│
├── README.md
└── main.py

## Sentence Types and Labels

The dataset is structurally labeled, not sentiment-guessed.

Affirmative: 1  
Interrogative: 0  
Negative: -1

Examples:
i love this -> 1  
i do not like this -> -1  
do you like this ? -> 0

## How the System Works

Vocabulary:
- Loaded from a WordLevel tokenizer
- Closed vocabulary
- Supports PAD, UNK, SOS, EOS

Grammar Rules:
- Deterministic sentence templates
- Explicit handling of negation, auxiliaries, and interrogatives

Sentence Builder:
- Combines vocabulary and grammar
- Outputs tokens, token IDs, sentence text, and polarity label

Random Sentence Generator:
- Adds controlled randomness
- Generates large labeled datasets safely

## Dataset Generation

Synthetic datasets are generated as CSV files.

text,token_ids,label  
i love this,"12 45 78",1  
do you like this ?,"33 21 54 78 9",0  

Advantages:
- Fully reproducible
- No scraping
- No copyright issues
- Suitable for controlled experiments

## Classical Model Baseline

Model:
- Bag-of-words and n-grams
- Logistic Regression

Result:
- Accuracy reaches 100 percent

Reason:
- Grammar rules explicitly leak labels
- Dataset is linearly separable in n-gram space

This behavior is intentional and used for analysis.

## Exploratory Data Analysis

EDA includes:
- Label distribution
- Sentence length analysis
- Token frequency
- Token-label correlation
- Model coefficient inspection

Key insight:
High accuracy does not imply semantic understanding.

## Known Limitations

- Grammar explicitly encodes labels
- Vocabulary is small and closed
- No paraphrasing or ambiguity
- No real-world noise
- Not suitable for benchmarking deep models yet

These limitations are intentional.

## Future Extensions

- Break grammar leakage
- Introduce paraphrasing and ambiguity
- Neural models with transformers
- RAG-style controlled generation
- CLI or API interface
- Dataset versioning

## Interview Talking Point

I built a grammar-controlled synthetic NLP dataset to understand why classical models succeed, performed EDA and interpretability analysis, and identified explicit sources of dataset leakage.

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Seaborn and Matplotlib
- Git and GitHub
- Kaggle

## License

Released for educational and research purposes.

## Author

SkredX
