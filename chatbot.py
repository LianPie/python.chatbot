import nltk.stem.wordnet
import numpy as np #
import nltk #for natural language processing
import string #process and handle strings
import random #randomizes response 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter
import customtkinter


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
    le= len(vals[0])
    i= random.randint(le-5,le-1)
    idx = vals.argsort()[0][i]
    flat = vals.flatten()
    flat.sort()
    reg_tfidf = flat[-2]
    if(reg_tfidf==0):
        robot_response= robot_response+"i'm sorry i don't understand your request"
        return robot_response
    else:
        robot_response = robot_response+sent_tokens[idx]
        return robot_response
    

flag= True

#main running loop
def processUserinput(user_input,sent_tokens=sent_tokens,word_tokens=word_tokens):
    user_input= user_input.lower()
    if user_input != "exit":
        if greet(user_input)!=None:
            botreply(greet(user_input))
        else:
            sent_tokens.append(user_input)
            word_tokens=word_tokens+nltk.word_tokenize(user_input)
            final_word= list(set(word_tokens))
            botreply(response(user_input))
            sent_tokens.remove(user_input)
    else: 
        flag=False
        botreply("goodbye, take care!")
        app.destroy()

def senddata():
    text.configure(text= chatentry.get())
    processUserinput(chatentry.get())
    print(chatentry.get())
    chatentry.delete(0,'end')

def botreply(bot):
    print(bot)
    res.configure(text= bot)

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("chatbot")

#elements
title = customtkinter.CTkLabel(app, text= "start chatting!")
title.place(relx=0.46,rely=0.01)


chatarea = customtkinter.CTkFrame(app,width=720,height=200)
chatarea.place(rely=0.08)
resarea = customtkinter.CTkFrame(app,width=720,height=200)
resarea.place(rely=0.5)
texttitle= customtkinter.CTkLabel(chatarea, text="you:", font=("Courier", 30))
texttitle.place(relx=0.02, rely=0.02)
restitle= customtkinter.CTkLabel(resarea, text="bot:", font=("Courier", 30))
restitle.place(relx=0.02, rely=0.02)

res= customtkinter.CTkLabel(resarea,text="" , wraplength=500,justify="left")
res.place(relx=0.02, rely=0.2)
text= customtkinter.CTkLabel(chatarea, text="", wraplength=500, justify="left")
text.place(relx=0.02, rely=0.2)




uchat=tkinter.StringVar()
chatentry = customtkinter.CTkEntry(app,width=590,height=40, textvariable=uchat)
chatentry.place(relx=0.17,rely=0.91)

sendbtn = customtkinter.CTkButton(app,text="send", command=senddata, width=110,height=40)
sendbtn.place(relx=0.01,rely=0.91)

user=chatentry.get()

bot=("hello! i can give you information about cybersecurity! if you want to exit just type exit any time")
botreply(bot)
app.mainloop()





