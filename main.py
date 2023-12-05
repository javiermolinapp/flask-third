from flask import Flask, jsonify
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Hola to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
