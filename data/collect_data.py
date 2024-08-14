import requests

# Collecting data from Project Gutenberg
book_url = "https://www.gutenberg.org/files/1342/1342-0.txt"
response = requests.get(book_url)
book_text = response.text

# Save the raw text data
with open('data/raw_text.txt', 'w', encoding='utf-8') as f:
    f.write(book_text)

print("Text data collected and saved.")
