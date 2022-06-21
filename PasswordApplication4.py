# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:32:42 2021

@author: surya
"""
import tkinter as tk
root = tk.Tk()
import sys
#part3
#our lists
newlist = []
#we got ourselves a 3d list here
listall = []
passwords = []
#time to open the file
reopen = open("passwords.txt", "r")
#We will take apart the file and assign them to a list
for x in reopen:
    g = x.split(',')
    z = slice(1)
    zmap = map(str, g[z])
    listz = list(zmap)
    newlist.append(listz)
    z1 = slice(1, 2)
    zmap1 = map(str, g[z1])
    listz1 = list(zmap1)
    z2 = slice(2, 3)
    zmap2 = map(str, g[z2])
    listz2 = list(zmap2)
    #we will append them all to this list here
    listall.append([listz, g[1], g[2]])
#gotta make sure that we can leave
def master():
    raise SystemExit

def get_entry():
    text = e1.get()
    for z in listall:
        for x in z:
            if x[0] == text:
                #print("The username is: ", z[1], "The password is: ", z[2])
                username1 = z[1]
                password1 = z[2]
                e2.insert(0, username1)
                e3.insert(0, password1)
                break
                #raise SystemExit()

#gotta give some instructions
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "Input account name:")
#let's get that entry in
e1 = tk.Entry()
e1.pack()
#ignore these, I tried to make them something else but this was the best i could do in 6 hours
e2 = tk.Entry()
e2.pack()

e3 = tk.Entry()
e3.pack()
#button to submit
b1 = tk.Button(text='Enter', command=get_entry)
b1.pack()
#button to leave
b2 = tk.Button(text='Quit',command=master)
b2.pack()
root.mainloop()
