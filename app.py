from os import makedirs
from dependencies import download_video, download_music, download_playlist, video_channel_info


app_title = '$ App: Universal YT Downloader'

makedirs('Downloaded Videos', exist_ok=True)
makedirs('Downloaded Musics', exist_ok=True)
makedirs('Downloaded Playlists', exist_ok=True)
makedirs('Video & Channel Info', exist_ok=True)

options = {
    1: download_video.start,
    2: download_music.start,
    3: download_playlist,
    4: video_channel_info,
}

print()
print(app_title)
print()

print('1. Video\n'
      '2. Music\n'
      '3. Playlist (Coming Soon)\n'
      '4. Video/Channel Info (Coming Soon)\n')
option = int(input('Number: '))
options[option]()
