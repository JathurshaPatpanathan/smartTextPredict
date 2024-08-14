from collections import Counter
from nltk.util import ngrams
import pickle

# Load preprocessed text data
with open('data/preprocessed_text.txt', 'r', encoding='utf-8') as f:
    tokens = f.read().split()

# Generate bi-grams and tri-grams
bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

# Count frequencies
bigram_freq = Counter(bigrams)
trigram_freq = Counter(trigrams)

# Save the model
with open('models/ngram_model.pkl', 'wb') as f:
    pickle.dump((bigram_freq, trigram_freq), f)

print("N-gram model trained and saved.")