import random
import json
import csv

from linebot.models import *

from jsonstorage import *

def backendprocess1(inputword):
    randomtrigger = ['กินอะไรดี','กินไรดี', 'kinraidee', 'KinRaiDee', 'Kinraidee']
    if inputword in randomtrigger:
        print(json.loads(quick_reply_temp))
        response_message = [
            QuickReplyButton(json.loads(QuickReply(quick_reply_temp))), 
            TextSendMessage({
            "type": "text",
            "text": "โปรดเลือกสถานที่ที่คุณต้องการจะไป"})
            ]
    return response_message

def backendprocess2(location):
    randomtrigger_location = ['MBK','SAMYAN', 'CHULA']
    if location in randomtrigger_location:
        file_to_access = 'restaurantlist.csv'
        flex_message = randomprocess(file_to_access)
    else:
        flex_message = None
    return flex_message

def randomprocess(location_based):
    payload = randomselectrestaurant(location_based)
    json_payload = json.dumps(payload)
    print(json.loads(json_payload))
    flex_message = FlexSendMessage(
        type = 'flex',
        alt_text=payload["body"]["contents"][0]["text"],
        contents=json.loads(json_payload)
    )
    return flex_message

def randomselectrestaurant(location_based):
    #open csv file as list
    randomselectrestaurant.var = open(location_based, "r")
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
    if len(restaurant) > 3:
        final_json['footer']['contents'][0]['action']['uri'] = restaurant[4].strip()
    return final_json

backendprocess1("Kinraidee")