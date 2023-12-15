import random
import string

def password_generator(length = 12):
    characters = string.ascii_letters + string.digit + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print('PASSWORD GENERATOR')

    try:
        password_length = int(input("Enter the password:"))
    except:
        print("Invalid password. Please enter a valid password")
        return

    password = password_generator(password_length)

    print('Generated Password:', password)

if __name__ == "__main__":
    main()
