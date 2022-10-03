from dependencies.functions import format_title
from pytube import Playlist
from os import system as cmd
from os import makedirs


def start():
    cmd('cls')
    print()
    print('Examples: "https://www.youtube.com/watch?v=xXxXxXxXxXx" "https://youtu.be/xXxXxXxXxXx"')
    url = input('YouTube - Playlist URL: ')
    print()

    playlist = Playlist(url)
    formatted_playlist_title = format_title(playlist.title)
    makedirs('Playlists', exist_ok=True)
    for video in playlist.videos:
        makedirs(f'Playlists\\{formatted_playlist_title}', exist_ok=True)
        plpath = f'Playlists\\{formatted_playlist_title}'
        video.streams.filter(only_audio=True).first().download(output_path=plpath, filename=format_title(video.title) + '.mp3')
        formatted_video_title = format_title(video.title)
        print(f'[~] Progress: |████████████████████| 100.0 % - Music: {formatted_video_title}')

    print()
    print('[O] The playlist was downloaded successfully!')
    print()

    # https://www.youtube.com/watch?v=ZaQpfVHPTXc&list=PLRBp0Fe2GpgkCzeNV9y7ULeApok_z9IqM
