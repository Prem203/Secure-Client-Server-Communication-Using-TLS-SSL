import requests

SERVER_URL = "https://localhost:5002"
CERT_PATH = "client.crt"
KEY_PATH = "client_unencrypted.key"
CA_CERT_PATH = "server.crt"  # Verify the server's certificate

def send_message():
    username = input("Enter your username: ")
    message = input("Enter your message: ")
    response = requests.post(
        f"{SERVER_URL}/send",
        json={"username": username, "message": message},
        cert=(CERT_PATH, KEY_PATH),
        verify=CA_CERT_PATH
    )
    print("\n🔐 Response:", response.json())

def receive_messages():
    username = input("Enter username to fetch messages: ")
    response = requests.get(
        f"{SERVER_URL}/receive/{username}",
        cert=(CERT_PATH, KEY_PATH),
        verify=CA_CERT_PATH
    )
    print("\n🔐 Response:", response.json())

def main():
    while True:
        print("\n💬 Secure Chat Client 💬")
        print("1. Send a message")
        print("2. Receive messages")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            send_message()
        elif choice == "2":
            receive_messages()
        elif choice == "3":
            print("Exiting Secure Chat Client...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
