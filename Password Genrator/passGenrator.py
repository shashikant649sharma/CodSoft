import random
import string

try:
    password_length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the desired complexity (low/medium/high): ").lower()

    if password_length <= 0:
        print("Password length must be a positive integer.")
    elif complexity not in ['low', 'medium', 'high']:
        print("Invalid complexity level. Please choose low, medium, or high.")
    else:
        characters = string.ascii_letters + string.digits

        if complexity == 'medium':
            characters += string.punctuation
        elif complexity == 'high':
            characters += string.ascii_uppercase + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(password_length))
        print("Generated Password:", password)

except ValueError:
    print("Invalid input.")
