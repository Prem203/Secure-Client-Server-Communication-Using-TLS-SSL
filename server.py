from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # replace with os.urandom or env var in prod
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

# In-memory message storage (per user)
message_store = {}

@app.route('/')
def index():
    return "🔒 Secure WebSocket Chat Server Running!"

@app.route('/chat')
def serve_chat_ui():
    return render_template('secure_chat.html')  # served from templates/secure_chat.html

@socketio.on('connect')
def on_connect():
    username = request.args.get('username')
    print(f"[Connected] {username}")
    join_room(username)

@socketio.on('disconnect')
def on_disconnect():
    username = request.args.get('username')
    print(f"[Disconnected] {username}")
    leave_room(username)

@socketio.on('send_message')
def handle_send_message(data):
    sender = data.get('sender')
    receiver = data.get('receiver')
    message = data.get('message')
    print(f"[Message] {sender} -> {receiver}: {message}")

    # Save message for receiver
    message_store.setdefault(receiver, []).append({
        'from': sender,
        'message': message
    })

    # Emit message to receiver in their private room
    emit('receive_message', {'from': sender, 'message': message}, room=receiver)

@socketio.on('fetch_messages')
def fetch_messages(data):
    username = data.get('username')
    messages = message_store.get(username, [])
    emit('message_history', messages)
    message_store[username] = []  # clear once sent

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5002, ssl_context=('server.crt', 'server.key'))
