import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return 1.5 * 1.732 * self.side_length

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 6 * 120

    def display(self):
        print("Hexagon:")
        print("Area:", self.calcArea())
        print("Perimeter:", self.calcPeri())
        print("Sum of Angles:", self.calcAngleSum())

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length ** 2

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        print("Square:")
        print("Area:", self.calcAreaSquare())
        print("Perimeter:", self.calcPeriSquare())

# Get the last digit of your CNIC
cnic = "XY210351532"
last_digit = int(cnic[-1])

# Create instances of Hexagon and Square classes
hexagon = Hexagon(last_digit)
square = Square(last_digit + 1)

# Display menu
while True:
    print("\nMenu:")
    print("1. Hexagon")
    print("2. Square")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        hexagon.display()
    elif choice == '2':
        square.display()
    else:
        print("Exiting program.")
        break
