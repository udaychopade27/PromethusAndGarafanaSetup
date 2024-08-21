from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json  # Get the JSON data sent by Alertmanager
    print(f"Received alert: {data}")
    # Here you can add logic to process the alert
    # For example, save to a database, send a notification, etc.
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
