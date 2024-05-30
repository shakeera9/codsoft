import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length for the password: "))
        
        # Ensure the length is a positive integer
        if length <= 0:
            print("Please enter a positive integer for the length.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print("Generated Password: ", password)
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()

