import hashlib
import getpass
import os
import random
import string
import json

# Using a file to persist the password data between runs.
PASSWORD_FILE = 'user_passwords.json'

def load_passwords():
    """Load user passwords from a JSON file."""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_passwords(passwords):
    """Save user passwords to a JSON file."""
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file)

def generate_salt(length=16):
    """Generate a random salt."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def hash_password(password, salt):
    """Hash the password with the salt."""
    password_salt_combined = password + salt
    return hashlib.sha256(password_salt_combined.encode()).hexdigest()

def create_account():
    """Create a new user account."""
    username = input("Create a username: ")

    # Prevent overwriting of existing accounts
    if username in user_passwords:
        print("Username already exists. Please choose a different one.")
        return

    password = getpass.getpass("Create a password: ")

    # Generate a salt and hash the password
    salt = generate_salt()
    hashed_password = hash_password(password, salt)

    # Store the salt and hashed password
    user_passwords[username] = {"salt": salt, "password": hashed_password}
    save_passwords(user_passwords)
    print("Account created successfully!")

def login():
    """Log in with an existing account."""
    username = input("Enter your username: ")

    if username not in user_passwords:
        print("Invalid username or password.")
        return

    password = getpass.getpass("Enter your password: ")
    salt = user_passwords[username]["salt"]
    stored_hashed_password = user_passwords[username]["password"]

    # Hash the entered password with the stored salt
    hashed_password = hash_password(password, salt)

    if hashed_password == stored_hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    """Main function to drive the program."""
    global user_passwords
    user_passwords = load_passwords()  # Load the existing passwords at the start

    while True:
        user_choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if user_choice == "1":
            create_account()
        elif user_choice == "2":
            login()
        elif user_choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
