#import libraries
import ctypes
user32 = ctypes.windll.user32
import os
import requests
import json
import time

def screen_resolution_ratio():
    """find desktop screen resolution"""
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    ratio = width/height
    return ratio

def image_ratio(image):
    """return width/height ratio of given image"""
    width = image['data']['preview']['images'][0]['source']['width']
    height = image['data']['preview']['images'][0]['source']['height']
    return width/height

def find_most_compatible(children):
    """take a list of images and return the most compatible one"""
    children = sorted(children, key=lambda k: image_ratio(k))
    most_compatible = min(
        children, key=lambda x:abs(image_ratio(x)-screen_resolution_ratio())
    )
    url = most_compatible['data']['url']
    return url

def get_image_url():
    """if there is no error, return URL of background image from EarthPorn"""
    #gather information from reddit API
    request_url = 'https://www.reddit.com/r/EarthPorn/top/.json?limit=20'
    result = requests.get(request_url, headers = {'User-agent': 'friendly program'})
    response = json.loads(result.text)

    if "error" in response:
        #print error message if there is an error
        print('Error ' + str(response["error"]) + '. ' + response["message"])
        return 1
    else:
        #find most compatible image and return it
        children = response["data"]["children"]
        url = find_most_compatible(children)
        return url

def download_image(image_url):
    """download and save image to current directory"""
    file_path = 'image.' + image_url.split('.')[-1]
    f = open(file_path,'wb')
    f.write(requests.get(image_url).content)
    f.close()

def set_background():
    """set the desktop background"""
    path = os.getcwd()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + '\image.jpg' , 0)

start_time = time.time()
image_url = get_image_url()

if image_url != 1:
    download_image(image_url)
    set_background()

print("--- %s seconds ---" % (time.time() - start_time))

input("\nPress enter key to exit.")