import json
import flask
import requests

import os
from flask import Flask, request, redirect, url_for
app = Flask(__name__)
# from app import routes

@app.route('/')
def newplayer():
    if request.method == 'POST':
        pn = request.form['pn']
        return redirect(url_for('loading',name=pn))
    else:
        pn = request.args.get('pn')
        return redirect(url_for('loading',name=pn))   

@app.route('/loading')
def loading_page():
    #wait for 4 players?
    pass

'''
@app.route('/newplayer')
def newplayer():
    if request.method == 'POST':
        pn = request.form['pn']
        return redirect(url_for('loading',name=pn))
    else:
        return redirect(url_for('newplayer'))
#'''
if __name__ == '__main__':
    host = "localhost"
    #host = "0.0.0.0"
    port = "80"
    app.run(host, port, debug = True)