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
@app.route('/index')
def index():
    setLoaded()
    setPayload(load if loaded < 2 else '')
    sawo = {
        "auth_key":"cdf3f6a8-b776-43f7-85f3-4d898a7a0779",
        "to":"login",
        "identifier":"phone_number_sms"
    }
    return render_template("index.html", sawo=sawo, load=load)

@app.route("/login", methods=["POST","GET"])
def login():
    payload = json.loads(request.data)["payload"]
    setLoaded(True)
    setPayload(payload)
    status = 200 if(verifyToken(payload)) else 404
    return {"status" : status}