import ctypes
user32 = ctypes.windll.user32
import os

def screen_resolution_ratio():
    """find desktop screen resolution"""
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    ratio = width/height
    return ratio

def set_background():
    """set the desktop background"""
    path = os.getcwd()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + '\image.jpg' , 0)