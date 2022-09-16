from dependencies import download_video, download_music, download_playlist


app_title = '$ App: Universal YT Downloader'

# makedirs('Playlists', exist_ok=True)

options = {
    1: download_video.start,
    2: download_music.start,
    3: download_playlist,
}

print()
print(app_title)
print()

print('1. Video\n'
      '2. Music\n'
      '3. Playlist (Coming Soon)\n')
option = int(input('Number: '))
options[option]()
