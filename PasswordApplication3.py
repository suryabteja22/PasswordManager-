# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:32:00 2021

@author: surya
"""

import tkinter as tk
import random
import string
#part2
root = tk.Tk()
root.title("Password Generator")
list = []
copy = []
def master():
    raise SystemExit
def get_entry():
    #creation of password
    text = int(e1.get())
    list.append(text)
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    all = lowercase + uppercase + numbers + numbers
    temp = random.sample(all, text)
    password = "".join(temp)
    e2.insert(0, password)
    #we want to copy that password
    copy.append(password)
#make life simple, a button to copy it
def copytext():
    global copy
    print(copy)
    root.clipboard_clear()
    root.clipboard_append(copy)
    root.update()
#we need some instructions right?
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "Enter the number of characters at the top then press enter ")
#entry
e1 = tk.Entry()
e1.pack()

e2 = tk.Entry()
e2.pack()
#button commands
b1 = tk.Button(text='Enter', command=get_entry)
b1.pack()

b2 = tk.Button(text='Quit',command=master)
b2.pack()

b3 = tk.Button(root, text="Copy Password", command=copytext)
b3.pack()

root.mainloop()