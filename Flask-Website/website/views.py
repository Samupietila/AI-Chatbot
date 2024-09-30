import logging
import requests
from flask import Blueprint, render_template, request, jsonify
from flask_cors import CORS

views = Blueprint('views', __name__)
CORS(views)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/games')
def games():
    return render_template("games.html")

@views.route('/community')
def community():
    return render_template("community.html")

@views.route('/help')
def help():
    return render_template("help.html")

@views.route('/withdraw-deposit')
def withdrawDeposit():
    return render_template("withdraw-deposit.html")

@views.route('/profile')
def profile():
    return render_template("profile.html")

@views.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_message = request.json.get('message')
        if user_message:
            # Communicate with Rasa server
            rasa_response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": user_message})
            bot_response = rasa_response.json()[0]['text'] if rasa_response.status_code == 200 else "Error communicating with Rasa"
            return jsonify({'response': bot_response})
        else:
            return jsonify({'response': 'No message received'}), 400
    return render_template('chatbot.html')