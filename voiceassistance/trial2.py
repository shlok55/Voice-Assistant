from tkinter import *
from timeit import default_timer as timer
from nltk.tokenize import word_tokenize
import nltk
import string
from gtts import gTTS
from io import BytesIO
import pygame
import playsound
i=0
stopwords = nltk.corpus.stopwords.words('english')
h=" "
def speak(txt,language = 'en'):
    mp3_fo=BytesIO()
    tts=gTTS(txt,lang=language)
    tts.write_to_fp(mp3_fo)
    return mp3_fo
def removep(txt):
    text="".join([c for c in txt if c not in string.punctuation])
    return text
def clean(txt):
    word=[i for i in txt if i not in stopwords]
    return word
def stopwfree(input):
    word=clean(word_tokenize(removep(input).lower()))
    w=' '.join([str(elem) for elem in word])
    return w
def printInput():
    end1()
    inp=T.get(1.0, "end-1c")
    h1="Word count:"+str(detectw(inp))
    lbl.config(text =h1,font=("Arial", 15))
    h2="Line count:"+str(detectl(inp))
    lbl2.config(text =h2,font=("Arial", 15))
    h3="Alpha-numeric character count:"+str(detectalnum(inp))
    lbl3.config(text =h3,font=("Arial", 15))
    h4 = "Numeric count:"+str(detectnum(inp))
    lbl4.config(text = h4,font=("Arial", 15))
    h5 = "Uppercase character count:"+str(detectupper(inp))
    lbl5.config(text = h5,font=("Arial", 15))
    h6 = "Lowercase character count:"+str(detectlower(inp))
    lbl6.config(text = h6,font=("Arial", 15))
    h7 = "Time taken : " +str(check())+" seconds"
    lbl7.config(text= h7,font=("Arial", 15))
    h8 = "Typing speed : " +str(speed(inp))+" words per minute"
    lbl8.config(text=h8,font=("Arial", 15))
    global i
    i=0
    h9 = "Your message after removing stop words and punctuations : "+str(stopwfree(inp)) 
    lbl10.config(text= h9,font=("Arial", 15))
    global h
    h = h1+h2+h3+h4+h5+h6+h7+h8+h9
    spell()
def spell():
     pygame.init()
     pygame.mixer.init()
     sound=speak(h)
     pygame.mixer.music.load(sound,'mp3')
     pygame.mixer.music.play()
def typingSpeed():
     global start
     start = timer()
     global i
     i=1
def end1():
    global end
    end=timer()
def check():
    if i==0:
        return "Not Applicable"
    return end-start
def speed(string):
     if i==0:
         return "Not Applicable"
     return ((detectw(string)*60)/(end-start))
def detectw(string):
    count=0;
    p=word_tokenize(removep(string))
    l=len(p)
    return l
def detectl(string):
    count=0;
    l=len(string);
    for i in range (0,l):
        if(string[i]=="\n"or i==l-1):
            count+=1
    return(count)
def detectalnum(string):
    count=0;
    l=len(string);
    for i in range (0,l):
        if(string[i].isalnum()==True):
            count+=1
    return(count)   
def detectnum(string):
    count=0;
    l=len(string);
    for i in range (0,l):
        if(string[i].isnumeric()==True):
            count+=1;
    return(count)  
def detectupper(string):
    count=0;
    l=len(string);
    for i in range (0,l):
        if(string[i].isupper()==True):
            count+=1
    return(count)  
def detectlower(string):
    count=0;
    l=len(string);
    for i in range (0,l):
        if(string[i].islower()==True):
            count+=1
    return(count)  

m=Tk()
m.geometry('1500x900')
m.minsize(1500,900)
m.maxsize(1500,900)
m.title('Text Mining Tool')
m.config(bg="#ADD8E6")
lbl11 = Label(m, text = "Write your text here for mining!", font=("Arial", 25))
lbl11.config(bg="#ADD8E6")
lbl11.pack(pady=10)
lbl12 = Label(m, text = "If you want to calculate your typing speed:", font=("Arial", 25))
lbl12.config(bg="#ADD8E6")
lbl12.pack()
button1 = Button(m, text='Calculate typing speed', width=25,font=("Arial", 15),command=typingSpeed)
button1.config(bg="#FFB6C1")
button1.place(x=1060,y=80)
T = Text(m, height=15, width=110,font=("Arial", 15))
T.pack(pady=21)   
button = Button(m, text='Ask', width=25,font=("Arial", 15), command=printInput)
button.config(bg="#FFB6C1")
button.pack(pady=16)
lbl = Label(m, text = "")
lbl.config(bg="#ADD8E6")
lbl.pack()
lbl2 = Label(m, text = "")
lbl2.config(bg="#ADD8E6")
lbl2.pack()
lbl3 = Label(m, text = "")
lbl3.config(bg="#ADD8E6")
lbl3.pack()
lbl4 = Label(m, text = "")
lbl4.config(bg="#ADD8E6")
lbl4.pack()
lbl5 = Label(m, text = "")
lbl5.config(bg="#ADD8E6")
lbl5.pack()
lbl6 = Label(m, text = "")
lbl6.config(bg="#ADD8E6")
lbl6.pack()
lbl7 = Label(m, text = "")
lbl7.config(bg="#ADD8E6")
lbl7.pack()
lbl8 = Label(m, text = "")
lbl8.config(bg="#ADD8E6")
lbl8.pack()
lbl10 = Label(m, text = "")
lbl10.config(bg="#ADD8E6")
lbl10.pack()

m.mainloop()