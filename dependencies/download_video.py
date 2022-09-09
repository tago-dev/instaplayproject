from os import system as cmd, makedirs
from pytube import YouTube
import ffmpeg
from shutil import rmtree


def start():
    cmd('cls && echo.')
    resolutions = {
        1: '1080p',
        2: '720p',
        3: '480p',
        4: '360p',
        5: '240p',
        6: '144p'
    }

    print('Resolutions: ' + '   '.join([f'{k}. {v}' for k, v in resolutions.items()]))
    video_quality = int(input('Number: '))
    video_quality = resolutions[video_quality]

    print()
    print('Examples: "https://www.youtube.com/watch?v=xXxXxXxXxXx" "https://youtu.be/xXxXxXxXxXx"')
    url = input('YouTube Video URL: ')
    yt = YouTube(url)

    print()
    print('Downloading Video...')
    makedirs('.temp', exist_ok=True)
    yt.streams.filter(res=video_quality).first().download(output_path='.temp', filename='temp_video.mp4')
    print('Download Complete!')
    print()

    print('Downloading Audio...')
    yt.streams.filter(only_audio=True).first().download(output_path='.temp', filename='temp_audio.mp3')
    print('Download Complete!')
    print()

    print('Merging Video and Audio without rendering...')
    video_title_mp4 = yt.title + '.mp4'

    for ch in '<>:"/\\|?*':
        video_title_mp4 = video_title_mp4.replace(ch, '')

    temp_video = '.temp\\temp_video.mp4'
    temp_audio = '.temp\\temp_audio.mp3'
    output = f'Downloaded Videos\\{video_title_mp4}'

    input_video = ffmpeg.input(temp_video)
    input_audio = ffmpeg.input(temp_audio)
    ffmpeg.output(input_video, input_audio, output, acodec='copy', vcodec='copy').run(quiet=True)

    print('Merge Complete!')
    print()

    print('Deleting Temporary Files...')
    rmtree('.temp', ignore_errors=True)
    print('Temporary Files Deleted!')
    print()

    print('The video was downloaded successfully!')
