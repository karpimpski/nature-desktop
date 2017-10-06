import os
import curses
stdscr = curses.initscr()

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
    
    def screen_resolution_ratio():
        """find desktop screen resolution"""
        height,width = stdscr.getmaxyx()
        return width/height

    def set_background():
        """set the desktop background"""
        file_path = os.path.expanduser('~/.image.jpg')
        os.system("gsettings set org.gnome.desktop.background picture-uri file://" + file_path)