import string
import random

def generate_password(length=12, use_symbols=True, use_numbers=True, use_uppercase=True, use_lowercase=True):
    # Define character sets based on user preferences
    characters = ''
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    # Ensure at least one character type is selected
    if not characters:
        return "Please select at least one character type for the password."

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user preferences for password generation
try:
    length = int(input("Enter password length (default is 12): ") or 12)
    use_symbols = input("Include symbols? (y/n, default is y): ").lower() != 'n'
    use_numbers = input("Include numbers? (y/n, default is y): ").lower() != 'n'
    use_uppercase = input("Include uppercase letters? (y/n, default is y): ").lower() != 'n'
    use_lowercase = input("Include lowercase letters? (y/n, default is y): ").lower() != 'n'
except ValueError:
    print("Invalid input. Please enter a valid number for password length.")
else:
    # Generate and print the password
    password = generate_password(length, use_symbols, use_numbers, use_uppercase, use_lowercase)
    print("Generated Password:", password)
