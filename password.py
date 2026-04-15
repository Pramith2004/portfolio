import hashlib
import os
import getpass

# Simple in-memory user database (for demo purposes)
users_db = {}

def hash_password(password, salt=None):
    """Hash a password with SHA-256 and a salt."""
    if salt is None:
        salt = os.urandom(16)  # Generate a random salt
    password_bytes = password.encode('utf-8')
    hashed = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, 100000)
    return salt, hashed

def register():
    print("\n--- User Registration ---")
    username = input("Enter username: ")

    if username in users_db:
        print("Username already exists!")
        return

    password = getpass.getpass("Enter password: ")

    if not validate_password(password):
        return

    salt, hashed_password = hash_password(password)
    users_db[username] = (salt, hashed_password)
    print("Registration successful!\n")

def login():
    print("\n--- User Login ---")
    username = input("Enter username: ")

    if username not in users_db:
        print("User not found!")
        return

    password = getpass.getpass("Enter password: ")
    salt, stored_hash = users_db[username]
    _, new_hash = hash_password(password, salt)

    if new_hash == stored_hash:
        print("Login successful!")
    else:
        print("Invalid credentials!")

def validate_password(password):
    """Ensure strong password rules."""
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    if not any(char in "!@#$%^&*()-_+=" for char in password):
        print("Password must contain at least one special character.")
        return False
    return True

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()