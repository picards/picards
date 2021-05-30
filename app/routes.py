from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import requests
from app import app
from sawo import createTemplate, verifyToken
import json

createTemplate("app/templates/partials", flask=True)

load = ''
loaded = 0

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
    return render_template("landing.html")

@app.route('/addcards')
def addcards():
    return render_template("add_cards.html")

@app.route('/sharecards')
def sharecards():
    return render_template("share.html")

@app.route('/viewshared')
def viewshared():
    return render_template("add_cards.html")

@app.route('/playcards')
def playcards():
    return render_template("play_cards.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/0/<name>')
def open_page(name):
    if load != '':
        return redirect(url_for(name))
    setLoaded()
    setPayload(load if loaded < 2 else '')
    sawo = {
        "auth_key":"cdf3f6a8-b776-43f7-85f3-4d898a7a0779",
        "to":("login/"+name),
        "identifier":"email"
    }
    return render_template("sawo.html", sawo=sawo, load=load)

@app.route("/login/<name>", methods=["POST","GET"])
def login(name):
    payload = json.loads(request.data)["payload"]
    setLoaded(True)
    setPayload(payload)
    status = 200 if(verifyToken(payload)) else 404
    return {"status" : status}