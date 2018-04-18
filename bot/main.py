import requests
from misc import TOKEN
import crypto
import messageParser

URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def getUpdetes():
    url = URL + 'getupdates'
    response = requests.get(url)

    return response.json()

def messageData(response):
    chatId = response['result'][-1]['message']['chat']['id']
    messageText = response['result'][-1]['message']['text']
    name = response['result'][-1]['message']['chat']['last_name']

    return {'chat_id': chatId, 'text': messageText, 'name': name}

def sendMessage(chat_id, text="Wait a second..."):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():
#     commands = ['/ce', '/ve', '/h', '/cd', '/vd']
#     standart_message = \
# """Type /ce to encrypt text using caesar cipher. Then type key and your message.
# Type /cd to decrypt text using caesar cipher. Then type key and your message.
#
# Type /ve to encrypt text using Vigenere cipher. Then type keyword and your message.
# Type /vd to decrypt text using Vigenere cipher. Then type keyword and your message.
#
# Type /h to hash your message. Then type your message."""
#
#     response = getUpdetes()
#     data = messageData(response)
#     chat_id = data['chat_id']
#     text = data['text']
#
#     com = messageParser.get_command(text)
#     if com:
#         if len(com) != 1:
#             sendMessage(chat_id, "To many commands")
#             sendMessage(chat_id, standart_message)
#         elif com[0] not in commands:
#             sendMessage(chat_id, "Unknown command")
#             sendMessage(chat_id, standart_message)
#     else:
#         sendMessage(data['chat_id'], standart_message)
    pass

if __name__ == '__main__':
    main()
