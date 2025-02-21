import os

username_password = {'guest': 'guest', 'jdoe': 'password', 'rsmith': 'Eggs', 'fbaldwin': 'fb12345', 'mjones': 'OakL0g'}

input_username = input("Please provide your username: ")

if input_username in username_password:
    input_password = input("Please provide your password: ")
    if input_password == username_password[input_username]:
        print("-----------------------------------------")
        print(f"Welcome {input_username}!")
    else:
        os._exit(0)
else:
    os._exit(0)

# checks for guest password
if input_password == 'guest':
    print("Security level: 5 (Bad)")

# at least one uppercase and one digit (i had to look up the solution for 'any')
elif (any(character.isupper() for character in input_password)) and \
        (any(character.isdigit() for character in input_password)):
    print("Security level: 1 (Really Good)")

# at least one digit
elif any(character.isdigit() for character in input_password):
    print("Security level: 2 (Good)")

# at least one uppercase
elif any(character.isupper() for character in input_password):
    print("Security level: 3 (Decent)")

# all lowercase
else:
    print("Security level: 4 (Not Good)")