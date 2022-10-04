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
    cprint("  _____           _              _                 ___           _           _", 'red', attrs=['bold'])
    cprint("  \_   \_ __  ___| |_ __ _ _ __ | | __ _ _   _    / _ \_ __ ___ (_) ___  ___| |_", 'red', attrs=['bold'])
    cprint(f"   / /\/ '_ \/ __| __/ _` | '_ \| |/ _` | | | |  / /_)/ '__/ _ \| |/ _ \/ __| __|", 'red', attrs=['bold'])
    cprint(f"/\/ /_ | | | \__ \ || (_| | |_) | | (_| | |_| | / ___/| | | (_) | |  __/ (__| |_", 'red', attrs=['bold'])
    cprint(f"\____/ |_| |_|___/\__\__,_| .__/|_|\__,_|\__, | \/    |_|  \___// |\___|\___|\__|", 'red', attrs=['bold'])
    cprint(f"                          |_|            |___/                |__/", 'red', attrs=['bold'])
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
