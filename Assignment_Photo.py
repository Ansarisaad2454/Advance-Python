import tkinter
from tkinter import *
import random

w=Tk()
w.geometry("700x450")

d1=tkinter.PhotoImage(file="1.png")
d2=tkinter.PhotoImage(file="2.png")
d3=tkinter.PhotoImage(file="3.png")
d4=tkinter.PhotoImage(file="4.png")
d5=tkinter.PhotoImage(file="5.png")
d6=tkinter.PhotoImage(file="6.png")

def roll():
    dice=[d1,d2,d3,d4,d5,d6]
    side=random.choice(dice)
    label=Label(w,image=side)
    if(side==d1):
        lable2 = Label(w, text="Your Number is 1",font=10)
        lable2.place(x=300,y=10)
    elif(side==d2):
        lable2 = Label(w, text="Your Number is 2", font=10)
        lable2.place(x=300,y=10)
    elif (side == d3):
        lable2 = Label(w, text="Your Number is 3",  font=10)
        lable2.place(x=300,y=10)
    elif (side == d4):
        lable2 = Label(w, text="Your Number is 4", font=10)
        lable2.place(x=300,y=10)
    elif (side == d5):
        lable2 = Label(w, text="Your Number is 5", font=10)
        lable2.place(x=300,y=10)
    elif (side == d6):
        lable2 = Label(w, text="Your Number is 6", font=10)
        lable2.place(x=300,y=10)
    label.place(x=230,y=50)

button=Button(w,text="Roll",width=40,height=5,font=10,bg="white",bd=2,command=roll)
button.place(x=150,y=300)

w.mainloop()