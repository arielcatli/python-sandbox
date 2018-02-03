# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:23:01 2018

@author: Ariel Domingo Catli
"""

#GUI exercise

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My first GUI program in Python")
root.geometry("300x200")
frame = ttk.Frame(root, padding="10 50 30 40")
frame.pack()
button1 = ttk.Button(frame, text="Ok")
button1.pack(fill=tk.BOTH, expand = True)
button2 = ttk.Button(frame, text="Cancel")
button2.pack()
root.mainloop()