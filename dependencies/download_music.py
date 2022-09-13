from os import system as cmd, makedirs
from pytube import YouTube


def start():
    cmd('cls')
    print()
    print('Examples: "https://www.youtube.com/watch?v=xXxXxXxXxXx" "https://youtu.be/xXxXxXxXxXx"')
    url = input('YouTube - Music URL: ')
    yt = YouTube(url)
    print()

    print('Downloading Audio...')
    yt.streams.filter(only_audio=True).first().download(output_path='Downloaded Musics', filename='temp_audio.mp3')
    print('Download Complete!')
    print()

    print('Renaming the file...')
    video_title_mp3 = yt.title + '.mp3'
    for ch in '<>:"/\\|?*':
        video_title_mp3 = video_title_mp3.replace(ch, '')

    cmd(f'ren "Downloaded Musics\\temp_audio.mp3" "{video_title_mp3}" >nul 2>&1')
    print('Rename Complete!')
    print()

    print('The music was downloaded successfully!')
    print()

    exit = input('Press Enter to exit...')
