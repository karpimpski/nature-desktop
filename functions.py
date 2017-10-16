#import libraries
import requests
import json

def image_ratio(image):
    """return width/height ratio of given image"""
    width = image['data']['preview']['images'][0]['source']['width']
    height = image['data']['preview']['images'][0]['source']['height']
    return width/height

def find_most_compatible(children, platform):
    """take a list of images and return the most compatible one"""
    children = sorted(children, key=lambda k: image_ratio(k))
    most_compatible = min(
        children, key=lambda x:abs(image_ratio(x)-platform.screen_resolution_ratio())
    )
    url = most_compatible['data']['preview']['images'][0]['source']['url']
    
    if len(url.split('.')[-1]) != 3 and url.split('.')[-1] != 'com':
        url = url + '.jpg'
        
    return url

def get_image_url(platform):
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
        url = find_most_compatible(children, platform)
        return url
