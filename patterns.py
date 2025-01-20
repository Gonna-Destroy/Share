import tkinter as tk
from tkinter import font
import importlib


def root(title: str, width: int, height: int):
    root = tk.Tk()
    root.title(title)
    root.geometry(f'{width}x{height}')
    root.resizable(width=False, height=False)
    root.configure(background='gray')
    return root

def head(root: tk.Tk, bg: str = '#be200b', height: int = 60):
    head = tk.Frame(
        root,
        bg=bg,
        height=height
    )
    return head

def label(root, text: str = '', f: str = 'Helvetica', scale: int = 16, bg: str = 'gray', fg: str = 'black'):
    custom_label = font.Font(family=f, size=scale, weight="bold")
    label = tk.Label(
        root,
        text=text,
        font=custom_label,
        background=bg,
        fg=fg
    )
    return label

def entry(root, width: int = 25, height: int = 16):
    custom_label = font.Font(family='Helvetica', size=height)
    entry = tk.Entry(
        root,
        font=custom_label,
        width=width,
    )
    return entry


def button(root, params: [] = None, text: str = 'SUBMIT', command: str = None, path_to_func: str = None, bg: str = '#50a6d5', scale: int = 16, f: str = 'Helvetica'):
    custom_label = font.Font(family=f, size=scale, weight="bold")
    button = tk.Button(
        root,
        text=text,
        font=custom_label,
        bg=bg,
        activebackground='#718ad3',
        anchor='s',
    )
    try:
        module = importlib.import_module(path_to_func)
        method = getattr(module, command)
        if params is not None:
            button.configure(command=lambda: method(*params, button))
        else:
            button.configure(command=method)
    except Exception as e:
        pass
    return button

