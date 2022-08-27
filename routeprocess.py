import random
import json
import csv

from linebot.models import *

from jsonstorage import *

def randomselectrestaurant():
    #open csv file as list
    randomselectrestaurant.var = open("restaurantlist.csv", "r")
    # with open('restaurantlist.csv', 'r') as datafile:
    data = csv.reader(randomselectrestaurant.var, delimiter=';')
    header = next(data)
    table = [row for row in data]
    #random select restaurant
    choice = random.choice(table)
    randomrestaurant = choice[0].split(',')
    post_data = convertjsontostring(randomrestaurant)
    randomselectrestaurant.var.close()
    return post_data

def convertjsontostring(restaurant):
    final_json = flex_message_json_template
    #photo url
    final_json["hero"]["url"] = restaurant[0].strip()
    #photo link
    final_json["hero"]["action"]["uri"] = restaurant[1].strip()
    #place title
    final_json["body"]["contents"][0]["text"] = restaurant[2].strip()
    #location
    final_json['body']['contents'][1]['contents'][0]['contents'][1]['text'] = restaurant[3].strip()
    #open time
    final_json['body']['contents'][1]['contents'][0]['contents'][1]['text'] = restaurant[4].strip()
    return final_json

def backendprocess(inputword):
    triggerwords = ['กินอะไรดี','กินไรดี', 'kinraidee', 'KinRaiDee', 'Kinraidee']
    example_message = ['คำตัวอย่าง','example']
    #have some random function to select restaurant
    if inputword in triggerwords:
        payload = randomselectrestaurant()
        json_payload = json.dumps(payload)
        print(json.loads(json_payload))
        flex_message = FlexSendMessage(
            type = 'flex',
            alt_text=payload["body"]["contents"][0]["text"],
            contents=json.loads(json_payload)
    )
        
    elif inputword in example_message:
        print(json.loads(flex_message_json_example))
        flex_message = FlexSendMessage(
            type = 'flex',
            alt_text='CU iCanteen',
            contents=json.loads(flex_message_json_example)
    )
    return flex_message

backendprocess('kinraidee')