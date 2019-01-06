from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def index():
    return jsonify({"message": "hello world"})