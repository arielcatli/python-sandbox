# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:46:50 2018

@author: Ariel Domingo Catli
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Future Value Calculator")
frame = ttk.Frame(root)
frame.pack(fill = tk.X)

ttk.Label(frame, text="Monthly Investment:").grid(column="0", row="0", sticky=tk.E)
monthly_inv = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=monthly_inv).grid(column=1, row=0)
ttk.Label(frame, text="Yearly Interest Rate:").grid(column=0, row=1, sticky=tk.E)
int_rate = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=int_rate).grid(column=1, row=1)
ttk.Label(frame, text="Years:").grid(column=0, row=2, sticky=tk.E)
years = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=years).grid(column=1, row=2)
ttk.Label(frame, text="Future Value:").grid(column=0, row=3, sticky=tk.E)
future_value = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=future_value).grid(column=1, row=3)
ttk.Button(frame, text="COMPUTE").grid(column=0, row=4, columnspan=2, sticky=(tk.W, tk.E))

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
    
root.mainloop()