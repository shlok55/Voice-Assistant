import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import googletrans
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am Aenna Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('20it045@charusat.edu.in', 'shlok45@1209')
    server.sendmail('shlok.jivtode@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

#opening youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

#opening google
        elif 'open google' in query:
            webbrowser.open("google.com")

#opening stackoverflow
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

#playing music
        elif 'play ' in query:
            # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            # songs = os.listdir(music_dir)
            # print(songs)    
            # os.startfile(os.path.join(music_dir, songs[0]))
            song = query.replace('play', ' ')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

#telling time
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

#opening vscode
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

#check diabetes
        elif 'diabetes' in query:
            # codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            # os.startfile(codePath)
            rd=int(input())
            if 100< rd :
               speak('Normal it is , you are good to go')
            elif rd<100 :
                speak('Abnormal, your reading seems to be high, plwase have a visit to your nearby doctor')

#check blood pressure
            elif 'check my blood pressure' in query:
                     rd=int(input())
            if 90< rd :
               speak('your Blood pressure seems to low, might you are having low bp')
            elif rd<120 :
                speak('Seems your are having high BP , might you having high BP or you are having hypertension')

#sending whatsapp(pywhatkit)
        elif 'send reminder' in query:  
                pywhatkit.sendwhatmsg("+919313133192", "take medi ", 15,34)
#jokes
     #  elif 'joke' in query:
      #     speak(pyjokes.get_joke())

       
#sending email
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shlok.jivtode@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    

 #weather
        elif 'What is the current wheather ' in query:
            webbrowser.open("https://www.accuweather.com/en/in/changa/3040893/weather-forecast/3040893")  


 #news
        elif 'Give me latest update' in query:
            webbrowser.open("https://www.aajtak.in/")

#stockupdate
        elif 'give me stock update' in query:
            webbrowser.open("https://www.moneycontrol.com/stocksmarketsindia/")

#MIke speak
        elif 'what are we doing right now' in query:
            speak("we are having our 5 semester SGP project represntation")

#opening game
        elif 'open game' in query:
            game = "C:\Riot Games\Riot Client"
            os.startfile(game)