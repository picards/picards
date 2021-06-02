from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import requests
from app import app
from sawo import createTemplate, verifyToken
import json
import uuid
from app import conf
from app.sqldb import create_account

createTemplate("app/templates/partials", flask=True)

load = ''
loaded = 0
account_uuid = None
email = None

def setPayload(payload):
    global load
    load = payload

def setLoaded(reset=False):
    global loaded
    if reset:
        loaded = 0
    else:
        loaded += 1

@app.route('/')
def landing():
    return render_template("landing.html", title="")

@app.route('/addcards')
def addcards():
    return render_template("add_cards.html", title="Add Card")

@app.route('/sharecards')
def sharecards():
    return render_template("share.html", title="Share Cards")

@app.route('/viewshared')
def viewshared():
    return render_template("add_cards.html", title="View Shared")

@app.route('/playcards')
def playcards():
    return render_template("play_cards.html", title="Play Cards")

@app.route('/relaxspace')
def relaxspace():
    return render_template("meme.html", title="Relax Space")

@app.route('/home')
def home():
    return render_template("index.html", title="Home")

@app.route('/addcard', methods=["POST"])
def addcard():
    question = request.form['qn']
    answer = request.form['ans']
    return redirect('/0/addcards')

@app.route('/0/<name>')
def open_page(name):
    if load != '':
        account_id = str(load['user_id'])
        email = str(load['identifier'])
        create_account(account_id, email)
        return redirect(url_for(name))
    setLoaded()
    setPayload(load if loaded < 2 else '')
    sawo = {
        'auth_key' : conf.SAWO_API_KEY,
        'to' : 'login',
        'identifier' : 'email'
    }
    return render_template("sawo.html", sawo=sawo, load=load, title="Login")

@app.route("/login", methods=["POST","GET"])
def login():
    payload = json.loads(request.data)["payload"]
    setLoaded(True)
    setPayload(payload)
    status = 200 if(verifyToken(payload)) else 404
    return {"status" : status}