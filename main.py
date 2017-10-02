import ctypes
import os
import requests
import json
import urllib
import time

def get_image_url():
    request_url = 'https://www.reddit.com/r/EarthPorn/top/.json?count=20'
    result = requests.get(request_url)
    response = json.loads(result.text)
    if response == {'message': 'Too Many Requests', 'error': 429}:
        print(response)
        return 1
    else:
        url = response["data"]["children"][0]["data"]["preview"]["images"][0]["source"]["url"]
        return url

def download_image(image_url):
    f = open('image.jpg','wb')
    f.write(requests.get(image_url).content)
    f.close()

def set_background():
    path = os.getcwd()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + '\image.jpg' , 0)

image_url = get_image_url()
if image_url != 1:
    download_image(get_image_url())
    set_background()
else:
    print('Error.')