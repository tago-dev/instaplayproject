from os import system as os
from pytube import YouTube


app_title = '$ App: Universal YT Downloader'

print()
print(app_title)
print()

resolutions = {
    1: '2160p',
    2: '1440p',
    3: '1080p',
    4: '720p',
    5: '480p',
    6: '360p',
    7: '240p',
    8: '144p'
}

print('Examples: ' + '   '.join([f'{k}. {v}' for k, v in resolutions.items()]))
video_quality = int(input('Number: '))
video_quality = resolutions[video_quality]

print()
print('Examples: "https://www.youtube.com/watch?v=xXxXxXxXxXx" "https://youtu.be/xXxXxXxXxXx"')
url = input('YouTube Video URL: ')
yt = YouTube(url)

print()
print('Downloading Video...')
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

temp_video = '.temp/temp_video.mp4'
temp_audio = '.temp/temp_audio.mp3'
output = f'"Downloads/{video_title_mp4}"'
os(f'ffmpeg -i {temp_video} -i {temp_audio} -c copy {output} >nul 2>&1')
os(f'ren "{output}" "{video_title_mp4}" >nul 2>&1')
print('Merge Complete!')
print()

print('Deleting Temporary Files...')
os('del /f /q ".temp\\temp_video.mp4" >nul 2>&1 && del /f /q ".temp\\temp_audio.mp3" >nul 2>&1')
print('Temporary Files Deleted!')
print()

print('The video was downloaded successfully!')
