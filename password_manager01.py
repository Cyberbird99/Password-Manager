import hashlib
import getpass

# Create an empty dictioanary to store usernames and passwords
user_passwords = {}

def create_user_account():
    #Ask the user to create a username
    username = input("Create a username: ")
    # Ask the user to create a password
    password = getpass.getpass("Create a password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_passwords[username] = hashed_password
    print("Account created successfully!")

def login():
    # Ask the user to enter the username
    username = input("Enter your username: ")
    # Ask the user to enter the password
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
   
    # check if the given credentials mathc the ones stored in the dictionary above
    if username in user_passwords.keys() and user_passwords[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


def main():
    while True:
        user_choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if user_choice == "1":
            create_user_account()
        elif user_choice == "2":
            login()
        elif user_choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

