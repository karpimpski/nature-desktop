#import libraries
import sys
from tkinter import *
from tkinter.ttk import *

from modules import config
from modules import functions
from popups import first_window, second_window

#determine platform
if sys.platform == 'win32' or sys.platform == 'cygwin':
    from platforms.windows import Windows
    platform = Windows()
elif sys.platform == 'linux' or sys.platform == 'linux2':
    from platforms.ubuntu import Ubuntu
    platform = Ubuntu()

app = None

def draw_first():
    root = Tk()
    app = first_window.Application(functions, platform, master=root)
    app.mainloop()

    if(app.successful):
        draw_second()

def draw_second():
    root = Tk()
    app = second_window.Application(platform, master=root)
    app.mainloop()

draw_first()

sys.exit()