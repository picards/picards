from flask import Flask
import sys
sys.path.insert(1, '../../secrets')
from config import DevConfig, ProdConfig
conf = DevConfig

app = Flask(__name__)

from app import routes


if __name__ == "__main__":
    app.run()