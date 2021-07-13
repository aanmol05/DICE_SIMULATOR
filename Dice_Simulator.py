from tkinter import *
import random


root = Tk()
root.geometry("5000x5000")

l1 = Label(root, font=("bold",200), background='pink')
l2 = Label(root, font=("bold",200),background='pink')

def rollD():
    dice= ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()

def roll():
    cusdice= ['\u2680', '\u2681', '\u2682', '\u2685', '\u2685', '\u2685']
    l1.config(text=f'{random.choice(cusdice)}{random.choice(cusdice)}')
    l1.pack()

b1 = Button(root, text="Lets Roll! ",width='12',height='2', foreground='black', background='white',command=rollD)

b1.pack()

b2 = Button(root, text="Customized Dice ",width='12',height='2', foreground='black', background='white',command=roll)

b2.pack()

root.mainloop()
