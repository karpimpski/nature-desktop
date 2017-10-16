import os

#configuration variables
title = 'Nature Desktop'

#scripts to be run in python shell
def build_windows():
    flags = ['icon=img/icon.ico', 'clean', 'name="Nature Desktop"', 'noconsole']
    command = 'pyinstaller '
    for flag in flags:
        command += '--' + flag + ' '
    command += ' main.py'
    os.system(command)