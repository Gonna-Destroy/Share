import yt_dlp
import tkinter
from tkinter import font, ttk

DIRECTORY = '/home/Gonna_Destroy/Downloads'

root = tkinter.Tk()
root.geometry('500x500')
root.configure(background = '#74579d')
root.title('Share')

custom_font = font.Font(family="Helvetica", size=16, weight="bold")
custom_font_entry = font.Font(family="Helvetica", size=16)
custom_font_exc = font.Font(family="Helvetica", size=16, slant="italic", weight='bold')

label = tkinter.Label(
    root,
    text='Вставьте URL-адресс',
    font= custom_font,
    background='#74579d',
)
label.pack(pady=50)

entry = tkinter.Entry(
    root,
    width=25,
    font=custom_font_entry,
    insertbackground="magenta", 
    insertwidth=10
)
entry.pack()

def main():
    url = entry.get()
    ydl_opts = {'outtmpl': f'{DIRECTORY}/%(title)s.%(ext)s'}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as video:
            video.download([url])
            info_dict = video.extract_info(url, download=False)
            print(info_dict)
    except Exception as e:
        exception = tkinter.Label(
            root,
            background='#74579d',
            text=f'Что-то пошло не так.\nПроверьте:\n - Соеденение с интернетом\n - Верность URL \n - Папку хранения. ',
            font=custom_font_exc,
            anchor='w',
            justify='left'
        )
        exception.place(x=20, y=250)


button = tkinter.Button(
    root,
    text='RUN',
    background='magenta',
    activebackground='red',
    font=custom_font,
    command=main,
    padx=10,
    pady=5
)

button.pack(padx=200, pady=15)


if __name__ == '__main__':
    root.mainloop()
