from os import system as cmd


filename = 'instaplayproject.py'
name = 'InstaplayProject'
working_os = 'win'
version = '1.3.2'
icon = 'images/instaplayproject-appicon.ico'
data = 'dependencies/*;.'

cmd(f'pyinstaller --onefile --icon={icon} --add-data={data} --name={name}-{working_os}-v{version} {filename}')

### Premade by @Henrique-Coder (https://github.com/Henrique-Coder) ###
