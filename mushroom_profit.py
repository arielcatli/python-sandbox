# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:53:11 2018

@author: Ariel Domingo Catli
"""

import tkinter as tk
from tkinter import ttk

class window():
    def __init__(self):
        
        #main window setup
        self.__root = tk.Tk()
        self.__root.title("Mushroom Profit Calculator")
        #self.__root.geometry("300x150")
        
        #data section setup
        self.__data_frame = ttk.Frame(self.__root, padding="5")
        self.__data_frame.pack(fill = tk.X)
        
        ##number of fruiting bags entry
        self.__data_frame_number_fb = ttk.Frame(self.__data_frame, padding="5")
        self.__data_frame_number_fb.pack(fill = tk.X )
        ttk.Label(self.__data_frame_number_fb, text="Number of fruiting bag(s): ").pack(side=tk.LEFT)
        self.__entry_text_number_fb = tk.StringVar()
        self.__entry_number_fb = tk.Entry(self.__data_frame_number_fb, width="20", textvariable=self.__entry_text_number_fb)
        self.__entry_number_fb.pack(side = tk.RIGHT)
        
        self.__data_frame_average_cost = ttk.Frame(self.__data_frame, padding="5")
        self.__data_frame_average_cost.pack(fill = tk.X)
        ttk.Label(self.__data_frame_average_cost, text="Average cost per FB: ").pack(side=tk.LEFT)
        self.__entry_text_average_cost = tk.StringVar()
        self.__entry_average_cost = tk.Entry(self.__data_frame_average_cost, width="20", textvariable=self.__entry_text_average_cost)
        self.__entry_average_cost.pack(side=tk.RIGHT)
        
        self.__data_frame_expected_gross_fb = ttk.Frame(self.__data_frame, padding="5")
        self.__data_frame_expected_gross_fb.pack(fill=tk.X)
        ttk.Label(self.__data_frame_expected_gross_fb, text="Gross profit per FB: ").pack(side=tk.LEFT) 
        self.__entry_text_expected_gross_fb = tk.StringVar()
        self.__entry_expected_gross_fb = ttk.Entry(self.__data_frame_expected_gross_fb, width="20", textvariable=self.__entry_text_expected_gross_fb)
        self.__entry_expected_gross_fb.pack(side=tk.RIGHT)
        
        #compute button
        self.__button_frame = ttk.Frame(self.__root, padding="5")
        self.__button_frame.pack(fill=tk.X)
        self.__button_compute = ttk.Button(self.__button_frame, text="Compute Profit", command=self.__compute)
        self.__button_compute.pack(fill=tk.X)
        
        #result section setup
        self.__result_frame = ttk.Frame(self.__root, padding="5")
        self.__result_frame.pack(fill = tk.X)
        ttk.Label(self.__result_frame, text="PROFIT: ").pack(side=tk.LEFT)
        self.__entry_text_result = tk.StringVar()
        self.__entry_result = ttk.Entry(self.__result_frame, width="40", textvariable=self.__entry_text_result)
        self.__entry_result.pack(side=tk.RIGHT)
        
        
        #start the main window
        self.__root.mainloop()
    
    def __compute(self):
        if(self.__entry_text_number_fb.get() != ""):
            if(self.__entry_text_average_cost.get() != ""):
                if(self.__entry_text_expected_gross_fb.get() != ""):
                    self.__entry_text_result.set(str(int(self.__entry_text_number_fb.get())*(int(self.__entry_text_expected_gross_fb.get())
                                    -int(self.__entry_text_average_cost.get()))))
                    self.__entry_result.pack()
        
        

if __name__ == "__main__":
    main = window()