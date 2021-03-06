import os
import curses
import requests
import readline
import easygui
stdscr = curses.initscr()
from shutil import copyfile

class Ubuntu():
    def __init__(self):
        self.image_file_name = ''
    
    def download_image(self, image_url):
        """download and save image to current directory"""
        self.image_file_name = 'image.' + image_url.split('.')[-1]
        file_path = self.image_file_name
        f = open(file_path,'wb')
        f.write(requests.get(image_url).content)
        f.close()
    
    def screen_resolution_ratio(self):
        """find desktop screen resolution"""
        height,width = stdscr.getmaxyx()
        return width/height

    def set_background(self):
        """set the desktop background"""
        file_path = os.getcwd() + '/' + self.image_file_name
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:" + file_path)
    
    def save_background(self):
        """give user the option to save the image for future use"""
        path = easygui.filesavebox(default=self.image_file_name)
        if(path):
            #add file extension if none is given
            if '.' not in path:
                path += '.' + self.image_file_name.split('.')[-1]
            
            #copy image file to given path
            copyfile(os.getcwd() + '/' + self.image_file_name, path)