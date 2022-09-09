from os import system as os
from pytube import YouTube


app_title = '$ App: Universal YT Downloader'

os('if not exist ".temp" mkdir ".temp" >nul 2>&1')
os('if not exist "Downloaded Videos" mkdir "Downloaded Videos" >nul 2>&1')
os('if not exist "Downloaded Musics" mkdir "Downloaded Musics" >nul 2>&1')
os('if not exist "Downloaded Playlists" mkdir "Downloaded Playlists" >nul 2>&1')

print()
print(app_title)
print()

resolutions = {
    1: '1080p',
    2: '720p',
    3: '480p',
    4: '360p',
    5: '240p',
    6: '144p'
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

temp_video = '.temp\\temp_video.mp4'
temp_audio = '.temp\\temp_audio.mp3'
output = f'"Downloaded Videos/{video_title_mp4}"'
os(f'ffmpeg -i {temp_video} -i {temp_audio} -c copy {output} >nul 2>&1')
os(f'ren "{output}" "{video_title_mp4}" >nul 2>&1')
print('Merge Complete!')
print()

print('Deleting Temporary Files...')
os('del /f /q ".temp\\temp_video.mp4" >nul 2>&1')
os('del /f /q ".temp\\temp_audio.mp3" >nul 2>&1')
print('Temporary Files Deleted!')
print()

print('The video was downloaded successfully!')
