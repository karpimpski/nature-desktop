#import libraries
import time

#import general methods module
import functions

#import platform modules
from platforms.windows import Windows

#determine platform
platform = Windows()

start_time = time.time()
image_url = functions.get_image_url(platform)

if image_url != 1:
    platform.download_image(image_url)
    platform.set_background()

print("--- %s seconds ---" % (time.time() - start_time))

input("\nPress enter key to exit.")