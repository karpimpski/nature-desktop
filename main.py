#import libraries
import time
import sys

#import general methods module
import functions

#determine platform
if sys.platform == 'win32' or sys.platform == 'cygwin':
    from platforms.windows import Windows
    platform = Windows()
elif sys.platform == 'linux2':
    from platforms.ubuntu import ubuntu
    platform = Ubuntu()

start_time = time.time()
image_url = functions.get_image_url(platform)

if image_url != 1:
    platform.download_image(image_url)
    platform.set_background()

print("--- %s seconds ---" % (time.time() - start_time))

input("\nPress enter key to exit.")