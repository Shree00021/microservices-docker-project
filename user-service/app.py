from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []

@app.route('/')
def home():
    return "User Service Running"

@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added", "users": users})

@app.route('/get', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)