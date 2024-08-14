import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load raw text data
with open('data/raw_text.txt', 'r', encoding='utf-8') as f:
    book_text = f.read()

# Preprocessing
book_text = re.sub(r'[^a-zA-Z\s]', '', book_text)
book_text = book_text.lower()

# Tokenization and Lemmatization
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
tokens = word_tokenize(book_text)
tokens = [word for word in tokens if word not in stopwords.words('english')]
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(word) for word in tokens]

# Save the processed text data
with open('data/preprocessed_text.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(tokens))

print("Text data preprocessed and saved.")
