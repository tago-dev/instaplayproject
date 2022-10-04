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

    symbol_more_than = colored('>', 'blue', attrs=['bold'])

    coder_text = colored('Coder:', 'blue')
    coder_github = colored('github.com/henrique-coder', 'blue')
    print()
    cprint(" _____     _                     _    __ __ _____    ____                _           _", 'red', attrs=['bold'])
    cprint("|  |  |___|_|_ _ ___ ___ ___ ___| |  |  |  |_   _|  |    \ ___ _ _ _ ___| |___ ___ _| |___ ___ ", 'red', attrs=['bold'])
    cprint(f"|  |  |   | | | | -_|  _|_ -| .'| |  |_   _| | |    |  |  | . | | | |   | | . | .'| . | -_|  _| {coder_text}", 'red', attrs=['bold'])
    cprint(f"|_____|_|_|_|\_/|___|_| |___|__,|_|    |_|   |_|    |____/|___|_____|_|_|_|___|__,|___|_ {coder_github}", 'red', attrs=['bold'])
    print()
    cprint('$ App: Universal YT Downloader', 'blue', attrs=['bold'])
    print()

    cprint('1. Video', 'white', attrs=['bold'])
    cprint('2. Music', 'white', attrs=['bold'])
    cprint('3. Playlist', 'white', attrs=['bold'])
    print()
    text1_option = colored(f'{symbol_more_than} Option: ', 'white', attrs=['bold'])
    option = int(input(text1_option))
    options[option]()

    text_continue_or_exit = colored('[X] Press 1 to exit or any other key to continue ', 'blue', attrs=['bold'])
    continue_or_exit = input(text_continue_or_exit)
