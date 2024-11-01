import logging
import requests
from flask import Blueprint, render_template, request, jsonify, make_response, url_for, redirect
from flask_cors import CORS
from flask_login import login_required, current_user
from datetime import timezone, datetime
from Database.authentication import store_chat_history
from flask_babel import gettext as _

views = Blueprint('views', __name__)
CORS(views)
RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'

@views.route('/')
def home():
    return render_template("home.html",)

@views.route('/games')
@login_required
def games():
    return render_template("games.html", user=current_user)

@views.route('/community')
def community():
    return render_template("community.html")

@views.route('/help')
def help():
    return render_template("help.html")

@views.route('/withdraw-deposit')
@login_required
def withdrawDeposit():
    return render_template("withdraw-deposit.html")

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html")

@views.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    return render_template('chatbot.html')

@views.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json.get('message')
    print("User message: ", user_message)
    rasa_response = requests.post(RASA_API_URL, json={'sender': 'default', 'message': user_message})
    rasa_response_json = rasa_response.json()
    print("Rasa response: ", rasa_response_json)

    if rasa_response_json:
        bot_response = rasa_response_json[0].get('text', "Sorry, I didn't get that. Can you rephrase?")
        buttons = rasa_response_json[0].get('buttons', [])
    else:
        bot_response = "Sorry, I didn't get that. Can you rephrase?"
        buttons = []
    print ("Bot response: ", bot_response)
    user_id = current_user
    print("User ID: ", user_id)

    if user_id:
        message_timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        try:
            store_chat_history({
                'userid': "1",
                'messagetimestamp': message_timestamp,
                'messagecontent': user_message,
                'airesponse': bot_response
            })
        except Exception as e:
            print(e)
            logging.error(e)
    else:
        message_timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        try:
            store_chat_history({
                'userid': "0",
                'messagetimestamp': message_timestamp,
                'messagecontent': user_message,
                'airesponse': bot_response
            })
        except Exception as e:
            print(e)
            logging.error(e)


    return jsonify({'message': bot_response, 'buttons': buttons, user_message: user_message})

@views.route('/set_language/<language>')
def set_language(language):
    
    rasa_server_url = 'http://localhost:5055/conversations/default/tracker/events'
    headers = {'Content-Type': 'application/json'}
    data = {
        "event": "slot",
        "name": "language",
        "value": language
    }
    
    print(data)
    response = requests.post(rasa_server_url, headers=headers, json=data)
    response = make_response(redirect(url_for('views.home')))
    response.set_cookie('language', language)
    return response

