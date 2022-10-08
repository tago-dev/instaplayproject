from dependencies.functions import format_title
from os import system as cmd, makedirs, environ, pathsep, getcwd, path
from pytube import YouTube, extract
from pytube.cli import on_progress
from requests import get
from shutil import rmtree
from music_tag import load_file
from termcolor import cprint, colored
from datetime import datetime
from codecs import open


def start():

    music_symbol_tilde = colored('[~]', 'yellow', attrs=['bold'])
    music_text_beside1 = colored('Audio Download Progress: ', 'white', attrs=['bold'])
    music_text_beside4 = colored('Quick rendering in progress...', 'white', attrs=['bold'])
    music_text_beside5 = colored('Quick rendering finished!', 'white', attrs=['bold'])

    music_symbol_plus = colored('[+]', 'yellow', attrs=['bold'])
    music_text_beside3 = colored('The music was downloaded successfully!', 'white', attrs=['bold'])

    cmd('cls')

    print()
    cprint("     _ _   _       _                     _ _               _                           _", 'yellow', attrs=['bold'])
    cprint(" ___|_| |_| |_ _ _| |_   ___ ___ _____  / | |_ ___ ___ ___|_|___ _ _ ___ ___ ___ ___ _| |___ ___", 'yellow', attrs=['bold'])
    cprint("| . | |  _|   | | | . |_|  _| . |     |/ /|   | -_|   |  _| | . | | | -_|___|  _| . | . | -_|  _|", 'yellow', attrs=['bold'])
    cprint("|_  |_|_| |_|_|___|___|_|___|___|_|_|_|_/ |_|_|___|_|_|_| |_|_  |___|___|   |___|___|___|___|_|", 'yellow', attrs=['bold'])
    cprint("|___|                                                         |_|", 'yellow', attrs=['bold'])
    print()
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
    userprofile_name = environ['userprofile']
    yt.streams.filter(only_audio=True).first().download(output_path=fr'{userprofile_name}\AppData\Local\Instaplay Project\temp', filename=format_title(yt.title) + '.mp3')
    cprint(f'{music_symbol_tilde} {music_text_beside1}|', 'white', attrs=['bold'])
    print()

    # Convert to MP3
    userprofile_name = environ['userprofile']
    environ['PATH'] += pathsep + path.join(getcwd(), fr'{userprofile_name}\AppData\Local\Instaplay Project\dependencies')
    cmd_formatted_title = format_title(yt.title) + '.mp3'
    print(f'{music_symbol_tilde} {music_text_beside4}')
    cmd(fr'ffmpeg -i "%userprofile%\AppData\Local\Instaplay Project\temp\{cmd_formatted_title}" -b:a 128K -vn "Musics\{cmd_formatted_title}" -y -loglevel quiet')
    print(f'{music_symbol_tilde} {music_text_beside5}')
    print()

    # Adding metadata...
    userprofile_name = environ['userprofile']
    yt_formatted_title = format_title(YouTube(url).title)
    makedirs(fr'{userprofile_name}\AppData\Local\Instaplay Project\temp', exist_ok=True)
    yt_id = extract.video_id(url)
    r = get(f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg', allow_redirects=True)
    open(fr'{userprofile_name}\AppData\Local\Instaplay Project\temp\{yt_formatted_title}.jpg', 'wb').write(r.content)
    publish_year = str(yt.publish_date).split('-')[0]

    f = load_file(fr'Musics\{yt_formatted_title}.mp3')
    f['artwork'] = open(fr'{userprofile_name}\AppData\Local\Instaplay Project\temp\{yt_formatted_title}.jpg', 'rb').read()
    f['tracktitle'] = yt_formatted_title
    f['artist'] = yt.author
    f['year'] = publish_year
    f['albumartist'] = yt.author
    f['genre'] = 'Music'
    f.save()

    # Generating download log in MD format...
    makedirs(fr'{userprofile_name}\AppData\Local\Instaplay Project\logs\.md', exist_ok=True)
    with open(fr'{userprofile_name}\AppData\Local\Instaplay Project\logs\.md\{format_title(yt.title)}.md', 'w', 'utf-8') as f:
        m, s = divmod(yt.length, 60)
        h, m = divmod(m, 60)

        f.write(f'# **Music: {format_title(yt.title)}**\n\n')
        f.write(f'![Video Thumbnail](https://img.youtube.com/vi/{extract.video_id(url)}/maxresdefault.jpg)\n\n')
        f.write(f'### **General Info**\n')
        f.write(f'* **Date:** {datetime.now().strftime("%Y/%m/%d")} (YYY/MM/DD)\n')
        f.write(f'* **Time:** {datetime.now().strftime("%H:%M:%S")} (H/M/S)\n\n')
        f.write(f'### **YouTube Info**\n')
        f.write(f'* **Subtitles:** {yt.captions}\n')
        f.write(f'* **Age Restriction:** {yt.age_restricted}\n')
        f.write(f'* **Rating:** {yt.rating}\n\n')
        f.write(f'### **Video Info**\n')
        f.write(f'* **URL:** {url}\n')
        f.write(f'* **Thumbnail URL:** https://img.youtube.com/vi/{extract.video_id(url)}/maxresdefault.jpg\n')
        f.write(f'* **Publish Date:** {yt.publish_date} (YYY/MM/DD) (H/M/S)\n'.replace('-', '/'))
        f.write(f'* **Title:** {yt.title}\n')
        f.write(f'* **Channel:** {yt.author}\n')
        f.write(f'* **Views:** {yt.views:,}\n'.replace(',', '.'))
        f.write(f'* **Duration:** {h:d}h, {m}m and {s}s\n')
        f.write(f'* **Description:** \n\n{yt.description}\n\n')
        f.write(f"* ### **Coder's GitHub:** https://github.com/Henrique-Coder\n")
        f.write(f"* ### **Project's Repository:** https://github.com/Henrique-Coder/instaplayproject\n")
        f.close()

    # Generating download log in TXT format...
    makedirs(fr'{userprofile_name}\AppData\Local\Instaplay Project\logs\.txt', exist_ok=True)
    with open(fr'{userprofile_name}\AppData\Local\Instaplay Project\logs\.txt\{format_title(yt.title)}.txt', 'w', 'utf-8') as f:
        m, s = divmod(yt.length, 60)
        h, m = divmod(m, 60)

        f.write(f'Music: {format_title(yt.title)}\n\n')
        f.write(f'General Info\n')
        f.write(f'Date: {datetime.now().strftime("%Y/%m/%d")} (YYY/MM/DD)\n')
        f.write(f'Time: {datetime.now().strftime("%H:%M:%S")} (H/M/S)\n\n')
        f.write(f'YouTube Info\n')
        f.write(f'Subtitles: {yt.captions}\n')
        f.write(f'Age Restriction: {yt.age_restricted}\n')
        f.write(f'Rating: {yt.rating}\n\n')
        f.write(f'Video Info\n')
        f.write(f'URL: {url}\n')
        f.write(f'Thumbnail URL: https://img.youtube.com/vi/{extract.video_id(url)}/maxresdefault.jpg\n')
        f.write(f'Publish Date: {yt.publish_date} (YYY/MM/DD) (H/M/S)\n'.replace('-', '/'))
        f.write(f'Title: {yt.title}\n')
        f.write(f'Channel: {yt.author}\n')
        f.write(f'Views: {yt.views:,}\n'.replace(',', '.'))
        f.write(f'Duration: {h:d}h, {m}m and {s}s\n')
        f.write(f'Description: \n\n{yt.description}\n\n')
        f.write(f"Coder's GitHub: https://github.com/Henrique-Coder\n")
        f.write(f"Project's Repository: https://github.com/Henrique-Coder/instaplayproject\n")
        f.close()

    # Deleting Temporary Files...
    rmtree(fr'{userprofile_name}\AppData\Local\Instaplay Project\temp', ignore_errors=True)

    print(f'{music_symbol_plus} {music_text_beside3}')
    print()
