'''
   1. python3 <SERVER_FILE>.py
   2. npm install -g localtunnel
   3. npx lt -p 8000
'''
from flask import Flask, redirect
import requests
app = Flask(__name__)

first_request_done = False

@app.route('/')
def index():
    return redirect('http://127.0.0.1:1337/admin')

app.run(port=8000)