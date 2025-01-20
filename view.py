import tkinter as tk
import patterns as pt
import importlib
from main import start_program

root = pt.root('Share', 600, 700)

head = pt.head(root)
head.pack(fill='x')

youtube = pt.label(head, 'YouTube',bg='#be200b', scale=30)
youtube.pack(pady=25)


space = pt.head(
    root,
    bg='gray',
    height=60
)
space.pack()


enter_path = pt.label(
    root,
    f='Courier',
    scale=25,
    text='Enter the path',
    bg='gray'
)
enter_path.pack()

url_enter = pt.entry(
    root,
    height=22,
)
url_enter.pack()

result = pt.label(
    root,
    fg='#be200b',
    scale=20,
)

start = pt.button(
    root,
    text='GO',
    bg='#3ec1a9',
    scale=27,
    command='start_program',
    path_to_func='main',
    params=[root, result]
)

submit = pt.button(
    root,
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


root.mainloop()
