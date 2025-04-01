def rotation_adjustment(rotation):
    rotation = float(rotation)
    rotation = rotation % 360
    return f'{rotation:.2f}'

def main():
    while True:
        try:
            rotation = (input("Enter a rotation: "))
            print(rotation_adjustment(rotation))
            print("---------------------------------------")
            if input("Press q to quit or enter to continue: ").strip().lower() == "q":
                break
            print("---------------------------------------")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()