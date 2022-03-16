from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)       # Initializing our Flask application
ACCESS_TOKEN = 'EAAEFVDoZAycwBAGzMO6D9XsTGZAcWyNLld6vVYnwTliMMNZAb2flBXGNVhb551uF33CE1sV7SCe3hLuDDJyihGOn3X9X14PGPN2UZAcQPnDYREfsEa77ZAMz3cyOGXDPhEjQMrf1zBn0yGbNheaTO4dlXiCKYmrow2SaE2fy8XGfS5JcH7yFuMd0ERdkFw2cZD'
VERIFY_TOKEN = 'HEAD_PAIN'
bot = Bot(ACCESS_TOKEN)

@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        jsondata = request.get_json()
        for event in jsondata['entry']:
            for message in event['messaging']:
                user_id = message['sender']['id']
                if message.get('message'):
                    if message['message'].get('text'):
                        bot.send_button_message(user_id, "Hello, I'm your  Real Estate Agent-BOT! Choose language:", [{
                                                                        "type":"postback",
                                                                        "title":"Polski",
                                                                        "payload":"1"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"Украинский",
                                                                        "payload":"2"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"English",
                                                                        "payload":"3"
                                                                    }])
                    if message['message'].get('attachments'):
                        response_sent_text = get_message()
                        send_message(user_id, response_sent_text)
                elif message.get('postback'):
                    payload = message['postback']['payload']
                    if payload ==  '1':
                        bot.send_text_message(user_id, 'O kurwa!')
                    elif payload ==  '2':
                        bot.send_text_message(user_id, 'Слава Украине!')
                    elif payload ==  '3':
                        bot.send_button_message(user_id, "Choose one of the options below:", [{
                                                                        "type":"postback",
                                                                        "title":"Looking for a real estate...   ",
                                                                        "payload":"4"
                                                                    }])
                    elif payload ==  '4':
                        bot.send_button_message(user_id, "Choose one of the options below:", [{
                                                                        "type":"postback",
                                                                        "title":"Rent",
                                                                        "payload":"5"
                                                                    }])
                    elif payload ==  '5':
                        bot.send_button_message(user_id, "I understand that you are interested in rent real estate please select the type:", [{
                                                                        "type":"postback",
                                                                        "title":"Apartment",
                                                                        "payload":"6"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"Home",
                                                                        "payload":"6"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"Commercial premises",
                                                                        "payload":"6"
                                                                    }])
                    elif payload ==  '6':
                        bot.send_button_message(user_id, "Choose one of the options below:", [{
                                                                        "type":"postback",
                                                                        "title":"Wroclaw",
                                                                        "payload":"7"
                                                                    }])    
    return "Message Processed"

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

if __name__ == "__main__":
    app.run()