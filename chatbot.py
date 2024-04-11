import nltk.stem.wordnet
import numpy as np #
import nltk #for natural language processing
import string #process and handle strings
import random #randomizes response 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity




#importing and reading the corpus
convF=open('testcorpus.txt','r',errors='ignore')
rawconv= convF.read()
rawconv=rawconv.lower()
nltk.download('punkt') #pretrained tokenizer
nltk.download('wordnet') #english semantic dictionary 
sent_tokens = nltk.sent_tokenize(rawconv) #list of sentences in doc 
word_tokens = nltk.word_tokenize(rawconv)

print(sent_tokens[:2])

#text preprocessing
lemmer = nltk.stem.WordNetLemmatizer() #grouping together the inflected forms of a word
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict= dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


#greating function
Greeting_inputs = ("hello", "hi","hey")
Greeting_responses=["hello there!","hello","hi"]
def greet(sentence):
    for word in sentence.split():
        if word.lower() in Greeting_inputs:
            return random.choice(Greeting_responses)


#response generation




