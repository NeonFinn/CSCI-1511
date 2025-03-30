def rotation_adjustment(rotation):
    if rotation < 0:
        rotation = rotation % 360
    elif rotation > 360:
        rotation = rotation % 360
    return rotation

def main():
    while True:
        try:
            rotation = (input("Enter a rotation: "))
            if (rotation.isdigit()) or (rotation[0] == '-' and rotation[1:].isdigit()):
                rotation = int(rotation)
                print(rotation_adjustment(rotation))
            else:
                raise ValueError
            if input("Press q to quit or enter to continue: ") == "q":
                break
        except:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()