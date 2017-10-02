#import libraries
import ctypes
user32 = ctypes.windll.user32
import os
import requests
import json

def screen_resolution_ratio():
    """find desktop screen resolution"""
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    ratio = width/height
    return ratio

def find_most_compatible(children):
    """take a list of images and return the most compatible one"""
    most_compatible = [None, 0]
    for i in range(0, len(children)):
        #get image data
        url = children[i]["data"]["url"]
        image = children[i]["data"]["preview"]["images"][0]["source"]
        image_resolution_ratio = image["width"]/image["height"]
        
        #compare resolution difference
        if abs(screen_resolution_ratio() - image_resolution_ratio) < abs(screen_resolution_ratio() - most_compatible[1]):
            most_compatible = [url, image_resolution_ratio]
    
    return most_compatible[0]

def get_image_url():
    """if there is no error, return URL of background image from EarthPorn"""
    #gather information from reddit API
    request_url = 'https://www.reddit.com/r/EarthPorn/top/.json?count=20'
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
    f = open('image.jpg','wb')
    f.write(requests.get(image_url).content)
    f.close()

def set_background():
    """set the desktop background"""
    path = os.getcwd()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + '\image.jpg' , 0)

image_url = get_image_url()

if image_url != 1:
    download_image(image_url)
    set_background()