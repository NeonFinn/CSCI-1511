import Circle
import Rectangle

# checks for valid input, including floats
def input_validation(user_input):
    value = input(user_input)
    # replaces "." with "" to check if the string is a float, the 1 insures that only the first "." is replaced
    # if no "." is found, the string is checked to see if it is a digit
    if value.replace(".", "", 1).isdigit():
        return float(value)
    else:
        print("-----------------------------------")
        print("Invalid input. Please try again.")
        print("-----------------------------------")

# keeps asking the user for input until they choose to quit, uses input_validation function to check for valid inputs
def main():
    while True:
        print("       MENU")
        print("1) Area of a Circle")
        print("2) Circumference of a Circle")
        print("3) Area of a Rectangle")
        print("4) Perimeter of a Rectangle")
        print("5) Quit")

        user_choice = (input("Enter your choice: "))
        print("-----------------------------------")

        if user_choice == "1":
            radius = input_validation("Enter the radius of the circle: ")
            Circle.circle_area_finder(radius)
            print("-----------------------------------")
        elif user_choice == "2":
            radius = input_validation("Enter the radius of the circle: ")
            Circle.circle_circumference_finder(radius)
            print("-----------------------------------")
        elif user_choice == "3":
            width = input_validation("Enter the width of the rectangle: ")
            height = input_validation("Enter the height of the rectangle: ")
            Rectangle.rectangle_area_finder(width, height)
            print("-----------------------------------")
        elif user_choice == "4":
            width = input_validation("Enter the width of the rectangle: ")
            height = input_validation("Enter the height of the rectangle: ")
            Rectangle.rectangle_perimeter_finder(width, height)
            print("-----------------------------------")
        elif user_choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
            print("-----------------------------------")

main()