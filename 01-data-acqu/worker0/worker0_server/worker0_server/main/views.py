from flask import render_template

from . import main

@main.route('/', methods=['GET'])
def index():
    #return 'hello world'
    return render_template('index.html')
