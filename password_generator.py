import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    # Define the character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all selected character sets
    all_chars = lowercase_chars + uppercase_chars + digits + special_chars
    
    if not all_chars:
        raise ValueError("At least one character set must be selected.")
    
    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            # Get user input for the length of the password
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Get user input for including various character types
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        try:
            # Generate and display the password
            password = generate_password(length, use_uppercase, use_digits, use_special_chars)
            print(f"Generated password: {password}")
        except ValueError as e:
            print(e)
            continue

        # Ask if the user wants to generate another password
        next_action = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if next_action != 'yes':
            break

    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()