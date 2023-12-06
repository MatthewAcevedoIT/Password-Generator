# Password Generator

A Python script for generating strong and random passwords.

## Tutorial: Writing the Code

### Step 1: Import Required Modules
```python
import string
import random
```
### Step 2: Define the Password Generation Function
```python
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
```
### Step 3: Get user Preferences for Password Generation
The script will prompt you for the following preferences: 

Password Length (default is 12 characters): Enter the desired length of the password.
Include symbols? (y/n, default is y): Type 'y' to include symbols in the password or 'n' to exclude them.
Include numbers? (y/n, default is y): Type 'y' to include numbers in the password or 'n' to exclude them.
Include uppercase letters? (y/n, default is y): Type 'y' to include uppercase letters in the password or 'n' to exclude them.
Include lowercase letters? (y/n, default is y): Type 'y' to include lowercase letters in the password or 'n' to exclude them.

### Step 4: Generate and Print the Password
Once you've provided your preferences, the script will generate a password based on your selections and display it on the screen. For example:
Enter password length (default is 12): 16
Include symbols? (y/n, default is y): y
Include numbers? (y/n, default is y): y
Include uppercase letters? (y/n, default is y): y
Include lowercase letters? (y/n, default is y): y
Generated Password: R#6kL&8WuJp7x@B2


