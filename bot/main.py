"main module which imports another modules"
import requests
import json
from misc import TOKEN
import crypto
import messageParser
from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

URL = 'https://api.telegram.org/bot' + TOKEN + '/'
helper =\
"""
Use this pattern for correct bot working:
/ce <number> <message> - to encrypt message using caesar cipher
/cd <number> <message> - to decrypt message using caesar cipher
/ve <key> <message> - to encrypt message using vigenere cipher
/vd <key> <message> - to decrypt message using vigenere cipher
/hash <message> - to hash your message
"""
about =\
"""
My name is Vitaliy.
I'm Python Developer.
My contacts:
Email - flamaster0806@gmail.com
Telegram - https://telegram.me/calvados0806
"""

def get_updates():
    "get new json-object, that contains new user's data and return it"
    url = URL + 'getupdates'
    response = requests.get(url)

    return response.json()

def message_data(response):
    "parse json-object and return dict with needful params for sending message"
    chat_id = response['message']['chat']['id']
    message_text = response['message']['text']
    name = response['message']['chat']['last_name']

    return {'chat_id': chat_id, 'text': message_text, 'name': name}

def send_message(chat_id, text="Wait a second..."):
    "send some message to user using chat_id"
    url = URL + 'sendmessage'
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=data)
    return response.json()

def handle_command(info):
    command = info.group('command')
    key = info.group('key')
    text = info.group('text')
    if command == '/help' or text == None:
        return helper
    elif command == '/about':
        return about
    elif command == '/ce':
        try:
            ikey = int(key)
        except ValueError:
            raise
        answer = crypto.caesar(text, ikey)
        return answer
    elif command == '/cd':
        try:
            ikey = int(key)
        except ValueError:
            raise
        answer = crypto.caesar(text, ikey, decode=True)
        return answer
    elif command == '/ve':
        answer = crypto.vigenere(text, key)
        return answer
    elif command == '/vd':
        answer = crypto.vigenere(text, key, decode=True)
        return answer
    elif command == '/hash':
        answer = crypto.hash_(info.group('another'))
        return answer

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        resp = request.get_json()
        data = message_data(resp)
        info = messageParser.get_info(data['text'])
        chat_id = data['chat_id']
        if not info:
            send_message(chat_id, helper)
            return jsonify(resp)
        else:
            try:
                answer = handle_command(info)
            except ValueError:
                send_message(chat_id, helper)
                return jsonify(resp)
            send_message(chat_id, answer)
            return jsonify(resp)
    return '<h1>Hello from Bot</h1>'

if __name__ == '__main__':
    app.run()
