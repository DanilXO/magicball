from flask import render_template, jsonify

from app import app
from app import service


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Amazing magic ball')


@app.route('/get-phrase')
def get_phrase():
    return jsonify(service.get_random_phrase())
