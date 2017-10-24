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

root = Tk()
app = first_window.Application(root, functions, platform, master=root)
app.mainloop()

#put this in a function because putting block in if statement led to error
def draw_second():
    root = Tk()
    app = second_window.Application(root, platform, master=root)
    app.mainloop()

if(app.successful):
    draw_second()