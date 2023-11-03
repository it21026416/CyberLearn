from nltk.tokenize import word_tokenize
import nltk

# Download necessary resources (if not already downloaded)
nltk.download('punkt') ##pretained model for tokenization 

def tokenize_text(text):
    return word_tokenize(text)
