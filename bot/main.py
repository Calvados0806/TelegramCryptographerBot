"main module which imports another modules"
import requests
from misc import TOKEN
import crypto
import messageParser

URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def get_updates():
    "get new json-object, that contains new user's data and return it"
    url = URL + 'getupdates'
    response = requests.get(url)

    return response.json()

def message_data(response):
    "parse json-object and return dict with needful params for sending message"
    chat_id = response['result'][-1]['message']['chat']['id']
    message_text = response['result'][-1]['message']['text']
    name = response['result'][-1]['message']['chat']['last_name']

    return {'chat_id': chat_id, 'text': message_text, 'name': name}

def send_message(chat_id, text="Wait a second..."):
    "send some message to user using chat_id"
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():
    "main function"
#     commands = ['/ce', '/ve', '/h', '/cd', '/vd']
#     standard_message = \
# """Type /ce to encrypt text using caesar cipher. Then type key and your message.
# Type /cd to decrypt text using caesar cipher. Then type key and your message.
#
# Type /ve to encrypt text using Vigenere cipher. Then type keyword and your message.
# Type /vd to decrypt text using Vigenere cipher. Then type keyword and your message.
#
# Type /h to hash your message. Then type your message."""
#
#     response = get_updates()
#     data = message_data(response)
#     chat_id = data['chat_id']
#     text = data['text']
#
#     com = messageParser.get_command(text)
#     if com:
#         if len(com) != 1:
#             send_message(chat_id, "To many commands")
#             send_message(chat_id, standard_message)
#         elif com[0] not in commands:
#             send_message(chat_id, "Unknown command")
#             send_message(chat_id, standard_message)
#     else:
#         send_message(data['chat_id'], standard_message)
    print(crypto.vigenere("Hello", "int", decode=True))

if __name__ == '__main__':
    main()
