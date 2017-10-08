#import libraries
import sys
import easygui

#import general methods module
import functions

#set variables
title = 'Nature Desktop'

#determine platform
if sys.platform == 'win32' or sys.platform == 'cygwin':
    from windows import Windows
    platform = Windows()
elif sys.platform == 'linux' or sys.platform == 'linux2':
    from ubuntu import Ubuntu
    platform = Ubuntu()

#run application
message = 'This application will change your desktop\'s background. Continue?'
save_message = 'Would you like to save the image?'

if easygui.ynbox(message, title, ('Yes', 'No')):
    image_url = functions.get_image_url(platform)

    if image_url != 1:
        platform.download_image(image_url)
        platform.set_background()
        if easygui.ynbox(save_message, title, ('Yes','No')):
            platform.save_background()

sys.exit()