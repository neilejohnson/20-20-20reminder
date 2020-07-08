#FUNCTIONALITY
#window pops up when you click on the .exe. fairly large to draw attention to itself
#message says to look away for 20 seconds button says 'remind me again in 20 minutes'
#should be fairly simple and loud

#imports
from time import sleep
import tkinter as tk
from tkinter import messagebox

#create main window
root = tk.Tk()
root.title('eye.exe')
#set size of main window
root.geometry("200x100")
#define message within main window
msg = tk.Message(root, text = "Every 20 minutes take a 20 second break. \nFocus your eyes on something at least 20 feet away.")
#configure that font
msg.config(font=('arial', 10))
#add message to window
msg.pack()

root.wm_attributes("-topmost", 1)

def onclose():
    root.wm_state('iconic')
    sleep(4)
    root.wm_state('normal')

B1 = tk.Button(root, text = "Close window", command = onclose)
B1.pack()

#loop it
tk.mainloop()