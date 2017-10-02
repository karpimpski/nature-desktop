import ctypes
import os
path = os.getcwd()
ctypes.windll.user32.SystemParametersInfoW(20, 0, path + '\image.jpg' , 0)