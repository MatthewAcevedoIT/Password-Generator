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
