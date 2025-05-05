import time
import tkinter as tk
# from tkinter import ttk

root=tk.Tk()
root.title("Hello world")
root.geometry('300x200')

def hello():
    print('hello world')
    print('good bye')

hello_button=tk.Button(root,text='click me',command=hello)
hello_button.pack()
root.mainloop()