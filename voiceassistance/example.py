from ctypes import _NamedFuncPointer
from pip import main
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import pyaudio
import pywhatkit
import googletrans
import pyjokes

# import smtplib -- for mail sending

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice
# print(voices) ,,,, voice change available here
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning manthan makwana")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon manthan makwana")
    else:
        speak("good night manthan makwana")
    speak("hello sir i am mann how may I help you")
    
  

def takeCommand():
    print("Listening --->")
    # take microphone input from the user
#     input()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing--->")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.


        

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

if _NamedFuncPointer == "_main_":
    wishme()
    speak("what can i do for you manthan makwana")
    #  if  true:
    while 1:
       query = takeCommand().lower() 
        # Converting user query into lower case
   
        # Logic for executing tasks based on query
       if 'search in wikipedia' in query:
            # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")

            print(results)
            speak(results)

       elif 'open google' in query:
         webbrowser.open("google.com")

       elif 'play ' in query:
        song = query.replace("play", " ")
        pywhatkit.playonyt(song)
    #    elif 'search in youtube' in query:
    #     speak('Searching youtube...')
    #     webbrowser.open("youtube.com")
        # query = query.replace("youtube", "")
        # results = youtube.summary(query, sentences=2)
        
    #    elif 'joke' in query:
    #       speak(pyjokes.get_joke())
       
       
        # webbrowser.open("google.com")

    #    elif 'open vs code' in query:
    #       codePath = "C:\Users\MAKWANA RADHUSINH\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
    #       os.startfile(codepath)
    #    elif 'play music' in query:
        # music_dir='path___'
    #     songs = os.listdir(music_dir)
        #   print(songs)
        #   os.stratfile(os.path.join(music_dir,songs[0]))

       elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"time is {strTime}")
  # elif 'email to --name--' in query:
    #     try:
    #         speak("What should I say?")
    #         content = takeCommand()
    #         to = "yourEmail@gmail.com"
    #         sendEmail(to, content)
    #         speak("Email has been sent!")
    #     except Exception as e:
    #         print(e)
    #         speak("Sorry  I am not able to send this email"