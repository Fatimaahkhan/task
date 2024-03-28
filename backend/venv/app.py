from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb://mongodb:27017/')
db = client.web_app_database
collection = db.users

@app.route('/api/save-data', methods=['POST'])
def save_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if name and email:
        collection.insert_one({'name': name, 'email': email})
        return jsonify({'message': 'Data saved successfully'})
    else:
        return jsonify({'error': 'Name and email are required'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
