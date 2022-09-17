from dependencies.functions import format_title
from os import system as cmd, makedirs
import os
from pytube import YouTube
from pytube.cli import on_progress


def start():
    cmd('cls')
    print()
    print('Examples: "https://www.youtube.com/watch?v=xXxXxXxXxXx" "https://youtu.be/xXxXxXxXxXx"')
    url = input('YouTube - Music URL: ')
    yt = YouTube(url, on_progress_callback=on_progress)
    print()

    # Downloading Audio...
    makedirs('Musics', exist_ok=True)
    yt.streams.filter(only_audio=True).first().download(output_path='Musics', filename='temp_audio.mp3')
    print('[~] Audio Download Progress: ')
    print()

    # Renaming the file...
    video_title_mp3 = format_title(yt.title) + '.mp3'
    os.rename('Musics\\temp_audio.mp3', f'Musics\\{video_title_mp3}')

    print('[O] The music was downloaded successfully!')
    print()
