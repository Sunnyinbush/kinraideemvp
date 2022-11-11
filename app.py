from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from oldrouteprocess import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('reGGOrpOZ5RafgV+VqQHiULKInLdOq4gTKa3npfHWNzorpMn/V85a7axufVRJzmHvhxlGAuJ9wAqI6NMGIHjdL1yMqoFkR3JwoAHrTbNnqiI91pFvfp/AWgnOQCMk2vWEBvbGLgT4POpr+nZOye9ewdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('9c727591b56bf0a08a4a404605a97f2c')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if flex_message != None:
        print("Flex Message Sent!")
        line_bot_api.reply_message(event.reply_token, reply_message)