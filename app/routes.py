from flask import Flask, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from app import app

@app.route('/')
def home():
    return render_template('index.html')