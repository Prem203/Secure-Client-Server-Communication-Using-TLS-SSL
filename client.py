import requests

SERVER_URL = "https://localhost:5002"

def store_key_value():
    key = input("Enter key: ")
    value = input("Enter value: ")
    response = requests.post(f"{SERVER_URL}/store", json={"key": key, "value": value}, verify="server.crt")
    print("🔹 Response:", response.json())

def fetch_value():
    key = input("Enter key to fetch: ")
    response = requests.get(f"{SERVER_URL}/fetch/{key}", verify="server.crt")
    print("🔹 Response:", response.json())

def delete_key():
    key = input("Enter key to delete: ")
    response = requests.delete(f"{SERVER_URL}/delete/{key}", verify="server.crt")
    print("🔹 Response:", response.json())

def main():

    store_key_value()
    fetch_value()
    delete_key()

    # while True:
    #     print("\n🔹 Secure Key-Value Store Client 🔹")
    #     print("1. Store a key-value pair")
    #     print("2. Fetch a value by key")
    #     print("3. Delete a key-value pair")
    #     print("4. Exit")

    #     choice = input("Select an option: ")
    #     if choice == "1":
    #         store_key_value()
    #     elif choice == "2":
    #         fetch_value()
    #     elif choice == "3":
    #         delete_key()
    #     elif choice == "4":
    #         print("Exiting Secure Client...")
    #         break
    #     else:
    #         print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
