import Circle
import Rectangle

def invalid_input():
    print("-----------------------------------")
    print("Invalid input. Please try again.")
    print("-----------------------------------")

def input_validation(prompt):
    value = input(prompt)
    if value.replace(".", "", 1).isdigit():
        return float(value)
    else:
        invalid_input()

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            print("-----------------------------------")

main()