from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    {"setup": "Miksi ohjelmoijat eivät käytä hissiä?", "punchline": "Koska he mieluummin debugaavat portaat."},
    {"setup": "Mitä sanoo 0 bitille 1?", "punchline": "Olet todella merkittävä!"},
    {"setup": "Miksi ohjelmoijat rakastavat pimeää tilaa?", "punchline": "Koska valoissa on liikaa bugeja."},
]

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200

@app.route('/joke', methods=['GET'])
def joke():
    joke = random.choice(jokes)
    return jsonify(joke)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)