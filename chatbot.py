import numpy as np #
import nltk #for natural language processing
import string #process and handle strings
import random #randomizes response 

convF=open('conversationcorpus.txt','r',errors='ignore')
rawconv= convF.read()
rawconv=rawconv.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(rawconv)
word_tokens = nltk.word_tokenize(rawconv)

print(sent_tokens[:2])





