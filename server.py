from flask import Flask, request, jsonify, render_template
import ssl
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
CORS(app, supports_credentials=True)

messages = {"user1": [], "user2": []}

@app.route("/")
def home():
    return "🔒 Secure TLS Server Running!"

@app.route("/chat")
def chat():
    return render_template("secure_chat.html")

@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    sender = data.get("username")  # sender (user1 or user2)
    message = data.get("message")

    # Determine recipient (if sender is user1, recipient is user2)
    recipient = "user2" if sender == "user1" else "user1"

    if sender in messages and recipient in messages:
        messages[recipient].append({"text": message, "type": "received"})  # Recipient gets it as a received message
        messages[sender].append({"text": message, "type": "sent"})  # Sender stores it as a sent message
        return jsonify({"message": "Message sent successfully!"}), 201

    return jsonify({"error": "Invalid user"}), 400

@app.route("/receive/<username>")
def receive_messages(username):
    if username in messages:
        return jsonify({"messages": messages[username], "username": username})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    app.run(host="0.0.0.0", port=5002, ssl_context=context)
