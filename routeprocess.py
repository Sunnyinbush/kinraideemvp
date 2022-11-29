import random
import json
import csv

from linebot.models import *

from jsonstorage import *

def backendrouter(textinput):
    triggerdictionary = {
        "MBK" : 'restaurantlist_mbk.csv',
        "สยามพารากอน" : 'restaurantlist_siamparagon.csv',
        "iCanteen" :'CSV-Chula - Icanteen.csv',
        "ตึกจุลจักรพงษ์" : 'CSV-Chula - ตึกจุล.csv',
        "โรงอาหารอักษร" : 'CSV-Chula - คณะอักษร.csv',
        "โรงอาหารรัฐศาสตร์" : 'CSV-Chula - โรงอาหารรัฐศาสตร์.csv',
        "ตึกมหิตลาธิเบศร" : 'CSV-Chula - ตึกมหิต.csv',
        "คณะครุศาสตร์" : 'CSV-Chula - โรงอาหารครุศาสตร์.csv',
        "โรงอาหารหอใน" : 'CSV-Chula - หอพักนิสิตจุฬา.csv',
        "สปอร์ตคอมเพล็กซ์" : 'CSV-Chula - Cu_Sport_Complex.csv',
        "จุฬาพัฒน์ 14" : 'CSV-Chula - จุฬสพัฒน์14.csv',
    }
    example_message = ['คำตัวอย่าง','example']
    input_word_list = textinput.split(" ")
    if input_word_list[0] == "กินอะไรดีที่":
        if input_word_list[1] in triggerdictionary:
            flex_message = randomprocess(triggerdictionary[input_word_list[1]], input_word_list[1])
        elif input_word_list[1] in example_message:
            flex_message = FlexSendMessage(
                type = 'flex',
                alt_text='CU iCanteen',
                contents=json.loads(flex_message_json_example))
        else:
            flex_message = None
    else:
        flex_message = None
    return flex_message

def randomprocess(csvfile, location):
    randomprocess.var = open(csvfile, "r")
    data = csv.reader(randomprocess.var, delimiter=';')
    header = next(data)
    table = [row for row in data]
    choice = random.choice(table)
    randomrestaurant = choice[0].split(',')
    post_data = convertjsontostring(randomrestaurant, location)
    randomprocess.var.close()
    json_payload = json.dumps(post_data)
    flex_message = FlexSendMessage(
        type = 'flex',
        alt_text=post_data["body"]["contents"][0]["text"],
        contents=json.loads(json_payload)
    )
    return flex_message

def convertjsontostring(restaurant, location):
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
    #menu button
    final_json['footer']['contents'][1]['action']['text'] = "กินอะไรดีที่ "+ location
    return final_json