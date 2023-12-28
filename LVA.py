#1 INCLUDING THE MODULES

#install pyttsx3, speechRecognition, wikipedia and os using pip or pipwin
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
from tkinter import *    #module to add GUI
from PIL import ImageTk,Image   #use for accepting all file types


#2 CONFIGURING THE VOICE OF LAPOIS-VA
engine = pyttsx3.init('sapi5')  #sapi5 - Microsoft developed speech API.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Voice id helps us to select different voices. 


#3 FUNCTION FOR LAPOIS-VA AUDIO
def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command speech is not audiable to the user


#4 FUNCTION FOR TAKING VOICE INPUT FROM USER AND RETURN STRING OUTPUT
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Please repeat, I can't hear your voice") 
        return "None"
    return query

#5 ADDING GUI OF VIRTUAL ASSISTANT
class Widget: 
    #I FUNCTION FOR GUI
    def __init__(self):
        # Greet the user according to the time of computer or PC
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

        speak(" I am Lapois. Please tell me how may I help you")
        
        # DESIGN FOR GUI
        lva =Tk()

        # TITLE
        lva.title('LAPOIS - VIRTUAL ASSISTANT')
        
        # ICON
        lva.iconbitmap(r'voiceicon.ico')

        # WIDTH AND HEIGTH
        lva.geometry('805x410')

        # ADDING BACKGROUND IMAGE, TEXT AND BUTTON
        img = ImageTk.PhotoImage(Image.open("LAPOIS.jpg"))
        panel = Label(lva, image=img) 
        panel.pack(side='right', fill='both', expand='no') 

        userText = StringVar()

        userText.set('WELCOME')

        userFrame = LabelFrame(lva, text='LAPOIS', font=('Times New Roman', 30), fg='#191919')
        userFrame.pack(fill='both', expand='yes')

        top = Message(userFrame, textvariable=userText, padx=10, pady=25, font=("Century Gothic", 15, "bold"), bg='black',  fg='#ADD8E6' ) 
        top.pack(side='top', fill='both', expand='yes')

        Button(lva, text='START', padx=10, pady=10, font=('railways', 10, 'bold'), bg='green', fg='#ADD8E6', command=self.clicked ).pack(fill='x', expand='no')
        
        # CALLING THE GUI FUNCTION
        lva.mainloop() 
    
    #II FUNCTION AFTER START BUTTON
    def clicked(self):
        print("Speak something...")
        while True:
            query = takeCommand().lower()

            # Condition for executing tasks based on query
            # opening wikipedia
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            # opening youtube
            if 'youtube' in query:
                webbrowser.open("youtube.com")
                speak("Here's your Youtube")

            # opening google
            if 'google' in query:
                webbrowser.open("google.com")
                speak("Here's your Google Search Engine")

            # opening stack overflow
            if 'stack overflow' in query:
                webbrowser.open("stackoverflow.com")   
                speak("Here's is the programmers forum Stack overflow")

            # opening the time
            if 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"the time is {strTime}")

            # opening notepad
            if 'notepad' in query:
                os.startfile('notepad.exe')

            # exit from LAPOIS-VA
            if 'exit' in query:
                speak('Thank you have a good day')
                exit()
#6 FUNCTION CALLING FOR GUI
if __name__ == "__main__":
    widget = Widget()