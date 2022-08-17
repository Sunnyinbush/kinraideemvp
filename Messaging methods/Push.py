from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('reGGOrpOZ5RafgV+VqQHiULKInLdOq4gTKa3npfHWNzorpMn/V85a7axufVRJzmHvhxlGAuJ9wAqI6NMGIHjdL1yMqoFkR3JwoAHrTbNnqiI91pFvfp/AWgnOQCMk2vWEBvbGLgT4POpr+nZOye9ewdB04t89/1O/w1cDnyilFU=')

try:
    profile = line_bot_api.get_profile('<user_id>')
except LineBotApiError as e:
    print("Unable to get user ID")

try:
    line_bot_api.push_message('<to>', TextSendMessage(text='Hello World! This is KinRaiDee'))
except LineBotApiError as e:
    print("Unable to push message")