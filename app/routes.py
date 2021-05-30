from flask import Flask, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User'}
    posts = [
        {
            'author': {'username': 'Frank'},
            'body': 'hack'
        },
        {
            'author': {'username': 'Sam'},
            'body': 'hack 2'
        }
    ]
    return render_template('index.html', user=user, posts=posts)