import numpy as np
from bs4 import BeautifulSoup
import unidecode
import contractions
import re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

stopwords_set = set(stopwords.words('english'))
lmtzr = WordNetLemmatizer()
tokenizer = TreebankWordTokenizer()

def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def remove_accented_chars(text):
    return unidecode.unidecode(text)
#     return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')


def expand_contractions(text):
    return contractions.fix(text)

# def lemmatize_text(text):
#     text = nlp(text)
#     text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
#     return text

def lemmatize_text(text):
    return ' '.join([lmtzr.lemmatize(word) for word in tokenizer.tokenize(text)])

def remove_stopwords(text):
    return ' '.join([word for word in text.split(' ') if word.lower() not in stopwords_set])

def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text

def normalize_doc(doc, html_stripping=True, contraction_expansion=True,
                     accented_char_removal=True, text_lower_case=True, 
                     text_lemmatization=True, special_char_removal=True, 
                     stopword_removal=True, remove_digits=True):
    # strip HTML
    if html_stripping:
        doc = strip_html_tags(doc)

    # remove accented characters
    if accented_char_removal:
        doc = remove_accented_chars(doc)

    # expand contractions    
    if contraction_expansion:
        doc = expand_contractions(doc)

    # lowercase the text    
    if text_lower_case:
        doc = doc.lower()

    
    # remove extra newlines
    doc = re.sub(r'[\r|\n|\r\n]+', ' ',doc)

    # lemmatize text
    if text_lemmatization:
        doc = lemmatize_text(doc)

    # remove special characters and\or digits    
    if special_char_removal:
        # insert spaces between special characters to isolate them    
        special_char_pattern = re.compile(r'([{.(-)!}])')
        doc = special_char_pattern.sub(" \\1 ", doc)
        doc = remove_special_characters(doc, remove_digits=remove_digits)  

    # remove extra whitespace
    doc = re.sub(' +', ' ', doc)

    # remove stopwords
    if stopword_removal:
        doc = remove_stopwords(doc)
        
    return doc

def normalize_corpus(corpus):
    return np.array([normalize_doc(doc) for doc in corpus])