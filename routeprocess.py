import random
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from restaurant1 import flex_message_json_template

def backendprocess(event):
    triggerwords = ['กินอะไรดี','กินไรดี']
    if event.message.text in triggerwords:
        flex_message = FlexSendMessage(
            type = 'flex',
            alt_text='CU iCanteen',
            contents=json.loads(flex_message_json_template)
    )
    return flex_message