# run a server using flask
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='web', static_folder='web/static')

# make a route to deliver the static files in the dist folder
@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=5000, debug=True)

