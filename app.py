# 載入LineBot所需要的模組
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Azq7PyEqnuIp67jsljWm78eEJyRqbY3aGDyDcfXuWYJ079GwiTVXMyQVW5drPh4xSCgNavRehBoOcDeiMKaq83t1VeiKA9VNJHLOf2T6l8ISRkugnWe/6SYI+x9igJTztEk1jNGB8C3t2QJ/nWFicQdB04t89/1O/w1cDnyilFU=')

# 必須放上自己的Channel Secret
handler = WebhookHandler('c9e39d95fb213944652e06690c005139')


# 監聽所有來自 /callback 的 Post Request
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

# 測試用
line_bot_api.push_message('U34c0faadf0c0e51f739ebb1fcc90e0e9', TextSendMessage(text='你可以開始

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)