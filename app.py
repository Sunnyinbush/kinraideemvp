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
line_bot_api = LineBotApi('vqiiCUBQCIZS0AJwgAunwn47nyFlDemUcsx9fr7SPXIQmXIlbg17N5hm0z+zo1Kcgges2TvHcKRoDuKBFiF0rAHuqE7TBQNYFlk1Q+Mkq2UyymeyWA249Abektv8lnES71cNhVO1LdOQiqsX/kx5ywdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ca2d11dc313463c0420dce1998398dfa')

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

#user responds "กินอะไรดี"
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text_message = backendrouter(event.message.text)
    if text_message != None:
        print("Text Message Recieved! Sending Quick Reply Message!")
    line_bot_api.reply_message(event.reply_token, text_message)

#quick reply
@handler.add(PostbackAction, message= Postback)
def handle_message(event):
    quick_reply_message = quickreply_backend(event.data.displayText)
    if quick_reply_message != None:
        print("We have received user reply")
        line_bot_api.reply_message(event.reply_token, flex_message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
