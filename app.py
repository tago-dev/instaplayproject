from dependencies import download_video, download_music, download_playlist
from os import system as cmd
from termcolor import cprint, colored

continue_or_exit = None
while continue_or_exit != '1':
    cmd('cls')

    options = {
        1: download_video.start,
        2: download_music.start,
        3: download_playlist.start,
    }

    coder_text = colored('Coder:', 'blue')
    coder_github = colored('github.com/henrique-coder', 'blue')

    print()
    cprint(" _____     _                     _    __ __ _____    ____                _           _", 'red')
    cprint("|  |  |___|_|_ _ ___ ___ ___ ___| |  |  |  |_   _|  |    \ ___ _ _ _ ___| |___ ___ _| |___ ___ ", 'red')
    cprint(f"|  |  |   | | | | -_|  _|_ -| .'| |  |_   _| | |    |  |  | . | | | |   | | . | .'| . | -_|  _| {coder_text}", 'red')
    cprint(f"|_____|_|_|_|\_/|___|_| |___|__,|_|    |_|   |_|    |____/|___|_____|_|_|_|___|__,|___|_ {coder_github}", 'red')
    print()
    cprint('$ App: Universal YT Downloader', 'white', attrs=['bold'])
    print()

    print('1. Video')
    print('2. Music')
    print('3. Playlist')
    print()
    option = int(input('Option: '))
    options[option]()

    continue_or_exit = input('[X] Press 1 to exit or any other key to continue ')
