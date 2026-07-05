import math
import sys


def print_menu():
    print("Scientific Calculator")
    print("====================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Natural Logarithm")
    print("8. Base-10 Logarithm")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Factorial")
    print("13. Absolute Value")
    print("14. Exponential")
    print("15. Degrees to Radians")
    print("0. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter an integer value.")


def main():
    while True:
        print_menu()
        choice = input("Choose an operation: ").strip()

        if choice == "0":
            print("Goodbye.")
            sys.exit(0)
        elif choice == "1":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            print("Result:", a + b)
        elif choice == "2":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            print("Result:", a - b)
        elif choice == "3":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            print("Result:", a * b)
        elif choice == "4":
            a = get_number("Enter dividend: ")
            b = get_number("Enter divisor: ")
            if b == 0:
                print("Error: Division by zero.")
            else:
                print("Result:", a / b)
        elif choice == "5":
            a = get_number("Enter base: ")
            b = get_number("Enter exponent: ")
            print("Result:", math.pow(a, b))
        elif choice == "6":
            a = get_number("Enter number: ")
            if a < 0:
                print("Error: Cannot compute square root of a negative number.")
            else:
                print("Result:", math.sqrt(a))
        elif choice == "7":
            a = get_number("Enter number: ")
            if a <= 0:
                print("Error: Natural logarithm is defined for positive numbers only.")
            else:
                print("Result:", math.log(a))
        elif choice == "8":
            a = get_number("Enter number: ")
            if a <= 0:
                print("Error: Log base 10 is defined for positive numbers only.")
            else:
                print("Result:", math.log10(a))
        elif choice == "9":
            a = get_number("Enter angle in degrees: ")
            print("Result:", math.sin(math.radians(a)))
        elif choice == "10":
            a = get_number("Enter angle in degrees: ")
            print("Result:", math.cos(math.radians(a)))
        elif choice == "11":
            a = get_number("Enter angle in degrees: ")
            print("Result:", math.tan(math.radians(a)))
        elif choice == "12":
            n = get_int("Enter a non-negative integer: ")
            if n < 0:
                print("Error: Factorial is defined for non-negative integers only.")
            else:
                print("Result:", math.factorial(n))
        
        print()


if __name__ == "__main__":
    main()
