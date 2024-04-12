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
def response(user_response):
    robot_response=''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    Tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(Tfidf[-1], Tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    reg_tfidf = flat[-2]
    if(reg_tfidf==0):
        robot_response= robot_response+"i'm sorry i don't understand your request"
        return robot_response
    else:
        robot_response = robot_response+sent_tokens[idx]
        return robot_response
    

#main running loop
flag= True
print("hello! how can i help you? if you want to exit just type exit any time")
while(flag==True):
    user_input= input()
    user_input= user_input.lower()
    if user_input != "exit":
        if greet(user_input)!=None:
            print("bot: "+greet(user_input))
        else:
            sent_tokens.append(user_input)
            word_tokens=word_tokens+nltk.word_tokenize(user_input)
            final_word= list(set(word_tokens))
            print("bot: "+response(user_input))
            sent_tokens.remove(user_input)
    else: 
        flag=False
        print("goodbye, take care!")


