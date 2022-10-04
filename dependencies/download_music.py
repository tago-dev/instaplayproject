from dependencies.functions import format_title
from os import system as cmd, makedirs
from pytube import YouTube, extract
from pytube.cli import on_progress
from requests import get
from shutil import rmtree
from music_tag import load_file
from termcolor import cprint, colored


def start():

    music_symbol_tilde = colored('[~]', 'yellow', attrs=['bold'])
    music_text_beside1 = colored('Audio Download Progress: ', 'white', attrs=['bold'])

    music_symbol_minus = colored('[-]', 'yellow', attrs=['bold'])
    music_text_beside2 = colored('Temporary Files Deleted!', 'white', attrs=['bold'])

    music_symbol_plus = colored('[+]', 'yellow', attrs=['bold'])
    music_text_beside3 = colored('The music was downloaded successfully!', 'white', attrs=['bold'])

    cmd('cls')
    print()

    music_text3_examples = colored('Examples: ', 'red', attrs=['bold'])
    music_text4_links = colored('"https://www.youtube.com/watch?v=xXxXxXxXxXx" "https://youtu.be/xXxXxXxXxXx"', 'white', attrs=['bold'])
    music_text2_input = colored('YouTube - Music URL: ', 'red', attrs=['bold'])
    print(music_text3_examples + music_text4_links)
    url = input(music_text2_input)

    yt = YouTube(url, on_progress_callback=on_progress)
    print()

    # Downloading Audio...
    makedirs('Musics', exist_ok=True)
    yt.streams.filter(only_audio=True).first().download(output_path='Musics', filename=format_title(yt.title) + '.mp3')
    cprint(f'{music_symbol_tilde} {music_text_beside1}|', 'white', attrs=['bold'])
    print()

    # Adding cover...
    makedirs('.temp', exist_ok=True)
    yt_fomatted_title = format_title(YouTube(url).title)
    yt_id = extract.video_id(url)
    yt_thumbnail = f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg'
    r = get(yt_thumbnail, allow_redirects=True)
    open(f'.temp\\{yt_fomatted_title}.jpg', 'wb').write(r.content)

    f = load_file(f'Musics\\{yt_fomatted_title}.mp3')
    f['artwork'] = open(f'.temp\\{yt_fomatted_title}.jpg', 'rb').read()
    f.save()

    # Deleting Temporary Files...
    rmtree('.temp', ignore_errors=True)
    print(f'{music_symbol_minus} {music_text_beside2}')
    print()

    print(f'{music_symbol_plus} {music_text_beside3}')
    print()
