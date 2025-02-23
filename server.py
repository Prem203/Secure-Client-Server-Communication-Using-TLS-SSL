from flask import Flask, request, jsonify
import ssl

app = Flask(__name__)

# In-memory key-value store
key_value_store = {}

@app.route('/')
def home():
    return "🔒 Secure TLS Server Running!"

# Store a Key-Value Pair (POST)
@app.route('/store', methods=['POST'])
def store():
    data = request.json
    key = data.get("key")
    value = data.get("value")

    if not key or not value:
        return jsonify({"error": "Key and value required"}), 400

    key_value_store[key] = value
    return jsonify({"message": "Key-Value stored successfully!", "data": {key: value}}), 201

# Retrieve a Value by Key (GET)
@app.route('/fetch/<key>', methods=['GET'])
def fetch(key):
    value = key_value_store.get(key)
    if value:
        return jsonify({"key": key, "value": value})
    else:
        return jsonify({"error": "Key not found. Enter valid key"}), 404

# Delete a Key-Value Pair (DELETE)
@app.route('/delete/<key>', methods=['DELETE'])
def delete(key):
    if key in key_value_store:
        del key_value_store[key]
        return jsonify({"message": f"Key '{key}' deleted successfully"}), 200
    else:
        return jsonify({"error": "Key not found"}), 404

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")  # Load TLS certificate
    app.run(host='0.0.0.0', port=5002, ssl_context=context)
