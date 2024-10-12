import random
import string

# Function to generate a password
def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password from the characters
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Main program loop
def main():
    print("Password Generator")
    
    # Input validation for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length should be a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == '__main__':
    main()