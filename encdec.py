from tkinter import *
import re, uuid 
from sys import platform
import webbrowser
import os



root = Tk()
root.title('ETHICAL HACKING TOOLKIT')
root.geometry('{}x{}'.format(820,650))

frame_top    = Frame(root, width=800, height=120, bg="#154e72")
title = Label(frame_top,text="ENCRYPTION AND DECRYPTION",fg="red")
title.config(font=("Courier bold", 34))

frame_center  = Frame(root, width=790, height=840, bg="#9dc8e3")
b1=Button(frame_center,  padx=30, pady=30, text="...",cursor="hand2")
b2=Button(frame_center,  padx=30, pady=30, text="...",cursor="hand2")
b3=Button(frame_center,  padx=30, pady=30, text="Encrypt",cursor="hand2")
b4=Button(frame_center,  padx=30, pady=30, text="Decrypt",cursor="hand2")
T1 = Text(frame_center, height=2, width=35)
T2 = Text(frame_center, height=2, width=35)
Entry(frame_center, justify='center')
L1 = Label(frame_center,text="ENCRYPTION   ")
L2 = Label(frame_center,text="DECRYPTION   ")


frame_center.grid_rowconfigure(1,weight=1)
frame_center.grid_columnconfigure(0,weight=1)


frame_bottom = Frame(root, width=800, height=50,  bg="#154e72")

title.pack()
L1.grid(row=0,column=0,sticky="n",padx=10,pady=30)
T1.grid(row=0,column=1,sticky="n",padx=10,pady=30)
b1.grid(row=0,column=2,sticky="n",padx=10,pady=30)

b3.grid(row=1,columnspan=3,sticky="n",padx=10,pady=30)

L2.grid(row=2,column=0,sticky="s",pady=30)
T2.grid(row=2,column=1,sticky="s",pady=30)
b2.grid(row=2,column=2,sticky="s",pady=30)

b4.grid(row=3,columnspan=3,sticky="s",padx=10,pady=30)

#b2.grid(row=1,sticky="e",padx=80, pady=30)
#T.grid(row=1,column=1,sticky="w",padx=80, pady=30)
#L.grid(row=2,columnspan=2,sticky="s",padx=80)
#T1.grid(row=3,columnspan=2,sticky="s",pady=30)
#b3.grid(row=4,columnspan=2,sticky="s",pady=30)


root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(0,weight=1)

frame_top.grid  (row=0,sticky="ew")

frame_center.grid(row=1)
frame_bottom.grid(row=2,sticky="ew")

label_1 = Label(frame_bottom, text="contribute to project",bg="white",fg="blue",cursor="hand2")
label_1.config(font=("Courier bold", 10))
label_1.bind("<Button-1>", lambda event: webbrowser.open("https://github.com/sampathbhargav/toolkit.git"))

frame_top.grid_rowconfigure(1,weight=1)
frame_top.grid_columnconfigure(0,weight=1)

label_1.pack()

root.mainloop()
