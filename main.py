import requests
from misc import TOKEN

URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def getUpdetes():
    url = URL + 'getupdates'
    response = requests.get(url)
    return response.json()

def messageData(response):
    chatId = response['result'][-1]['message']['chat']['id']
    messageText = response['result'][-1]['message']['text']

    return {'chat_id': chatId, 'text': messageText}

def sendMessage(chat_id, text="Wait a second..."):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():
    pass

if __name__ == '__main__':
    main()
