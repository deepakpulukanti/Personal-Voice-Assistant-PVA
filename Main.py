from tkinter import *
import tkinter
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import filedialog
import speech_recognition as sr
import os
from os import walk
import subprocess
import webbrowser
from gtts import gTTS   
import playsound

main = Tk()
main.title("PERSONAL VOICE ASSISTANT")
main.geometry("1300x1200")

def play():
    data = text.get("1.0",END) 
    print("test "+data)
    t1 = gTTS(text=data, lang='en', slow=False) 
    t1.save("output.mp3")
    playsound("output.mp3")

def runOffline(data):
    data = data.lower()
    current = 0
    total = 0
    count = 0
    arr = data.split(" ")
    i = 0
    while i < len(arr):
        print(str(arr[i])+" "+str(arr[i].isnumeric())+" "+str(i))
        if arr[i].isnumeric():
            current = float(arr[i])
            count = count + 1
        if total == 0:
            total = current
            #play()
        if arr[i] == 'into' or arr[i] == '*':
            i = i + 1
            current = float(arr[i])
            total = total * current
            #play()
        if arr[i] == 'plus' or arr[i] == '+':
            i = i + 1
            current = float(arr[i])
            total = total + current
            #play()
        if arr[i] == 'minus' or arr[i] == '-':
            i = i + 1
            current = float(arr[i])
            total = total - current
            #play()
        if arr[i] == 'divide':
            total = total / current
            #play()
        if arr[i] == 'percentage':
            i = i + 1
            current = float(arr[i])
            total = total / count
            #play()
        if arr[i] == 'power':
            i = i + 1
            current = float(arr[i])
            total = pow(total,current)
            #play()
        if arr[i] == 'root':
            i = i + 1
            current = float(arr[i])
            total = total ** count
            #play()
        if arr[i] == 'increase':
            i = i + 1
            current = float(arr[i])
            total = total + 1
            #play()
        if arr[i] == 'decrease':
            i = i + 1
            current = float(arr[i])
            total = total - 1
            #play()
        if arr[i] == 'table':
            i = i + 2
            current = int(arr[i])
            for k in range(1,11):
                text.insert(END,str(current)+" * "+str(k)+" = "+str(current * k)+"\n")
            #play()    
        i = i + 1    
    return total            


def offline():
    text.delete('1.0', END)
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        text.insert(END,"speak\n")
        text.update_idletasks()
        print('speak')
        r.adjust_for_ambient_noise(source)
        audio = r.record(source,duration=5)
        data = r.recognize_google(audio)
        text.insert(END,"Received Command : "+data+"\n")
        text.update_idletasks()
        total = runOffline(data+"\n\n")
        text.insert(END,"Computed Result Below\n\n"+str(total)+"\n")
        text.update_idletasks()
    play()
    
    

def runOnline(command):
    data = command.lower()
    data = data.strip("\n")
    data = data.strip()
    arr = data.split(" ")
    i = 0
    while i < len(arr):
        print(str(i)+" "+arr[i])
        if arr[i].strip("\n").strip() == 'search':
            i = i + 1
            url = "https://www.google.com.tr/search?q={}".format(arr[i])
            webbrowser.open_new_tab(url)
        if arr[i].strip("\n").strip() == 'settings':
            subprocess.Popen([r"C:/Windows/System32/DpiScaling.exe"])
        if arr[i].strip("\n").strip() == 'wi-fi':
            i = i + 1
            if arr[i].strip("\n").strip() == 'on':
                os.system("netsh interface set interface 'Wifi' enabled")
            if arr[i].strip("\n").strip() == 'off':
                os.system("netsh interface set interface 'Wifi' disabled")        
        if arr[i].strip("\n").strip() == 'open':
            i = i + 1
            name = arr[i]
            name = name.strip("\n")
            name = name.strip()
            print(str(os.path.exists('E:/'+name+".txt"))+" "+str(name))
            if os.path.exists('E:/'+name+".txt"):
                os.system("start " + 'E:/'+name+".txt")
            if os.path.exists('E:/'+name+".doc"):
                os.system("start " + 'E:/'+name+".doc")
            if os.path.exists('E:/'+name+".docx"):
                os.system("start " + 'E:/'+name+".docx")
            if os.path.exists('E:/'+name+".pdf"):
                os.system("start " + 'E:/'+name+".pdf")
            if os.path.exists('E:/'+name+".jpg"):
                os.system("start " + 'E:/'+name+".jpg")
            if os.path.exists('E:/'+name+".png"):
                os.system("start " + 'E:/'+name+".png")
            if os.path.exists('E:/'+name+".gif"):
                os.system("start " + 'E:/'+name+".gif")
        i = i + 1        
    

def online():
    text.delete('1.0', END)
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        text.insert(END,"speak\n")
        text.update_idletasks()
        print('speak')
        r.adjust_for_ambient_noise(source)
        audio = r.record(source,duration=5)
        data = r.recognize_google(audio)
        text.insert(END,"Received Command : "+data+"\n")
        text.update_idletasks()
        runOnline(data+"\n\n")
    #play()
        
    

def close():
    main.destroy()

    
font = ('times', 15, 'bold')
title = Label(main, text='PERSONAL VOICE ASSISTANT')
#title.config(bg='powder blue', fg='olive drab')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 13, 'bold')
ff = ('times', 12, 'bold')

offlineButton = Button(main, text="Offline Mathematical Operations", command=offline)
offlineButton.place(x=300,y=100)
offlineButton.config(font=ff)


onlineButton = Button(main, text="Online Operations", command=online)
onlineButton.place(x=300,y=150)
onlineButton.config(font=ff)

exitButton = Button(main, text="Exit", command=close)
exitButton.place(x=300,y=200)
exitButton.config(font=ff)


font1 = ('times', 12, 'bold')
text=Text(main,height=25,width=130)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=250)
text.config(font=font1)

main.config()
main.mainloop()
