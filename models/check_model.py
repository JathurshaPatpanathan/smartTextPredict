import pickle

with open('models/ngram_model.pkl', 'rb') as f:
    bigram_freq, trigram_freq = pickle.load(f)

print(type(bigram_freq))
print(type(trigram_freq))

#print("Bigram frequencies:", bigram_freq)
#print("Trigram frequencies:", trigram_freq)

print(predict_next_word("hi", n=2))  # Should print a prediction if data is present
print(predict_next_word("hi there", n=2))  # Test with known context



