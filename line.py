from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('uT+X26Oct2Al6RXN4Gi/f4U3b//Jl0JxXR88YloujyGyRcbyY/tJVx+Y0reITeBgAlf3a8jUFYNL+Be9etwJm30lyjXpXDki3PnOwIh08jmxc2pCgoCpaKu9vqxr0KrBQ1i0r/jamXOUhavbqWdrpQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('69308dc638b077c8b36d79ee2bb6b374')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()