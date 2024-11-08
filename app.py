from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Root route for basic check
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask app! The app is running."

# Route to handle POST requests at '/receive-data'
@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json  # Get JSON data from the request
    if not data:
        return jsonify({"error": "No data received"}), 400

    # Print data to the console for debugging
    print("Data received:", data)

    # Respond with a success message and echo the received data
    return jsonify({"message": "Data received successfully", "received_data": data}), 200

# Entry point for local development
if __name__ == '__main__':
    app.run(port=5001)

