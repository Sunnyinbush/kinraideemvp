from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

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
    if event.message.text = "test":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="test"))
    pass

@handler.add(JoinEvent)
def handle_join(event):
    welcomemessage = "Hello"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=welcomemessage))

@handler.add(PostbackEvent)
def handle_postback(event):
    quick_reply = quick_reply_process(event.postback.data)
    if quick_reply != None:
        line_bot_api.reply_message(event.reply_token, quick_reply)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
