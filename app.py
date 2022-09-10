from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from routeprocess import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('reGGOrpOZ5RafgV+VqQHiULKInLdOq4gTKa3npfHWNzorpMn/V85a7axufVRJzmHvhxlGAuJ9wAqI6NMGIHjdL1yMqoFkR3JwoAHrTbNnqiI91pFvfp/AWgnOQCMk2vWEBvbGLgT4POpr+nZOye9ewdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('9c727591b56bf0a08a4a404605a97f2c')

# callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message1 = backendprocess1(event.message.text)
    message2 = backendprocess2(event.postback.data)
    if message1 != None:
        line_bot_api.reply_message(event.reply_token, message1)
    if message2 != None:
        line_bot_api.reply_message(event.reply_token, message2)
    
    # flex_message = backendprocess2(event.message.text)
    # if flex_message != None:
    #     line_bot_api.reply_message(event.reply_token, flex_message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
