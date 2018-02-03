# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:23:01 2018

@author: Ariel Domingo Catli
"""

#GUI exercise

import tkinter as tk
from tkinter import ttk

def btn1_click():
    root.title("Changing the title")

def btn2_click():
    root.destroy()
    
root = tk.Tk()
root.title("My first GUI program in Python")
root.geometry("300x200")
frame = ttk.Frame(root, padding="10 50 30 40")
frame.pack()
ttk.Label(frame, text="This is the first button").pack()
button1 = ttk.Button(frame, text="Ok", command=btn1_click)
button1.pack(fill=tk.BOTH, expand = True)
ttk.Label(frame, text="This is the last button").pack()
button2 = ttk.Button(frame, text="Cancel", comman=btn2_click)
button2.pack()
sometext = tk.StringVar()
tbox1 = ttk.Entry(frame, width=10, textvariable=sometext)
sometext.set("Type something")
tbox1.pack()
root.mainloop()



