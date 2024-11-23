import string
import secrets

def generate_secure_password(password_length: int = 15):
    # Ensure password is long enough for security (at least 12 characters recommended)
    if password_length < 12:
        print("Warning: A stronger password is recommended. Use at least 12 characters.")
    
    # Define the character pool (letters, digits, and punctuation)
    character_pool = string.ascii_letters + string.digits + string.punctuation

    # Generate a password that contains at least one character from each category
    while True:
        password = ''.join(secrets.choice(character_pool) for i in range(password_length))

        # Check if password has at least one uppercase, one lowercase, one digit, and one punctuation character
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            break  # Exit the loop if password meets criteria
    
    return password

# Generate a secure random password
new_password = generate_secure_password()

# Print the generated password
print(f"Generated password: {new_password}")
