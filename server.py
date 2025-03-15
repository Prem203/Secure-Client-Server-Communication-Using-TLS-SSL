from flask import Flask, request, jsonify
import ssl

app = Flask(__name__)

# In-memory message store (Dictionary format: {username: [messages]})
messages_store = {}

@app.route('/')
def home():
    return "🔒 Secure TLS Chat Server Running with Mutual Authentication!"

# Send a message (POST)
@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    username = data.get("username")
    message = data.get("message")
    
    if not username or not message:
        return jsonify({"error": "Username and message required"}), 400
    
    if username not in messages_store:
        messages_store[username] = []
    
    messages_store[username].append(message)
    return jsonify({"message": "Message sent successfully!", "data": {username: message}}), 201

# Retrieve messages by username (GET)
@app.route('/receive/<username>', methods=['GET'])
def receive_messages(username):
    if username in messages_store:
        return jsonify({"username": username, "messages": messages_store[username]})
    else:
        return jsonify({"error": "No messages found for this user"}), 404

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations("client.crt")  # Mutual TLS Authentication
    
    app.run(host='0.0.0.0', port=5002, ssl_context=context)
