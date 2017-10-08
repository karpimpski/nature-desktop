#import libraries
import time
import sys

#import general methods module
import functions

#determine platform
if sys.platform == 'win32' or sys.platform == 'cygwin':
    from windows import Windows
    platform = Windows()
elif sys.platform == 'linux' or sys.platform == 'linux2':
    from ubuntu import Ubuntu
    platform = Ubuntu()

image_url = functions.get_image_url(platform)

if image_url != 1:
    platform.download_image(image_url)
    platform.set_background()
    platform.save_background()

input("\nPress enter key to exit.")

sys.exit()