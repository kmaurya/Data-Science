from flask import Flask
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    pass


@app.route('/train', methods=['POST'])
def trainRouteClient():
    pass


if __name__ == "__main__":
    app.run(port=8000)
