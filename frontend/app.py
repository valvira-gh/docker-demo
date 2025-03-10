from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5000/joke"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-joke', methods=["GET"])
def get_joke():
    try:
        response = requests.get(BACKEND_URL)
        return jsonify(response.json())
    except requests.exceptions.RequestException:
        return jsonify({"setup": "Virhe", "punchline": "Ei saatu yhteyttä palvelimeen."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)