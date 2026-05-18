"""
Secure Password Generator
Author: [Your Name]
Description: A beginner-friendly tool to generate strong, randomized passwords.
"""

import random
import string

def generate_password(length, use_digits, use_special):
    """
    Generates a random password based on user preferences.
    """
    # Base character set: always include lowercase and uppercase letters
    characters = string.ascii_letters  
    
    if use_digits:
        characters += string.digits  # Adds '0123456789'
    if use_special:
        characters += string.punctuation  # Adds '!@#$%' etc.

    # Randomly select characters from our pool
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("-" * 30)
    print("   SECURE PASSWORD GENERATOR   ")
    print("-" * 30)

    try:
        # Get user preferences
        length = int(input("Enter desired password length (minimum 6): "))
        if length < 6:
            print("Security Warning: Passwords shorter than 6 characters are weak.")
            length = int(input("Please enter a length of 6 or more: "))

        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'

        # Generate the password
        secure_password = generate_password(length, include_numbers, include_special)

        # Output result
        print("\n" + "=" * 30)
        print(f"Generated Password: {secure_password}")
        print("=" * 30)
        print("Keep it safe! Never share your passwords.")

    except ValueError:
        print("Error: Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
