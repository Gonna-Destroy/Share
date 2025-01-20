import time
import tkinter
from yt_dlp import YoutubeDL
import importlib
import pickle
from tkinter import Entry
import re
import os
from tkinter import font

file_cache = 'cache.pkl'
DIRECTORY = ''

def messageGreen(message: tkinter.Label, text: str = 'Succes!\nThis path saved in the cache.'):
    message.configure(fg='#00e50b')
    message.configure(text=text)
    message.pack(pady=50)

def messageRed(message: tkinter.Label, text: str = 'Error!\n This path is invalid!\n'):
    message.configure(fg='#be200b')
    message.configure(text=text)
    message.pack(pady=50)

def is_valid_path(path, message: tkinter.Label):
    pattern = r'^(/[^/ ]+)+/?$'
    match = re.match(pattern, path)
    if match is None:
        messageRed(message)
        return False
    else:
        if os.path.isdir(path):
            return True
        else:
            messageRed(message, text='This path was not found.\nEnter another path!')
            return False

def create_cache(message: tkinter.Label):
    cache = {'path': f'{DIRECTORY}'}

    if is_valid_path(DIRECTORY, message):
        try:
            with open(file_cache, 'wb') as file:
                pickle.dump(cache, file)
            messageGreen(message)
            return True
        except Exception as e:
            messageRed(message, text='Path is robust.\nBut not stored in cache :(')
            return False
    else: return False

def get_directory(entry: Entry,  message: tkinter.Label, start: tkinter.Button, button: tkinter.Button):
    global DIRECTORY
    DIRECTORY = entry.get()
    if create_cache(message):
        start.place(x=253, y=550)

def start_program(root: tkinter.Tk, message: tkinter.Label, button: tkinter.Button):
    button.destroy()
    with open(file_cache, 'rb') as file:
        path = pickle.load(file)
        data = path.get('path')
        if os.path.isdir(data):
            message.configure(text=f'Your path: {data}\nWelcome!')
            message.update()
            timer = tkinter.Label(
                root,
            )
            messageGreen(timer, text='3')
            custom_font = font.Font(family='Helvetica', size=22, weight='bold')
            timer.configure(font=custom_font, bg='gray', fg='magenta')
            timer.place(x=286, y=470)
            for i in range(3,0,-1):
                timer.configure(text=f'{i}')
                timer.update()
                time.sleep(1)
        else: messageRed(message, text='Path incorrect!')
















