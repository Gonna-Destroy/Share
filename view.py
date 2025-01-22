import pickle
import tkinter as tk
import patterns as pt
import importlib
from main import start_program
import re
import subprocess



root = pt.root('Share', 600, 700)

head = pt.head(root)
head.pack(fill='x')

body = pt.head(root, bg='gray', height=350)
body.pack(fill='x')

main = pt.head(root, bg='gray', height=350)
main.pack(fill='x')
main.pack_forget()


youtube = pt.label(head, 'YouTube',bg='#be200b', scale=30)
youtube.pack(pady=25)


skip = pt.button(
    body,
    text='   SKIP   ',
    path_to_func='main',
    command='skip',
    params=[body, main]
)

space = pt.head(
    body,
    bg='gray',
    height=60
)
space.pack()


enter_path = pt.label(
    body,
    f='Courier',
    scale=25,
    text='Enter the path',
    bg='gray'
)
enter_path.pack()

url_enter = pt.entry(
    body,
    height=22,
)
url_enter.pack()

result = pt.label(
    body,
    fg='#be200b',
    scale=20,
)

start = pt.button(
    body,
    text='GO',
    bg='#3ec1a9',
    scale=27,
    command='start_program',
    path_to_func='main',
    params=[body, result, main]
)

submit = pt.button(
    body,
    command='get_directory',
    path_to_func='main',
    params=[url_enter, result, start]
)

def disable_submit(event):
    submit.configure(state='disabled')
    submit.update()

start.bind('<Button-3>', disable_submit)
start.bind('<Button-1>', disable_submit)


submit.pack(pady=20)

try:
    with open('cache.pkl', 'rb') as file:
        info = pickle.load(file)
        try:
            path = info.get('path')
            pattern = r'^(/[^/ ]+)+/?$'
            try:
                match = re.match(pattern, path)
                if match is not None:
                    skip.pack()
                    if len(path) > 15:
                        newPath = ''
                        for i in range(0, len(path), 15):
                            newPath += i[i:i+15] + "\n"
                        path = newPath
                    label = pt.label(
                        body,
                        text=f'Current path:\n{path}',
                        bg='gray',
                        scale=14
                    )
                    label.pack(pady=20)
            except Exception:
                pass
        except Exception:
            pass
except Exception:
    pass

def close(event):
    if skip.winfo_exists():
        skip.destroy()
    if label.winfo_exists():
        label.destroy()

submit.bind('<Button-3>', close)
submit.bind('<Button-1>', close)

#create widgets of url enter
space2 = pt.head(
    main,
    bg='gray',
    height=60
)
space2.pack()

label_url = pt.label(
    main,
    f='Courier',
    scale=25,
    text='Enter the URL',
    bg='gray'
)
label_url.pack()

entry_url = pt.entry(
    main,
    height=22,
)
entry_url.pack()


info = pt.label(
    main,
    bg='gray',
    scale=20,
)

download = pt.button(
    main,
    text='DOWNLOAD',
    path_to_func='body',
    command='main',
    params=[entry_url, info]
)
download.pack(pady=15)





root.mainloop()
