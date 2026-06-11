import re
import nltk
from nltk.corpus import stopwords

_STOPWORDS = None

def ensure_nltk():
    global _STOPWORDS
    try:
        _STOPWORDS = set(stopwords.words('english'))
    except Exception:
        nltk.download('stopwords')
        _STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    if _STOPWORDS is None:
        ensure_nltk()
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', ' ', text)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    tokens = [t for t in text.split() if t not in _STOPWORDS]
    return ' '.join(tokens)
