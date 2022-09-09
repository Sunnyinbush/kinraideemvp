import random
import json
import csv

from linebot.models import *

from jsonstorage import *

def backendprocess(inputword):
    randomtrigger = ['กินอะไรดี','กินไรดี', 'kinraidee', 'KinRaiDee', 'Kinraidee']
    example_message = ['คำตัวอย่าง','example']
    if inputword in randomtrigger:
        flex_message = randomprocess()
    elif inputword in example_message:
        print(json.loads(flex_message_json_example))
        flex_message = FlexSendMessage(
            type = 'flex',
            alt_text='CU iCanteen',
            contents=json.loads(flex_message_json_example)
    )
    else:
        flex_message = None
    return flex_message

def randomprocess():
    payload = randomselectrestaurant()
    json_payload = json.dumps(payload)
    print(json.loads(json_payload))
    flex_message = FlexSendMessage(
        type = 'flex',
        alt_text=payload["body"]["contents"][0]["text"],
        contents=json.loads(json_payload)
    )
    return flex_message

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
    #place title
    final_json["body"]["contents"][0]["text"] = restaurant[1].strip()
    #location
    final_json['body']['contents'][1]['contents'][0]['contents'][1]['text'] = restaurant[2].strip()
    #open time
    final_json['body']['contents'][1]['contents'][1]['contents'][1]['text'] = restaurant[3].strip()
    #navigate button
    if len(restaurant) > 4:
        final_json['footer']['contents'][0]['action']['uri'] = restaurant[4].strip()
    if len(restaurant) > 5:
        final_json['footer']['contents'][1]['action']['uri'] = restaurant[5].strip()
    return final_json

backendprocess("Kinraidee")