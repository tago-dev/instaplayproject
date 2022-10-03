from dependencies.functions import format_title
from os import system as cmd, makedirs
from pytube import YouTube, extract
from pytube.cli import on_progress
import requests
from shutil import rmtree
import music_tag


def start():
    cmd('cls')
    print()
    print('Examples: "https://www.youtube.com/watch?v=xXxXxXxXxXx" "https://youtu.be/xXxXxXxXxXx"')
    url = input('YouTube - Music URL: ')
    yt = YouTube(url, on_progress_callback=on_progress)
    print()

    # Downloading Audio...
    makedirs('Musics', exist_ok=True)
    yt.streams.filter(only_audio=True).first().download(output_path='Musics', filename=format_title(yt.title) + '.mp3')
    print('[~] Audio Download Progress: |')
    print()

    # Adding cover...
    makedirs('.temp', exist_ok=True)
    yt_fomatted_title = format_title(YouTube(url).title)
    yt_id = extract.video_id(url)
    yt_thumbnail = f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg'
    r = requests.get(yt_thumbnail, allow_redirects=True)
    open(f'.temp\\{yt_fomatted_title}.jpg', 'wb').write(r.content)

    f = music_tag.load_file(f'Musics\\{yt_fomatted_title}.mp3')
    f['artwork'] = open(f'.temp\\{yt_fomatted_title}.jpg', 'rb').read()
    f.save()

    # Deleting Temporary Files...
    rmtree('.temp', ignore_errors=True)
    print('[-] Temporary Files Deleted!')
    print()

    print('[O] The music was downloaded successfully!')
    print()

    # https://youtu.be/5z_SPHwspo8
