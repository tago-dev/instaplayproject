from dependencies.functions import format_title
from os import system as cmd, makedirs, environ
from pytube import YouTube, extract
from pytube.cli import on_progress
from ffmpeg import input as ffinput, output as ffoutput
from termcolor import cprint, colored
from shutil import rmtree
from datetime import datetime
from codecs import open


def start():

    video_symbol_more_than = colored('>', 'blue', attrs=['bold'])

    video_symbol_tilde = colored('[~]', 'yellow', attrs=['bold'])
    video_text_beside1 = colored('Video Download Progress: ', 'white', attrs=['bold'])
    video_text_beside2 = colored('Audio Download Progress: ', 'white', attrs=['bold'])
    video_text_beside3 = colored('Quick rendering in progress...', 'white', attrs=['bold'])
    video_text_beside4 = colored('Quick rendering finished!', 'white', attrs=['bold'])

    video_symbol_plus = colored('[+]', 'yellow', attrs=['bold'])
    video_text_beside5 = colored('The music was downloaded successfully!', 'white', attrs=['bold'])

    cmd('cls')

    print()
    cprint("     _ _   _       _                     _ _               _                           _", 'yellow', attrs=['bold'])
    cprint(" ___|_| |_| |_ _ _| |_   ___ ___ _____  / | |_ ___ ___ ___|_|___ _ _ ___ ___ ___ ___ _| |___ ___", 'yellow', attrs=['bold'])
    cprint("| . | |  _|   | | | . |_|  _| . |     |/ /|   | -_|   |  _| | . | | | -_|___|  _| . | . | -_|  _|", 'yellow', attrs=['bold'])
    cprint("|_  |_|_| |_|_|___|___|_|___|___|_|_|_|_/ |_|_|___|_|_|_| |_|_  |___|___|   |___|___|___|___|_|", 'yellow', attrs=['bold'])
    cprint("|___|                                                         |_|", 'yellow', attrs=['bold'])
    print()
    print()

    video_text3_examples = colored('Examples: ', 'red', attrs=['bold'])
    video_text4_links = colored('"https://www.youtube.com/watch?v=xXxXxXxXxXx" "https://youtu.be/xXxXxXxXxXx"', 'white', attrs=['bold'])
    video_text2_input = colored('YouTube - Video URL: ', 'red', attrs=['bold'])
    cprint(video_text3_examples + video_text4_links, 'white', attrs=['bold'])
    url = input(video_text2_input)
    print()

    # Checking available video resolutions
    yt = YouTube(url)
    available_resolutions = list(set(stream.resolution for stream in yt.streams if stream.resolution is not None))
    available_resolutions.sort(key=lambda x: int(x[:-1]), reverse=True)
    available_resolutions = {k: v for k, v in enumerate(available_resolutions, start=1)}

    video_text5_resolutions = colored('Resolutions: ', 'red', attrs=['bold'])
    video_text6_option = colored('Option: ', 'red', attrs=['bold'])
    video_text7_option = colored(f'{video_symbol_more_than} {video_text6_option}', 'red', attrs=['bold'])
    print(video_text5_resolutions + '   '.join([f'{k}. {v}' for k, v in available_resolutions.items()]))
    video_quality = int(input(video_text7_option))
    video_quality = available_resolutions[video_quality]
    print()

    yt = YouTube(url, on_progress_callback=on_progress)

    userprofile_name = environ['userprofile']

    # Formatting the title...
    video_title_mp4 = format_title(yt.title) + '.mp4'
    video_title_mp3 = format_title(yt.title) + '.mp3'

    # Downloading Video...
    yt.streams.filter(res=video_quality).first().download(output_path=fr'{userprofile_name}\AppData\Local\Instaplay Project\temp', filename=video_title_mp4)
    print(f'{video_symbol_tilde} {video_text_beside1}|')

    # Downloading Audio...
    yt.streams.filter(only_audio=True).first().download(output_path=fr'{userprofile_name}\AppData\Local\Instaplay Project\temp', filename=video_title_mp3)
    print(f'{video_symbol_tilde} {video_text_beside2}|')
    print()

    # Merging Video and Audio...
    makedirs('Videos', exist_ok=True)
    temp_video = fr'{userprofile_name}\AppData\Local\Instaplay Project\temp\{video_title_mp4}'
    temp_audio = fr'{userprofile_name}\AppData\Local\Instaplay Project\temp\{video_title_mp3}'
    output = fr'Videos\{video_title_mp4}'

    input_video = ffinput(temp_video)
    input_audio = ffinput(temp_audio)
    print(f'{video_symbol_tilde} {video_text_beside3}')
    ffoutput(input_video, input_audio, output, acodec='copy', vcodec='copy').run(quiet=True, overwrite_output=True)
    print(f'{video_symbol_tilde} {video_text_beside4}')
    print()

    # Generating download log in MD format...
    makedirs(fr'{userprofile_name}\AppData\Local\Instaplay Project\logs\.md', exist_ok=True)
    with open(fr'{userprofile_name}\AppData\Local\Instaplay Project\logs\.md\{format_title(yt.title)}.md', 'w', 'utf-8') as f:
        m, s = divmod(yt.length, 60)
        h, m = divmod(m, 60)

        f.write(f'# **Video: {format_title(yt.title)}**\n\n')
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
        f.write(f'* **Resolution:** {video_quality}\n')
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

        f.write(f'Video: {format_title(yt.title)}\n\n')
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
        f.write(f'Resolution: {video_quality}\n')
        f.write(f'Duration: {h:d}h, {m}m and {s}s\n')
        f.write(f'Description: \n\n{yt.description}\n\n')
        f.write(f"Coder's GitHub: https://github.com/Henrique-Coder\n")
        f.write(f"Project's Repository: https://github.com/Henrique-Coder/instaplayproject\n")
        f.close()

    # Deleting Temporary Files...
    rmtree(fr'{userprofile_name}\AppData\Local\Instaplay Project\temp', ignore_errors=True)

    print(f'{video_symbol_plus} {video_text_beside5}')
    print()
