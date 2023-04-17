import tkinter as tk
from random import choice
from tkinter import messagebox
import time
from difflib import SequenceMatcher

with open('sentences.txt', 'r') as file:
    lines = file.readlines()


class MyGUI:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Accuracy Test')
        self.inner_frame = tk.Frame(self.window)
        self.inner_frame.pack(padx=20, pady=20)

        self.title = str(choice(lines))

        self.out_frame = tk.LabelFrame(self.inner_frame, text='Rewrite this text', font=('Arial', 15), foreground='green') 
        self.out_frame.grid(row=0, column=0, sticky='news')

        self.label = tk.Label(self.out_frame, text=self.title, font=('Arial', 25))
        self.label.grid(row=0, column=1)
       
        self.out_frame2 = tk.LabelFrame(self.inner_frame, text='Type as fast as you can', font=('Arial', 15), foreground='green')
        self.out_frame2.grid(row=1, column=0)

        self.result = tk.Label(self.out_frame2, text='', font=('Arial', 25))
        self.result.grid(row=2, column=0, pady=10)

        self.textbox = tk.Entry(self.out_frame2, width=70, font=('Arial', 25))
        self.textbox.grid(row=1, column=0, padx=10)
        self.textbox.bind("<Return>", self.enter)
        self.textbox.bind('<Button-1>', self.time_start)

        self.check = tk.Button(self.inner_frame, text='Done', font=('Arial', 10), command=self.show_m)
        self.check.grid(row=3, column=0, pady=10)
        
        
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
