from operator import index
import random
import json
import csv

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
            alt_text=payload["body"]["contents"][0]["text"],
            contents=json.loads(str(payload))
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
    with open('restaurantlist.csv', 'r') as datafile:
        data = csv.reader(datafile, delimiter=';')
        header = next(data)
        table = [row for row in data]
    #random select restaurant
    choice = random.choice(table)
    randomrestaurant = choice[0].split(',')
    post_data = convertjsontostring(randomrestaurant)
    return post_data

def convertjsontostring(restaurant):
    final_json = flex_message_json_template
    #photo url
    final_json["hero"]["url"] = restaurant[0]
    #photo link
    final_json["hero"]["action"]["uri"] = restaurant[1]
    #place title
    final_json["body"]["contents"][0]["text"] = restaurant[2]
    #location
    final_json['body']['contents'][1]['contents'][0]['contents'][1]['text'] = restaurant[3]
    #open time
    final_json['body']['contents'][1]['contents'][1]['contents'][1]['text'] = restaurant[4]
    return final_json

randomselectrestaurant()