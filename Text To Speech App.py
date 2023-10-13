# BIG GOALS IF POSSIBLE:
# - detect langauge (spanish or english)
# - have dependent dropdown for accents (based on whether it is spanish or english)


# ALL IMPORTS
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title(" Text to Speech App") #application title
root.geometry("900x450+200+200") #how big window is
root.resizable(False, False) #cannot change size
root.configure(bg = "#305065") #coloring background

#making actual commands
engine = pyttsx3.init()

# 0 -> English: United States: Male
# 1 -> English: Australia: Male
# 2 -> Spanish: Spain: Female
# 3 -> Spanish: Spain: Male
# 4 -> Spanish: Mexico: Male
# 5 -> English: Australia: Female
# 6 -> English: United States: Female
# 8 -> Spanish: Mexico: Female

def speakNow():
    text = text_area.get(1.0, END) #getting input text
    gender = gender_combobox.get() #getting gender selection
    speed = speed_combobox.get()   #getting speed selection
    accent = accent_combobox.get()

    voices = engine.getProperty('voices')

    def setvoice():
        if ((gender == 'Male') and (accent == 'E - United States')):           # 0 -> English: United States: Male
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        if ((gender == 'Female') and (accent == 'E - United States')):       # 6 -> English: United States: Female
            engine.setProperty('voice',voices[6].id)
            engine.say(text)
            engine.runAndWait()
        
        if (gender == 'Male' and (accent == 'E - Australia')):             # 1 -> English: Australia: Male
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
        if (gender == 'Female' and (accent == 'E - Australia')):           # 5 -> English: Australia: Female
            engine.setProperty('voice',voices[5].id)
            engine.say(text)
            engine.runAndWait()

        if (gender == 'Male' and (accent == 'S - Mexico')):                # 4 -> Spanish: Mexico: Male
            engine.setProperty('voice',voices[4].id)
            engine.say(text)
            engine.runAndWait()
        if (gender == 'Female' and (accent == 'S - Mexico')):              # 7 -> Spanish: Mexico: Female
            engine.setProperty('voice',voices[8].id)
            engine.say(text)
            engine.runAndWait()

        if (gender == 'Male' and (accent == 'S - Spain')):                 # 3 -> Spanish: Spain: Male
            engine.setProperty('voice',voices[3].id)
            engine.say(text)
            engine.runAndWait()
        if (gender == 'Female' and (accent == 'S - Spain')):               # 2 -> Spanish: Spain: Female
            engine.setProperty('voice',voices[2].id)
            engine.say(text)
            engine.runAndWait()

        else:
            engine.runAndWait()

    # setting speed
    if(text):
        if(speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == "Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
        

def download():
    text = text_area.get(1.0, END) #getting input text
    gender = gender_combobox.get() #getting gender selection
    speed = speed_combobox.get()   #getting speed selection
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if(text):
        if(speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == "Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()


#icon/logo in top left corner next to 'Text to Speech App'
image_icon = PhotoImage(file="speaker.png")
root.iconphoto(False,image_icon)

#top frame (title box)
Top_frame = Frame(root,bg = "white", width = 900, height = 110)  #creating big white box
Top_frame.place(x=0,y=0) #putting at top

Logo = PhotoImage(file = "speaker SMALL.png") #making 'logo'
Label(Top_frame,image=Logo,bg = "white").place(x=15,y=5) #putting logo in big white title box

Label(Top_frame,text = "TEXT TO SPEECH",font = "Helvetica 37 bold", bg = "white", fg="black").place(x=130,y=26) #putting title in box

#LARGE text entry box
text_area = Text(root,font="Robote 15", bg = "white", relief = GROOVE, wrap=WORD) #creating text box
text_area.place(x=15,y=165,width=400,height=250) #placing the box

#selection options comboboxes
Label(root,text="LANGUAGE", font="arial 15 bold",bg = "#305065", fg="white").place(x=85,y=123) #header
Label(root,text="VOICE", font="arial 15 bold",bg = "#305065", fg="white").place(x=465,y=165) #header
Label(root,text="ACCENT", font="arial 15 bold",bg = "#305065", fg="white").place(x=615,y=165) #header
Label(root,text="SPEED", font="arial 15 bold",bg = "#305065", fg="white").place(x=780,y=165) #header

language_combobox=Combobox(root,values=['English','Spanish'],font="arial 14",state='r',width=10) #making speed 'options' box
language_combobox.place(x=225,y=123) #placing it
language_combobox.set('English') #setting original settings

gender_combobox=Combobox(root,values=['Female','Male'],font="arial 14",state='r',width=10) #making gender 'options' box
gender_combobox.place(x=435,y=200) #placing it
gender_combobox.set('Female') #setting original settings

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10) #making speed 'options' box
speed_combobox.place(x=750,y=200) #placing it
speed_combobox.set('Normal') #setting original settings

accent_combobox=Combobox(root,values=['E - United States','E - Australia', 'S - Mexico', 'S - Spain'],font="arial 14",state='r',width=10) #making speed 'options' box
accent_combobox.place(x=595,y=200) #placing it
accent_combobox.set('E - United States') #setting original settings

"""
if(language_combobox.get()=="English"):
    accent_combobox=Combobox(root,values=['United States','Australia'],font="arial 14",state='r',width=10) #making speed 'options' box
    accent_combobox.place(x=595,y=200) #placing it
    accent_combobox.set('United States') #setting original settings

if(language_combobox.get()=="Spanish"):
    accent_combobox=Combobox(root,values=['Mexico','Spain'],font="arial 14",state='r',width=10) #making speed 'options' box
    accent_combobox.place(x=595,y=200) #placing it
    accent_combobox.set('Spain') #setting original settings
"""

#buttons
speak = tk.Button(root, text = "Speak", width = 10, font = "arial 20 bold", command = speakNow)
speak.place(x=460,y=290)

save = tk.Button(root, text = "Save", width = 10, bg = "#39c790", font = "arial 20 bold", command = download)
save.place(x = 680, y = 290)


root.mainloop()
