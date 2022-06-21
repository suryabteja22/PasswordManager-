# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:07:28 2021

@author: surya
"""
#os.system('PasswordApplication.py')
#import sys
import os
from tkinter import *
import tkinter as tk
window=Tk()
#made By Surya Bairisetti
window.title("Surya's Final project")
window.geometry('270x200')
text = Label(window, text="Welcome to the password management program")
text.place(x=0,y=90)
text2 = Label(window, text="Made By Surya Bairisetti")
text2.place(x=75,y=120)
#to run the new entry program
def run1():
    #os.system('PasswordApplication2.py')
    #import PasswordApplication2
    #os.system('"PasswordApplication2.py"')
    #os.system('D:\PythonProjects\PasswordApplication2.py')
    v = 'D:\PythonProjects\PasswordApplication2.py'
    os.system('"%s' % v )
    #PasswordApplication2()
#to run the password generator program
def run2():
    os.system('"PasswordApplication3.py"')
#to run the username and password pull up system
def run3():
    os.system('"PasswordApplication4.py"')
#our buttons or else gui wouldn't be very usefull
btn = Button(window, text="CLick to add a new entry", bg="black", fg="white",command=run1)
btn.grid(column=0, row=0)
btn2 = Button(window, text="CLick to access the random number generator", bg="black", fg="white",command=run2)
btn2.grid(column=0, row=2)
btn3 = Button(window, text="CLick to pull up entry details", bg="black", fg="white",command=run3)
btn3.grid(column=0, row=3)


window.mainloop()

#tk.mainloop()