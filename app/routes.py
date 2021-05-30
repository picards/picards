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
        "auth_key":"34b10c22-1add-4f46-90fa-8b28dbe38d83",
        "to":"login",
        "identifier":"email"
    }
    return render_template("index.html", sawo=sawo, load=load)

@app.route("/login", methods=["POST","GET"])
def login():
    payload = json.loads(request.data)["payload"]
    setLoaded(True)
    setPayload(payload)
    status = 200 if(verifyToken(payload)) else 404
    return {"status" : status}