from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint 1 : handel message
@app.route('/message', methods=['POST'])
def handle_message():
    # Extract JSON data from the request
    data = request.get_json()
    print(f"Received message: {data}")
    # Respond with a confirmation message
    return jsonify({"status": "success", "message": "Message received!"}), 200

# Endpoint 2 : Health check
@app.route('/health', methods =['GET'])
def check_health():
    return jsonify({"status": "Running"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6060)
