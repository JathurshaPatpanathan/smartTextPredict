from flask import Flask, request, render_template
import pickle
from collections import Counter

app = Flask(__name__, template_folder='templates')

# Load the n-gram model
with open('models/ngram_model.pkl', 'rb') as f:
    bigram_freq, trigram_freq = pickle.load(f)


def predict_next_word(sequence, n=2):
    tokens = sequence.split()
    print("Tokens:", tokens)
    
    if n == 2 and len(tokens) >= 1:
        context = tuple(tokens[-1:])
        print("Bigram context:", context)
        possible_bigrams = {k: v for k, v in bigram_freq.items() if k[:1] == context}
        print("Possible bigrams:", possible_bigrams)
        if possible_bigrams:
            return max(possible_bigrams, key=possible_bigrams.get)[1]
    
    elif n == 3 and len(tokens) >= 2:
        context = tuple(tokens[-2:])
        print("Trigram context:", context)
        possible_trigrams = {k: v for k, v in trigram_freq.items() if k[:2] == context}
        print("Possible trigrams:", possible_trigrams)
        if possible_trigrams:
            return max(possible_trigrams, key=possible_trigrams.get)[2]
    
    return "No prediction available"


@app.route('/')
def index():
    return render_template('index.html', prediction="")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('input_text', '').strip()  # Get input text and remove extra spaces
    if not text:
        return render_template('index.html', prediction="No input provided")
    
    print("Received text:", text)
    n = 2  # Assume bigrams by default; adjust as needed
    next_word = predict_next_word(text, n)
    print("Predicted next word:", next_word)
    
    return render_template('index.html', prediction=next_word)

@app.errorhandler(Exception)
def handle_exception(e):
    return f"An error occurred: {e}", 500



if __name__ == '__main__':
    app.run(debug=True, port=8000)
