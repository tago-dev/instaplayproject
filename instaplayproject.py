from dependencies import download_video, download_music, download_playlist
from os import system as cmd, makedirs, environ, path, pathsep, getcwd, remove
from termcolor import cprint, colored
from pathlib import Path
from zstd import ZSTD_uncompress
from requests import get

continue_or_exit = None
while continue_or_exit != '1':
    cmd('cls')

    # Downloading FFMPEG...
    print()
    userprofile_name = environ['userprofile']
    makedirs(fr'{userprofile_name}\AppData\Local\Instaplay Project\dependencies', exist_ok=True)
    ffmpeg_exe = Path(fr'{userprofile_name}\AppData\Local\Instaplay Project\dependencies\ffmpeg.exe')

    if not ffmpeg_exe.is_file():
        cprint('[!] WARNING: The FFMPEG file will be downloaded ONLY the FIRST TIME you run this script! (Like now, please wait...)','red', attrs=['bold'])
        ffmpeg_url = 'https://drive.google.com/uc?export=download&id=16Ob9qv7uwLWqcMOwTOKeC9p52accn-wO'
        r = get(ffmpeg_url, allow_redirects=True)
        open(fr'{userprofile_name}\AppData\Local\Instaplay Project\dependencies\ffmpeg.exe.zst', 'wb').write(r.content)

        # Extracting FFMPEG...
        with open(fr'{userprofile_name}\AppData\Local\Instaplay Project\dependencies\ffmpeg.exe.zst', mode='rb') as fi:
            with open(fr'{userprofile_name}\AppData\Local\Instaplay Project\dependencies\ffmpeg.exe', mode='wb') as fo:
                fo.write(ZSTD_uncompress(fi.read()))
        remove(fr'{userprofile_name}\AppData\Local\Instaplay Project\dependencies\ffmpeg.exe.zst')
    environ['PATH'] += pathsep + path.join(getcwd(), fr'{userprofile_name}\AppData\Local\Instaplay Project\dependencies')
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
