import os
import curses
stdscr = curses.initscr()

def screen_resolution_ratio():
    """find desktop screen resolution"""
    height,width = stdscr.getmaxyx()
    return width/height

def set_background():
    """set the desktop background"""
    file_path = os.path.expanduser('~/.image.jpg')
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + file_path)