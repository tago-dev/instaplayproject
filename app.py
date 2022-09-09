from os import makedirs
from dependencies import download_video
# import download_music
# import download_playlist
# import collect_data


def coming_soon():
    print()
    print('Hahaha')


app_title = '$ App: Universal YT Downloader'

makedirs('Downloaded Videos', exist_ok=True)
makedirs('Downloaded Musics', exist_ok=True)
makedirs('Downloaded Playlists', exist_ok=True)

options = {
    1: download_video.start,
    2: coming_soon,
    3: coming_soon,
    4: coming_soon
}

print()
print(app_title)
print()

print('1. Video\n'
      '2. Music (Coming Soon)\n'
      '3. Playlist (Coming Soon)\n'
      '4. Collect data (Coming Soon)\n')
option = int(input('Number: '))
options[option]()
