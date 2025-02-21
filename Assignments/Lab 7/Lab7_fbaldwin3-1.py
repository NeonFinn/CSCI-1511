import os

username_password = {'guest': 'guest', 'jdoe': 'password', 'rsmith': 'Eggs', 'fbaldwin': 'fb12345', 'mjones': 'OakL0g'}

input_username = input("Please provide your username: ")

if input_username in username_password:
    input_password = input("Please provide your password: ")
    if input_password == username_password[input_username]:
        print(f"Welcome {input_username}!")
    else:
        os._exit(0)
else:
    os._exit(0)

if input_password == 'guest':
    print("Security level: 5")
elif (any(character.isupper() for character in input_password)) and (any(character.isdigit() for character in input_password)):
    print("Security level: 1")
elif any(character.isdigit() for character in input_password):
    print("Security level: 2")
elif any(character.isupper() for character in input_password):
    print("Security level: 3")
else: # all lowercase
    print("Security level: 4")