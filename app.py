from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Endpoints for different Zaps/actions
stored_data = {
    "general_availability": {},
    "specific_availability": {},
    "event_creation": {},
    "event_finding": {},
    "event_cancellation": {},
    "event_rescheduling": {}
}

# Endpoint to receive data from a "Check General Availability" Zap
@app.route('/general-availability', methods=['POST'])
def receive_general_availability():
    global stored_data
    stored_data["general_availability"] = request.get_json() or {}
    print("Data received for General Availability:", stored_data["general_availability"])
    return jsonify({"message": "General Availability data received successfully"}), 200

# Endpoint to receive data from a "Check Specific Availability" Zap
@app.route('/specific-availability', methods=['POST'])
def receive_specific_availability():
    global stored_data
    stored_data["specific_availability"] = request.get_json() or {}
    print("Data received for Specific Availability:", stored_data["specific_availability"])
    return jsonify({"message": "Specific Availability data received successfully"}), 200

# Endpoint to receive data from an "Event Creation" Zap
@app.route('/create-event', methods=['POST'])
def receive_event_creation():
    global stored_data
    stored_data["event_creation"] = request.get_json() or {}
    print("Data received for Event Creation:", stored_data["event_creation"])
    return jsonify({"message": "Event Creation data received successfully"}), 200

# Endpoint to receive data from an "Event Finding" Zap
@app.route('/find-event', methods=['POST'])
def receive_event_finding():
    global stored_data
    stored_data["event_finding"] = request.get_json() or {}
    print("Data received for Event Finding:", stored_data["event_finding"])
    return jsonify({"message": "Event Finding data received successfully"}), 200

# Endpoint to receive data from an "Event Cancellation" Zap
@app.route('/cancel-event', methods=['POST'])
def receive_event_cancellation():
    global stored_data
    stored_data["event_cancellation"] = request.get_json() or {}
    print("Data received for Event Cancellation:", stored_data["event_cancellation"])
    return jsonify({"message": "Event Cancellation data received successfully"}), 200

# Endpoint to receive data from an "Event Rescheduling" Zap
@app.route('/reschedule-event', methods=['POST'])
def receive_event_rescheduling():
    global stored_data
    stored_data["event_rescheduling"] = request.get_json() or {}
    print("Data received for Event Rescheduling:", stored_data["event_rescheduling"])
    return jsonify({"message": "Event Rescheduling data received successfully"}), 200

# Endpoint to retrieve stored data for any action/Zap
@app.route('/get-data/<action>', methods=['GET'])
def get_data(action):
    if action in stored_data:
        return jsonify(stored_data[action] or {"message": "No data available"}), 200
    return jsonify({"error": "Invalid action"}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
