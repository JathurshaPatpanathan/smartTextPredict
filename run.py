from flask import Flask, request, jsonify, render_template
import pickle
from collections import Counter
from nltk.util import ngrams


app = Flask(_name_)

# Load the n-gram model
with open('models/ngram_model.pkl', 'rb') as f:
    bigram_freq, trigram_freq = pickle.load(f)

def predict_next_word(sequence, n=2):
    tokens = sequence.split()
    if n == 2:
        # Predict based on bigram frequency
        bigrams = [(tokens[-1], next_word) for next_word in bigram_freq if (tokens[-1], next_word) in bigram_freq]
        if bigrams:
            return max(bigrams, key=lambda x: bigram_freq[x])[1]
    elif n == 3:
        # Predict based on trigram frequency
        trigrams = [(tokens[-2], tokens[-1], next_word) for next_word in trigram_freq if (tokens[-2], tokens[-1], next_word) in trigram_freq]
        if trigrams:
            return max(trigrams, key=lambda x: trigram_freq[x])[2]
    return ""

@app.route('/')
def index():
    return render_template('index.html', prediction="")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('input_text', '')
    n = 2  # You can make this configurable if needed
    next_word = predict_next_word(text, n)
    return render_template('index.html', prediction=next_word)

if _name_ == '_main_':
    app.run(debug=True)