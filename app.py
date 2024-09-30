from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests



RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User message: ", user_message)
    rasa_response = requests.post(RASA_API_URL, json={'sender': 'test_user', 'message': user_message})
    rasa_response_json = rasa_response.json()
    print("Rasa response: ", rasa_response_json)

    if rasa_response_json:
        bot_response = rasa_response_json[0].get('text', "Sorry, I didn't get that. Can you rephrase?")
        buttons = rasa_response_json[0].get('buttons', [])
    else:
        bot_response = "Sorry, I didn't get that. Can you rephrase?"
        buttons = []
    
    print ("Bot response: ", bot_response)

    return jsonify({'message': bot_response, 'buttons': buttons})

if __name__ == '__main__':
    app.run(debug=True, port=5005)
