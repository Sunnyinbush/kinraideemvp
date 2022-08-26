import random
import json

from linebot.models import *

from jsonstorage import *

def backendprocess(inputword):
    triggerwords = ['กินอะไรดี','กินไรดี', 'kinraidee', 'KinRaiDee', 'Kinraidee']
    example_message = ['คำตัวอย่าง','example']
    #have some random function to select restaurant
    if inputword in triggerwords:
        payload = randomselectrestaurant()
        flex_message = FlexSendMessage(
            type = 'flex',
            alt_text=payload["body"]["content"]["text"],
            contents=json.loads(payload)
    )
    elif inputword in example_message:
        flex_message = FlexSendMessage(
            type = 'flex',
            alt_text='CU iCanteen',
            contents=json.loads(flex_message_json_example)
    )
    return flex_message

def randomselectrestaurant():
    #open csv file as list
    with open('restaurant.csv', 'r') as csvfile:
        restaurantlist = csvfile.readlines()
    #random select restaurant
    randomrestaurant = random.choice(restaurantlist)

def convertjsontostring(json):
    return json.dumps(json)