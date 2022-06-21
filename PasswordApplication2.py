# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:31:17 2021

@author: surya
"""

import tkinter as tk
#part1
#let's check to see file exists first
try:
    fhand = open("passwords.txt")
except:
    print("Passwords file not found, making new one")
    file = open("passwords.txt", "w+")
    file.close()
def writeFile():
    #write file
    file2 = open("passwords.txt", "a")
    file2.write(e1.get() + str(",")+ e2.get() + str(",")+ e3.get() + '\n')
    file2.close()

master = tk.Tk()
tk.Label(master,
         text="account").grid(row=0)
tk.Label(master,
         text="username").grid(row=1)
tk.Label(master,
         text="password").grid(row=2)
#entry
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
#size
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
#buttons
tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='submit',
          command=writeFile).grid(row=3,
                                    column=2,
                                    sticky=tk.W,
                                    pady=4)
tk.mainloop()