# Secure Chat Application

This project is a **Secure Chat Application** that enables two users to communicate securely using **TLS encryption**. The chat UI visually differentiates sent and received messages for better user experience.

---

## 🚀 Features

- **Secure communication** using TLS encryption.
- **Real-time messaging** with a dual-panel chat UI.
- **Color-coded messages** for better distinction.
- **HTTPS-based API** for sending and receiving messages.

---

## 📜 Prerequisites

Ensure you have the following installed:

- **Python 3.x**
- **Flask** (`pip install flask`, `pip install flask-cors`)
- **Requests** (`pip install requests`)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```sh
$ git clone https://github.com/your-repo/secure-chat-app.git
$ cd secure-chat-app
```

### 2️⃣ Setup a Virtual Environment (Optional but Recommended)

```sh
$ python -m venv venv
$ source venv/bin/activate   # For macOS/Linux
$ venv\Scripts\activate     # For Windows
```

---

## 🖥️ Running the Server

Start the **Flask Server** with SSL enabled:

```sh
$ python server.py
```

The server should start and run at:

```
https://127.0.0.1:5002
```

---

## 💬 Running the Chat UI

### Method 1: Open HTML File

Simply open `secure_chat.html` in your browser.

### Method 2: Access via Flask Server

If integrated with Flask, visit:

```
https://127.0.0.1:5002/chat
```

> If you see a **certificate warning**, manually trust the `server.crt` in your browser settings.

---

## 📡 Sending & Receiving Messages

1. Enter a message in **User 1** chat box and press **Send**.
2. The message will appear in **User 2's** chat window.
3. **User 2** can reply, and the message will show up for **User 1**.

---

## 🛠️ Troubleshooting

### Issue: "Your connection is not private"

- Manually **trust** `server.crt` in your browser.
- On Chrome: Go to `chrome://certificate-manager` → Import `server.crt`.

### Issue: Messages not updating

- Try refreshing the chat page.
- Ensure the server is running.
- Check for errors in the browser console (`F12 > Console`).

---

## 📝 Future Enhancements

- Implement **WebSocket** for real-time messaging.
- Improve **authentication** for user-specific encryption.
- Enhance **mobile responsiveness**.

---

## 📌 Contributors

- **Team** - CarpeDiem
- **Team Member 1** - Diya Deepak Wadhwani
- **Team Member 2** - Prem Bhavesh Vora

---

## 📜 License

This project is licensed under the **MIT License**.
