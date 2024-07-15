
import random
import string

def generate_password(length):
    
    # Combine all possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters)for i in range(length))
    return password

def main():
    try:
        
        # Get the desired length of the password from the user.
        length = int(input("Enter the desired length for your password: "))
        
        # Validate that the length is a positive integer
        if length <= 0:
            print("Please enter a positive integer.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generate password
        print(f"Generate Password: {password}")
        
    except ValueError:
        
        # Handle non-integer input
        print("Invalid input. Please enter a valid number.")
        
if __name__ == "__main__":
    main()
