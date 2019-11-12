from tkinter import *
import re, uuid 
from sys import platform
import webbrowser
import os

def currentmac():
    # Python 3 code to print MAC 
    # in formatted way and easier 
    # to understand 
    # joins elements of getnode() after each 2 digits. 
    # using regex expression
    if platform == "linux" or platform == "linux2":
        # linux
        sys_net='/sys/class/net'
        for dev in os.listdir(sys_net):
            with open(os.path.join(os.path.join(sys_net, dev), 'address')) as f:
                return dev, f.read(),
    elif platform == "win32":
        # Windows...
        return (':'.join(re.findall('..', '%012x' % uuid.getnode())))


root = Tk()
root.title('ETHICAL HACKING TOOLKIT')
root.geometry('{}x{}'.format(820,650))

frame_top    = Frame(root, width=800, height=120, bg="#154e72")
title = Label(frame_top,text="MAC CHANGER",fg="red")
title.config(font=("Courier bold", 34))

frame_center  = Frame(root, width=790, height=840, bg="#9dc8e3")
b1=Button(frame_center, height=1, width=30, padx=10, pady=10, text="CHANGE MAC RANDOMLY",cursor="hand2")
b2=Button(frame_center, height=2, width=50, padx=10, pady=10, text="CHANGE TO SPECIFIED MAC ADDRESS",cursor="hand2")
T = Text(frame_center, height=2, width=35)
T1 = Text(frame_center, height=2, width=35)
Entry(frame_center, justify='center')
L = Label(frame_center,text="CURRENT MAC ADDRESS",fg="red")
cm=currentmac()
T1.insert(END,cm)
b3=Button(frame_center, height=1, width=30, padx=10, pady=10, text="RESET MAC TO ORIGINAL",cursor="hand2")

frame_center.grid_rowconfigure(1,weight=1)
frame_center.grid_columnconfigure(0,weight=1)


frame_bottom = Frame(root, width=800, height=50,  bg="#154e72")

title.pack()
b1.grid(row=0,columnspan=2,sticky="n",pady=30)
b2.grid(row=1,sticky="e",padx=80, pady=30)
T.grid(row=1,column=1,sticky="w",padx=80, pady=30)
L.grid(row=2,columnspan=2,sticky="s",padx=80)
T1.grid(row=3,columnspan=2,sticky="s",pady=30)
b3.grid(row=4,columnspan=2,sticky="s",pady=30)


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
