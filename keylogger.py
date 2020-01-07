
""" KEYLOGGER """
import time
import tkinter
from tkinter import Tk, Entry
import logging
import pynput.keyboard
import keyboard
from pynput import keyboard
import os
import sys
from time import mktime
from datetime import datetime

#Log array of Strings typed and times
Log = []
master = tkinter.Tk()
frame = tkinter.Frame(master,height=1000, width=1000)

""" Log File """

log_dir=""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(messages)s:')

""" Window """
#USERNAME LABEL AND INPUT BOX
tkinter.Label(master, text = "Input Text").grid(row = 0) # this is placed in 0 0
username = tkinter.Entry(master)
username.grid(row = 1)

""" Functions """
def char(event):
    start = time.time()
    key = event.char
    end = time.time()
    final_time = (end-start)*1000000000
    final_time = round(final_time, 6)
    Log.append(key)
    Log.append(final_time)
    
def get_input():
    user_start = time.time()
    username_input=username.get()
    user_end = time.time()
    user_time = (user_end-user_start)*1000000000
    user_time = round(user_time, 6)
    Log.append(username_input)
    Log.append(len(username_input))
    Log.append(user_time)
    print(Log)

logging.info(str(Log))
""" Button """
#BUTTON
button = tkinter.Button(master, text="Login", command=get_input)
button.grid(row = 4)

""" Bindings """
username.bind("<Key>", char)
#password.bind("<Key>", char)

#HELD TIME
#INTER-KEY

""" Activate """
master.mainloop()
