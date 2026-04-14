import json
import os

DB_FILE = "users.json"

def _load_users():
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def _save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

def login():
    print("\n--- LOGIN ---")
    username = input("Username: ")
    password = input("Password: ")
    users = _load_users()

    if username in users and users[username] == password:
        return username
    print("Error: Invalid username or password.")
    return None

def register():
    print("\n--- REGISTER NEW ACCOUNT ---")
    username = input("Choose a username: ")
    users = _load_users()

    if username in users:
        print("Error: This username is already taken.")
        return False

    password = input("Choose a password: ")
    confirm_password = input("Confirm password: ")

    if password == confirm_password:
        users[username] = password
        _save_users(users)
        print("Registration successful! You can now log in.")
        return True
    
    print("Error: Passwords do not match.")
    return False

def logout():
    print("\nLogging out... You have been safely disconnected.")

def start_login_process():
    while True: # Loop, damit man nach Fehlern/Registrierung zurückkommt
        print("\n--- WELCOME TO GROUP 4 SYSTEM ---")
        print("1. Login")
        print("2. Register")
        choice = input("Please choose an option (1/2/3): ")

        if choice == "1":
            return login()
        elif choice == "2":
            register()
        elif choice == "3":
            return None
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    current_user = start_login_process()
    if current_user:
        print(f"\nSuccess! Welcome, {current_user}.")
        input("\nPress Enter to logout...")