import tkinter
import customtkinter 


def senddata():
    text= customtkinter.CTkLabel(chatarea, text="")
    text.place(relx=0.02, rely=0.02)
    text.configure(text="you: "+ chatentry.get())
    chatentry.delete(0,'end')


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

uchat=tkinter.StringVar()
chatentry = customtkinter.CTkEntry(app,width=590,height=40, textvariable=uchat)
chatentry.place(relx=0.17,rely=0.91)

sendbtn = customtkinter.CTkButton(app,text="send", command=senddata, width=110,height=40)
sendbtn.place(relx=0.01,rely=0.91)

user=chatentry.get()
chatarea = customtkinter.CTkFrame(app,width=720,height=390)
chatarea.place(rely=0.08)



#run
app.mainloop()
