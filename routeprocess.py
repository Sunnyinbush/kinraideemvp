import random
import json

from linebot.models import *

from jsonstorage import *

def backendprocess(inputword):
    triggerwords = ['กินอะไรดี','กินไรดี', 'kinraidee', 'KinRaiDee', 'Kinraidee']
#have some random function to select restaurant

    if inputword in triggerwords:
        flex_message = FlexSendMessage(
            type = 'flex',
            alt_text='CU iCanteen',
            contents=json.loads(flex_message_json_example)
    )
    return flex_message

def randomselectrestaurant(place, list):
    pass

def convertjsontostring(json):
    return json.dumps(json)