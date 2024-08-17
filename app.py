from flask import Flask, request, jsonify, render_template
import re
import pickle

app = Flask(__name__)

# Load the n-gram model from the pickle file
with open('ngram_model.pkl', 'rb') as file:
    ngram_model = pickle.load(file)

# Define n based on your n-gram model (e.g., n=3 for trigrams)
n = 3  # Adjust this value based on your model

# Define a function to predict the next word based on the n-gram model
def predict_next_word(seed_text, ngram_model):
    words = seed_text.split()
    last_n_gram = tuple(words[-(n-1):])  # Get the last n-1 words
    if last_n_gram in ngram_model:
        return ngram_model[last_n_gram]  # Adjust based on your model's structure
    else:
        return ''  # or some default/fallback word

def generate_text(seed_text, next_words=50):
    for _ in range(next_words):
        predicted_word = predict_next_word(seed_text, ngram_model)
        if not predicted_word:
            break  # Stop if no prediction is available
        seed_text += ' ' + predicted_word
    return seed_text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    seed_text = request.form['text']  # Get the seed text from the form
    output_text = generate_text(seed_text)  # Generate text based on the seed text
    return jsonify({'generated_text': output_text})  # Return the generated text as a JSON response

if __name__ == '__main__':
    app.run(debug=True)




