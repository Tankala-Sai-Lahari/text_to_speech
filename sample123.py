import pyttsx3
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import os

def submit():
    n=name.get()
    t=pyttsx3.init()
    t.say(n)
    t.runAndWait()
    



#main
root=tk.Tk()
root.geometry("700x400")
root.resizable(0,0)
#icon

#Frame

frame=tk.Frame(root).pack()

#label
name=tk.StringVar()
l1=tk.Label(root,text="text :").pack()

e1=tk.Entry(root,textvariable=name).pack()


b1=tk.Button(root,text="submit",command=submit).pack()

b2=tk.Button(root,text="quit",command=root.destroy).pack()

















root.mainloop()
