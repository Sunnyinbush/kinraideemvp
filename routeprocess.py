import random
import json
import csv
from selectors import EVENT_READ

from linebot.models import *

from jsonstorage import *

def backendprocess(inputword,source):
    randomtrigger = ['กินอะไรดี','กินไรดี', 'kinraidee', 'KinRaiDee', 'Kinraidee']
    example_message = ['คำตัวอย่าง','example']
    if source.userID == None:
        print(json.loads(bubble_message_new_user))
        flex_message = FlexSendMessage(
            type = "template",
            altText =  "this is a carousel template"
            contents=json.loads(bubble_message_new_user)
        )
    elif inputword in randomtrigger:
        flex_message = randomprocess()
    else:
        flex_message = None
    return flex_message
    
    # if inputword in randomtrigger:
    #     flex_message = randomprocess()
    # elif inputword in example_message:
    #     print(json.loads(flex_message_json_example))
    #     flex_message = FlexSendMessage(
    #         type = 'flex',
    #         alt_text='CU iCanteen',
    #         contents=json.loads(flex_message_json_example)
    # )
    # else:
    #     flex_message = None
    # return flex_message

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
    #photo link
    final_json["hero"]["action"]["uri"] = restaurant[1].strip()
    #place title
    final_json["body"]["contents"][0]["text"] = restaurant[2].strip()
    #location
    final_json['body']['contents'][1]['contents'][0]['contents'][1]['text'] = restaurant[3].strip()
    #open time
    final_json['body']['contents'][1]['contents'][1]['contents'][1]['text'] = restaurant[4].strip()
    return final_json

