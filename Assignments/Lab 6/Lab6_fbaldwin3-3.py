sons_and_fathers = {'john quincy adams': 'john adams', 'john adams': 'john adams sr', \
                    'bart simpson': 'homer simpson', 'homer simpson': 'grandpa simpson', \
                    'jaden smith': 'will smith', 'will smith': 'will smith sr', \
                    'ben skywalker': 'luke skywalker', 'luke skywalker': 'anakin skywalker', \
                    'spongebob squarepants': 'harold squarepants', 'harold squarepants': 'grandpa squarepants', \
                    'marquise jackson': 'curtis jackson', 'curtis jackson': 'unknown', \
                    'donald trump jr': 'donald trump', 'donald trump': 'fred trump', \
                    'monkey d luffy': 'monkey d dragon', 'monkey d dragon': 'monkey d garp', \
                    'harry potter': 'james potter', 'james potter': 'fleamont potter', \
                    'michael jordan': 'james jordan', 'james jordan': 'william jordan', \
                    }

print("Father Finder")
print("0 - Quit")
print("1 - Find a Father")
print("2 - Find a Grandfather")
print("3 - List Sons")

choice = input('Choice: ')
print('---------------------------------')

while choice != '0':
    if choice == '1':
        son_name = input('Enter son: ').lower().strip()
        if son_name in sons_and_fathers:
            print(f'His father is {sons_and_fathers[son_name].title()}')
            print('---------------------------------')
        else:
            print(f'The father of "{son_name.title()}" does not exist in this database')
            print('---------------------------------')
    elif choice == '2':
        son_name = input('Enter grandson: ').lower().strip()
        if son_name in sons_and_fathers:
            father = sons_and_fathers[son_name]
            if father in sons_and_fathers:
                print(f'His grandfather is {sons_and_fathers[father].title()}')
                print('---------------------------------')
            else:
                print(f'The grandfather of "{son_name.title()}" does not exist in this database')
                print('---------------------------------')
        else:
            print(f'The grandfather of "{son_name.title()}" does not exist in this database')
            print('---------------------------------')
    elif choice == '3':
        for sons in sons_and_fathers:
            print(sons.title())
        print('---------------------------------')
    else:
        print('Invalid choice')
        print('---------------------------------')


    print("Father Finder")
    print("0 - Quit")
    print("1 - Find a Father")
    print("2 - Find a Grandfather")
    print("3 - List Sons")
    choice = input('Choice: ')
    print('---------------------------------')

print('Thank you for using Father Finder. Goodbye!')