from dependencies.functions import format_title
from os import system as cmd, makedirs, environ, pathsep, path, getcwd
from pytube import YouTube
from pytube.cli import on_progress
from ffmpeg import input as ffinput, output as ffoutput
from shutil import rmtree
from zstd import ZSTD_uncompress
from requests import get
from pathlib import Path
from termcolor import cprint, colored


def start():

    video_symbol_more_than = colored('>', 'blue', attrs=['bold'])

    video_symbol_tilde = colored('[~]', 'yellow', attrs=['bold'])
    video_text_beside1 = colored('Video Download Progress: ', 'white', attrs=['bold'])
    video_text_beside2 = colored('Audio Download Progress: ', 'white', attrs=['bold'])
    video_text_beside3 = colored('Rendering Progress:      ', 'white', attrs=['bold'])

    video_symbol_minus = colored('[-]', 'yellow', attrs=['bold'])
    video_text_beside4 = colored('Temporary Files Deleted!', 'white', attrs=['bold'])

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

    resolutions = {
        1: '1080p',
        2: '720p',
        3: '480p',
        4: '360p',
        5: '240p',
        6: '144p'
    }

    video_text5_resolutions = colored('Resolutions: ', 'red', attrs=['bold'])
    video_text6_option = colored('Option: ', 'red', attrs=['bold'])
    video_text7_option = colored(f'{video_symbol_more_than} {video_text6_option}', 'red', attrs=['bold'])
    print(video_text5_resolutions + '   '.join([f'{k}. {v}' for k, v in resolutions.items()]))
    video_quality = int(input(video_text7_option))
    video_quality = resolutions[video_quality]
    print()

    yt = YouTube(url, on_progress_callback=on_progress)

    # Downloading FFMPEG...
    ffmpeg_exe_zst = Path(r'dependencies\ffmpeg.exe.zst')
    if not ffmpeg_exe_zst.is_file():
        cprint('[!] WARNING: The FFMPEG file will be downloaded ONLY the FIRST TIME you run this script! (Like now, please wait...)', 'red', attrs=['bold'])
        ffmpeg_url = 'https://drive.google.com/uc?export=download&id=16Ob9qv7uwLWqcMOwTOKeC9p52accn-wO'
        r = get(ffmpeg_url, allow_redirects=True)
        open(r'dependencies\ffmpeg.exe.zst', 'wb').write(r.content)
        print()

    # Extracting FFMPEG...
    makedirs('.temp', exist_ok=True)
    with open(r'dependencies\ffmpeg.exe.zst', mode='rb') as fi:
        with open(r'.temp\ffmpeg.exe', mode='wb') as fo:
            fo.write(ZSTD_uncompress(fi.read()))
    environ['PATH'] += pathsep + path.join(getcwd(), '.temp')

    # Downloading Video...
    yt.streams.filter(res=video_quality).first().download(output_path='.temp', filename='temp_video.mp4')
    print(f'{video_symbol_tilde} {video_text_beside1}|')

    # Downloading Audio...
    yt.streams.filter(only_audio=True).first().download(output_path='.temp', filename='temp_audio.mp3')
    print(f'{video_symbol_tilde} {video_text_beside2}|')
    print()

    # Merging Video and Audio...
    makedirs('Videos', exist_ok=True)
    video_title_mp4 = format_title(yt.title) + '.mp4'

    temp_video = '.temp\\temp_video.mp4'
    temp_audio = '.temp\\temp_audio.mp3'
    output = f'Videos\\{video_title_mp4}'

    input_video = ffinput(temp_video)
    input_audio = ffinput(temp_audio)
    ffoutput(input_video, input_audio, output, acodec='copy', vcodec='copy').run(quiet=True, overwrite_output=True)
    print(f'{video_symbol_tilde} {video_text_beside3}|████████████████████████████████████████| 100.0 %')
    print()

    # Deleting Temporary Files...
    rmtree('.temp', ignore_errors=True)
    print(f'{video_symbol_minus} {video_text_beside4}')
    print()

    print(f'{video_symbol_plus} {video_text_beside5}')
    print()
