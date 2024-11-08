from flask import Flask, request, jsonify
import os

app = Flask(__name__)
stored_data = {}  # A simple dictionary to temporarily store data

# Home route
@app.route('/')
def home():
    return "Welcome to the Booking Assistant!"

# Endpoint to receive data from Zapier
@app.route('/zapier-data', methods=['POST'])
def receive_data():
    global stored_data
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400
    
    # Store the received data (use a database for long-term storage)
    stored_data = data
    print("Data received from Zapier:", data)
    return jsonify({"message": "Data received successfully"}), 200

# Endpoint to retrieve data for GPT
@app.route('/get-data', methods=['GET'])
def get_data():
    return jsonify(stored_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
