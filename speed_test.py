import tkinter as tk
from random import choice
from tkinter import messagebox
import time
from difflib import SequenceMatcher

with open('/Users/andriiminets/Desktop/My_python/Portfolio/My_python/sentences.txt', 'r') as file:
    lines = file.readlines()


class MyGUI:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Speed Test')

        self.title = str(choice(lines))

        self.out_frame = tk.Frame(self.window) 
        self.out_frame.pack(padx=20, pady=20)

        self.label = tk.Label(self.out_frame, text=self.title, font=('Arial', 15))
        self.label.grid(row=0, column=0)
       
        self.result = tk.Label(self.out_frame, text='', font=('Arial', 15))
        self.result.grid(row=2, column=0, pady=10)

        self.textbox = tk.Entry(self.out_frame, width=70, font=('Arial', 15))
        self.textbox.grid(row=1, column=0)
        self.textbox.bind("<Return>", self.enter)
        self.textbox.bind('<Button-1>', self.time_start)

        self.check = tk.Button(self.out_frame, text='Done', font=('Arial', 10), command=self.show_m)
        self.check.grid(row=3, column=0)
        
        
        self.window.mainloop()
        
    def time_start(self, event):
        self.start = time.time()

    def enter(self, event):
        self.end = time.time()
        self.show_m()

    def show_m(self):
        self.nt = self.label['text'].strip()
        self.tx = self.textbox.get()
        w = SequenceMatcher(None, self.nt, self.tx).ratio()
        self.time_result = f"{round((self.end - self.start), 2)} seconds"
        self.result['text'] = f"{str(self.time_result)} Accuracy {int(w * 100)}%"


MyGUI()
