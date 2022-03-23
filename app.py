from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)       # Initializing our Flask application
ACCESS_TOKEN = 'EAAEFVDoZAycwBAAIjinqUl362nCk40sGgaWckALhORKxYbycAxmpIoDaPoJGcKCjB67yktsUck27CrG3GaiwIJdVe5EtSLMPC6wrArVUEIsf91VDQ8BYEau7ZAE9MZCvZBG0bn6rh4ErrSyKzyXZA4ld23xmYlGWgUujNsYnchPTIZCZBIc3WXYKubgKD4KlZCEZD'
VERIFY_TOKEN = 'HEAD_PAIN'
bot = Bot(ACCESS_TOKEN)

status = None

@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        global status
        jsondata = request.get_json()
        for event in jsondata['entry']:
            for message in event['messaging']:
                user_id = message['sender']['id']
                if message.get('message'):
                    if message['message'].get('text'):
                        if status:
                            if status == 1:
                                bot.send_text_message(user_id, 'Now please enter your monthly budget (including fees):')
                                status = 2
                            elif status == 2:
                                bot.send_text_message(user_id, 'Landlords often ask who the potential tenant is. Therefore, I would like to ask you a few questions:')
                                bot.send_button_message(user_id, 'Are you a student?', [{
                                                                                            "type":"postback",
                                                                                            "title":"Yes",
                                                                                            "payload":"10"
                                                                                         },{
                                                                                            "type":"postback",
                                                                                            "title":"No",
                                                                                            "payload":"10"
                                                                                        }])
                                status = None
                            elif status == 3:
                                amount = float(message['message']['text'])
                                if int(amount) > 1:
                                    bot.send_text_message(user_id,'Will you be living with the children?', [{
                                                                                            "type":"postback",
                                                                                            "title":"Yes",
                                                                                            "payload":"22"
                                                                                         },{
                                                                                            "type":"postback",
                                                                                            "title":"No",
                                                                                            "payload":"22"
                                                                                        }])
                                else:
                                    bot.send_raw('23')
                                status = None
                            elif status == 4:
                                bot.send_raw('23')
                                status = None
                            elif status == 5:
                                bot.send_button_message(user_id, "Let's summarize. Everything is correct?", [{
                                                                                            "type":"postback",
                                                                                            "title":"Yes",
                                                                                            "payload":"10"
                                                                                         },{
                                                                                            "type":"postback",
                                                                                            "title":"Not really",
                                                                                            "payload":"10"
                                                                                        }])
                                status = None
                        else:
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
                            pain = int(float(message['message']['text']))
                            bot.send_text_message(user_id, pain)
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
                    elif payload ==  '7':
                        bot.send_button_message(user_id, "What area in Wroclaw are you interested in?", [{
                                                                        "type":"postback",
                                                                        "title":"Stare Miasto",
                                                                        "payload":"8"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"Srodmiescie",
                                                                        "payload":"8"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"More options...",
                                                                        "payload":"9"
                                                                    }])
                    elif payload ==  '9':
                        bot.send_button_message(user_id, "I understand that you are interested in rent real estate please select the type:", [{
                                                                        "type":"postback",
                                                                        "title":"Kryzki",
                                                                        "payload":"8"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"Fabryczna",
                                                                        "payload":"8"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"Psie Pole",
                                                                        "payload":"8"
                                                                    }])
                    elif payload ==  '8':
                        bot.send_text_message(user_id, 'Now give us the minimum number of rooms. Enter the number below:')
                        status = 1
                    elif payload ==  '10':
                        bot.send_button_message(user_id, "Are you a working person?", [{
                                                                        "type":"postback",
                                                                        "title":"Yes",
                                                                        "payload":"11"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"No",
                                                                        "payload":"11"
                                                                    }])
                    elif payload ==  '11':
                        bot.send_button_message(user_id, "Do you have animals?", [{
                                                                        "type":"postback",
                                                                        "title":"Yes",
                                                                        "payload":"21"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"No",
                                                                        "payload":"12"
                                                                    }])
                    elif payload ==  '21':
                        bot.send_button_message(user_id, "What animals?", [{
                                                                        "type":"postback",
                                                                        "title":"Cat",
                                                                        "payload":"12"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"Dog",
                                                                        "payload":"12"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"Another",
                                                                        "payload":"12"
                                                                    }])
                    elif payload ==  '12':
                        bot.send_text_message(user_id, 'How many people are going to live including you? Please enter the number below:')
                        status = 3
                    elif payload ==  '22':
                        bot.send_text_message(user_id, 'What is the age of the child(ren)? Please enter the number below (for example "4,12")')
                        status = 4
                    elif payload == '23':
                        bot.send_button_message(user_id, 'Do you have any additional real estate requirements (eg terrace, balcony, elevator)?', [{
                                                                        "type":"postback",
                                                                        "title":"Yes",
                                                                        "payload":"13"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"No",
                                                                        "payload":"20"
                                                                    }])
                    elif payload ==  '13':
                        bot.send_button_message(user_id, "Terrace?", [{
                                                                        "type":"postback",
                                                                        "title":"Yes",
                                                                        "payload":"15"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"No",
                                                                        "payload":"15"
                                                                    }])
                    elif payload ==  '15':
                        bot.send_button_message(user_id, "Balcony?", [{
                                                                        "type":"postback",
                                                                        "title":"Yes",
                                                                        "payload":"16"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"No",
                                                                        "payload":"16"
                                                                    }])
                    elif payload ==  '16':
                        bot.send_button_message(user_id, "Lift?", [{
                                                                        "type":"postback",
                                                                        "title":"Yes",
                                                                        "payload":"17"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"No",
                                                                        "payload":"17"
                                                                    }])
                    elif payload ==  '17':
                        bot.send_button_message(user_id, "Last floor?", [{
                                                                        "type":"postback",
                                                                        "title":"Yes",
                                                                        "payload":"18"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"No",
                                                                        "payload":"18"
                                                                    }])
                    elif payload ==  '18':
                        bot.send_button_message(user_id, "Ground floor?", [{
                                                                        "type":"postback",
                                                                        "title":"Yes",
                                                                        "payload":"19"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"No",
                                                                        "payload":"19"
                                                                    }])
                    elif payload ==  '19':
                        bot.send_button_message(user_id, "Parking?", [{
                                                                        "type":"postback",
                                                                        "title":"Yes",
                                                                        "payload":"20"
                                                                    },{
                                                                        "type":"postback",
                                                                        "title":"No",
                                                                        "payload":"20"
                                                                    }])
                    elif payload ==  '20':
                        bot.send_text_message(user_id, 'What number is the best to contact you? Enter your number along with the country code. For example, +48799194461')
                        status = 5



    return "Message Processed"

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

if __name__ == "__main__":
    app.run()