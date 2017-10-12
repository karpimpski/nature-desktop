#import libraries
import sys
import tkinter
from tkinter import messagebox

import config
import functions

#determine platform
if sys.platform == 'win32' or sys.platform == 'cygwin':
    from windows import Windows
    platform = Windows()
elif sys.platform == 'linux' or sys.platform == 'linux2':
    from ubuntu import Ubuntu
    platform = Ubuntu()

#start and close tkinter root window
root = tkinter.Tk()
root.withdraw()

#save prompts
confirm_message = 'This application will change your desktop\'s background. Continue?'
save_message = 'The background has been set. Would you like to save the image?'

#warn user and confirm
if messagebox.askyesno(config.title, confirm_message):
    #retrieve image url
    image_url = functions.get_image_url(platform)

    #test that a url was retrieved
    if image_url != 1:
        #download and set the background image
        platform.download_image(image_url)
        platform.set_background()
        
        #ask user if they would like to save image to disk
        if messagebox.askyesno(config.title, save_message):
            platform.save_background()

sys.exit()