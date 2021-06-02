from flask import Flask
from app.config import DevConfig, ProdConfig
conf = DevConfig

app = Flask(__name__)

from app import routes


if __name__ == "__main__":
    app.run()