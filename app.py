from flask import (Flask, render_template, redirect,
                    url_for, request, make_response)
import json, requests, redis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whois', methods=['POST'])
def whois():
    return render_template('thisis.html')

app.run(debug=True, host='0.0.0.0', port=8000)