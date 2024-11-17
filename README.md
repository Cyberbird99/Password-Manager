# Password-Manager
Both codes are password managers.
The first one is a simple pyhthon code with hashlib and getpass libraries only.
There's no salt added, no check for repeating user names or persistent storage

A lot of fetures are added to the second like below:

Salting the passwords:
A salt is a random value added to the password before hashing. This prevents attacks like rainbow table attacks and makes it significantly harder to crack passwords. The salt is stored alongside the hashed password, but not the password itself.

Persistent storage:
The user data is stored in a JSON file (user_passwords.json). This allows accounts to persist between program runs.

Better error handling:
We prevent account overwriting by checking if the username already exists in the user_passwords dictionary before creating a new account.

Global user dictionary (user_passwords):
We load and save passwords from/to a file with a global user_passwords dictionary. This keeps track of all users and their hashed passwords and salts.

Password security:
The hash_password function now takes both the password and the salt, then hashes the concatenated string. This ensures that two users with the same password will have different hashes due to different salts.


