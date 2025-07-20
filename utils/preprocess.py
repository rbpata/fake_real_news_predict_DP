import re
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences

nltk.download('stopwords')
ps = PorterStemmer()
voc_size = 5000
sent_len = 10


def clean_text(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    return ' '.join(review)


def text_to_sequence(text):
    corpus = [clean_text(text)]
    onehot = [one_hot(words, voc_size) for words in corpus]
    return pad_sequences(onehot, padding='pre', maxlen=sent_len)