import tkinter
import yt_dlp as yt
import pickle
from threading import Thread


def get_directory():
    with open('cache.pkl', 'rb') as cache:
        info = pickle.load(cache)
        path = info.get('path')
        return path

def add_newline_every_10_chars(text):
    result = ""
    for i in range(0, len(text), 15):
        result += text[i:i+15] + "\n"
    return result

def receive_meta(video, url, label):
    try:
        info_dict = video.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        video_ext = info_dict.get('ext', None)
        video_uploader = info_dict.get('uploader', None)
        video_duration = info_dict.get('duration', None)
        video_view_count = info_dict.get('view_count', None)
        video_like_count = info_dict.get('like_count', None)
        video_dislike_count = info_dict.get('dislike_count', None)

        if len(video_title) > 10:
            title = video_title[:10]
            info = f'Title: {title}...\nDuration: {video_duration}\nLikes: {video_like_count}\nDislike:{video_dislike_count}\nViews: {video_view_count}'
        else:
            info = f'Title: {video_title}\nDuration: {video_duration}\nLikes: {video_like_count}\nDislike:{video_dislike_count}\nViews: {video_view_count}'

        label.configure(text=f'{info}')
        label.pack(pady=30)
        return info
    except Exception as E:
        strE = str(E)
        e = add_newline_every_10_chars(strE)
        label.configure(text=f'{e}\n\nERROR...')
        label.pack(pady=30)


def main(entry: tkinter.Entry, label: tkinter.Label, button: tkinter.Button):
    url = entry.get()

    directory = get_directory()

    opt = {
        'format': 'mp4',
        'outtmpl': f'{directory}/%(title)s.%(ext)s',
        'ignoreerrors': True
    }

    with yt.YoutubeDL(opt) as video:

        thread = Thread(target=video.download, args=([url]))
        thread.start()

        info = receive_meta(video, url, label)

        if 'Title' in info:
            thread.join()
            label.configure(text=f'{info}\n\nWATCH A VIDEO!')

        label.update()








