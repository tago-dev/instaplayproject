from dependencies.functions import format_title
from os import system as cmd, makedirs
import os
from pytube import YouTube
from pytube.cli import on_progress
import ffmpeg
from shutil import rmtree
import zstd
import requests
import pathlib


def start():
    cmd('cls')
    print()

    resolutions = {
        1: '1080p',
        2: '720p',
        3: '480p',
        4: '360p',
        5: '240p',
        6: '144p'
    }

    print('Resolutions: ' + '   '.join([f'{k}. {v}' for k, v in resolutions.items()]))
    video_quality = int(input('Option: '))
    video_quality = resolutions[video_quality]
    print()

    print('Examples: "https://www.youtube.com/watch?v=xXxXxXxXxXx" "https://youtu.be/xXxXxXxXxXx"')
    url = input('YouTube - Video URL: ')
    yt = YouTube(url, on_progress_callback=on_progress)
    print()

    # Downloading FFMPEG...
    ffmpeg_exe_zst = pathlib.Path(r'dependencies\ffmpeg.exe.zst')
    if not ffmpeg_exe_zst.is_file():
        print('[!] WARNING: The FFMPEG file will be downloaded ONLY the FIRST TIME you run this script! (Like now)')
        print()
        ffmpeg_url = 'https://drive.google.com/uc?export=download&id=16Ob9qv7uwLWqcMOwTOKeC9p52accn-wO'
        r = requests.get(ffmpeg_url, allow_redirects=True)
        open(r'dependencies\ffmpeg.exe.zst', 'wb').write(r.content)
        print()

    # Extracting FFMPEG...
    makedirs('.temp', exist_ok=True)
    with open(r'dependencies\ffmpeg.exe.zst', mode='rb') as fi:
        with open(r'.temp\ffmpeg.exe', mode='wb') as fo:
            fo.write(zstd.ZSTD_uncompress(fi.read()))
    os.environ['PATH'] += os.pathsep + os.path.join(os.getcwd(), '.temp')

    # Downloading Video...
    yt.streams.filter(res=video_quality).first().download(output_path='.temp', filename='temp_video.mp4')
    print('[~] Video Download Progress: ')

    # Downloading Audio...
    yt.streams.filter(only_audio=True).first().download(output_path='.temp', filename='temp_audio.mp3')
    print('[~] Audio Download Progress: ')
    print()

    # Merging Video and Audio...
    makedirs('Videos', exist_ok=True)
    video_title_mp4 = format_title(yt.title) + '.mp4'

    temp_video = '.temp\\temp_video.mp4'
    temp_audio = '.temp\\temp_audio.mp3'
    output = f'Videos\\{video_title_mp4}'

    input_video = ffmpeg.input(temp_video)
    input_audio = ffmpeg.input(temp_audio)
    ffmpeg.output(input_video, input_audio, output, acodec='copy', vcodec='copy').run(quiet=True, overwrite_output=True)
    print('[~] Rendering Progress:      █████████████████████████████████████████| 100.0 %')
    print()

    # Deleting Temporary Files...
    rmtree('.temp', ignore_errors=True)
    print('[-] Temporary Files Deleted!')
    print()

    print('[O] The video was downloaded successfully!')
    print()
