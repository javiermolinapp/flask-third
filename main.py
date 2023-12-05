from flask import Flask, jsonify
import os
import matplotlib


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Hola to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)
