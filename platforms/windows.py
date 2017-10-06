import ctypes
user32 = ctypes.windll.user32
import os
import requests

class Windows():
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
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)
        ratio = width/height
        return ratio

    def set_background(self):
        """set the desktop background"""
        path = os.getcwd() + '\\' + self.image_file_name
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)