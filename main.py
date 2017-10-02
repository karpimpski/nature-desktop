#import libraries
import ctypes
import os
import requests
import json
import urllib
import time

def get_image_url():
    """if there is no error, return URL of background image from EarthPorn"""
    #gather information from reddit API
    request_url = 'https://www.reddit.com/r/EarthPorn/top/.json?count=20'
    result = requests.get(request_url, headers = {'User-agent': 'friendly program'})
    response = json.loads(result.text)

    if "error" in response:
        print('Error ' + str(response["error"]) + '. ' + response["message"])
        return 1
    else:
        url = response["data"]["children"][0]["data"]["url"]
        return url

def download_image(image_url):
    """download and save image to current directory"""
    f = open('image.jpg','wb')
    f.write(requests.get(image_url).content)
    f.close()

def set_background():
    """set the desktop background"""
    path = os.getcwd()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + '\image.jpg' , 0)

image_url = get_image_url()

if image_url != 1:
    download_image(get_image_url())
    set_background()