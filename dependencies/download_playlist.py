from dependencies.functions import format_title
from pytube import Playlist
from os import system as cmd
from os import makedirs
from termcolor import colored


def start():

    playlist_symbol_tilde = colored('[~]', 'yellow', attrs=['bold'])
    playlist_text_beside1 = colored('Progress: ', 'white', attrs=['bold'])

    playlist_symbol_plus = colored('[+]', 'yellow', attrs=['bold'])
    playlist_text_beside2 = colored('The playlist was downloaded successfully!', 'white', attrs=['bold'])

    playlist_symbol_line = colored('-', 'white', attrs=['bold'])

    cmd('cls')
    print()

    playlist_text3_examples = colored('Example: ', 'red', attrs=['bold'])
    playlist_text4_links = colored('"https://youtu.be/xXxXxXxX_xX?list=xXxXxXxXxXxXxXxXxXxXxXxXxXxX-xXxXx"', 'white', attrs=['bold'])
    playlist_text2_input = colored('YouTube - Playlist URL: ', 'red', attrs=['bold'])
    print(playlist_text3_examples + playlist_text4_links)
    url = input(playlist_text2_input)
    print()

    playlist = Playlist(url)
    for video in playlist.videos:
        formatted_playlist_title = format_title(playlist.title)
        makedirs('Playlists', exist_ok=True)
        makedirs(f'Playlists\\{formatted_playlist_title}', exist_ok=True)
        playlist_path = f'Playlists\\{formatted_playlist_title}'
        video.streams.filter(only_audio=True).first().download(output_path=playlist_path, filename=format_title(video.title) + '.mp3')
        formatted_video_title = format_title(video.title)
        playlist_formatted_video_title_colored = colored(formatted_video_title, 'white', attrs=['bold'])
        print(f'{playlist_symbol_tilde} {playlist_text_beside1}|████████████████████| 100.0 % {playlist_symbol_line} Music: {playlist_formatted_video_title_colored}')

    print()
    print(f'{playlist_symbol_plus} {playlist_text_beside2}')
    print()
