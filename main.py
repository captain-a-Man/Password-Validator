import re

# Function to load rockyou.txt passwords
def load_default_passwords(filename):
    try:
        with open(filename, 'r', encoding='latin-1') as file:  # 'latin-1' avoids decoding errors
            return set(line.strip().lower() for line in file)
    except FileNotFoundError:
        print("rockyou.txt file not found.")
        return set()

def check_password_strength(password, default_passwords):
    if password.lower() in default_passwords:
        print("This is a default/common password from rockyou.txt!")
        return

    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error):
        print("This is a strong password!")
    else:
        print("This is a weak password!")
        if length_error:
            print("- Too short (must be at least 8 characters)")
        if digit_error:
            print("- No digits")
        if uppercase_error:
            print("- No uppercase letters")
        if lowercase_error:
            print("- No lowercase letters")
        if symbol_error:
            print("- No special symbols (e.g., !, @, #)")

# Load passwords from rockyou.txt
default_passwords = load_default_passwords('rockyou.txt')

# Ask for user input
password = input("Enter your password: ")
check_password_strength(password, default_passwords)
