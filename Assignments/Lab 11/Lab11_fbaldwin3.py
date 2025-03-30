def rotation_adjustment(rotation):
    rotation = int(rotation)
    if rotation < 0:
        rotation = rotation % 360
    elif rotation > 360:
        rotation = rotation % 360
    return rotation

def main():
    while True:
        try:
            rotation = (input("Enter a rotation: "))
            # I had to add this in because my test case for invalid input was failing, saying that str cannot be converted to int
            if (rotation.isdigit()) or (rotation[0] == '-' and rotation[1:].isdigit()):
                print(rotation_adjustment(rotation))
            else:
                raise ValueError
            if input("Press q to quit or enter to continue: ") == "q":
                break
        except:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()