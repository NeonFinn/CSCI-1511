def rotation_adjustment(rotation):
    if rotation < 0:
        rotation = rotation + 360
    elif rotation > 360:
        rotation = rotation - 360
    return rotation

def main():
    while True:
        try:
            rotation = int(input("Enter a rotation: "))
            print(rotation_adjustment(rotation))
            if input("Press q to quit or enter to continue: ") == "q" or "Q":
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()