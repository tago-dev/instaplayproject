from dependencies import download_video, download_music
from os import system as cmd

continue_or_exit = None
while continue_or_exit != '1':
    cmd('cls')

    options = {
        1: download_video.start,
        2: download_music.start,
    }

    print()
    print('$ App: Universal YT Downloader')
    print()

    print('1. Video\n'
          '2. Music\n')
    option = int(input('Option: '))
    options[option]()

    continue_or_exit = input('[X] Press 1 to exit or any other key to continue ')
