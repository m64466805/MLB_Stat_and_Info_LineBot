import os
# import sys

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
# from linebot.models import MessageEvent, TextMessage, TextSendMessage
from machine import create_machine
# from fsm import TocMachine
from dotenv import load_dotenv
from utils import send_text_message

load_dotenv()
app = Flask(__name__, static_url_path="")


# Get channel_secret and channel_access_token from your environment variable
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
admin_id=os.getenv("LINE_ADMIN_ID",None)
# if channel_secret is None:
#     print("Specify LINE_CHANNEL_SECRET as environment variable.")
#     sys.exit(1)
# if channel_access_token is None:
#     print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
#     sys.exit(1)
machines = {}

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
line_bot_api.push_message(admin_id,TextSendMessage(text='部屬成功'))


#callback for testing  connection
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text= event.message.text)
        )

    return "OK"

#official content
@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        # Create a machine for new user
        if event.source.user_id not in machines:
            machines[event.source.user_id] = create_machine()        
        # print(f"\nFSM STATE: {machine.state}")
        # print(f"REQUEST BODY: \n{body}")
        # if event.source.user_id not in machines:
        #     machines[event.source.user_id]= create_machine()
        # machines= create_machine()
        # Advance the FSM for each MessageEvent
        response = machines[event.source.user_id].advance(event)
        # response= machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Invalid command, try again")

    return "OK"


# @app.route("/show-fsm", methods=["GET"])
# def show_fsm():
#     machine.get_graph().draw("fsm.png", prog="dot", format="png")
#     return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host='0.0.0.0', port=port) 
