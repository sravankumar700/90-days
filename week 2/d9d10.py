"""
Mini Python Basics Project

Features (no lists/arrays, no imports used):
- Interactive menu
- Basic arithmetic
- Even/Odd check
- Factorial (loop)
- Prime check
- Fibonacci sequence (iterative without arrays)
- Reverse a string
- Count vowels in a string
- Simple number pattern

Run and follow the on-screen menu. This is intended for learning loops,
conditionals, functions and basic I/O.
"""

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def basic_arithmetic():
    a = read_int("Enter first integer: ")
    b = read_int("Enter second integer: ")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Integer Division:", a // b)
        print("Float Division:", a / b)
    else:
        print("Division by zero not allowed.")


def even_odd():
    n = read_int("Enter an integer to check even/odd: ")
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")


def factorial():
    n = read_int("Compute factorial for (non-negative integer): ")
    if n < 0:
        print("Factorial not defined for negative numbers.")
        return
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    print(f"{n}! =", result)


def is_prime():
    n = read_int("Enter integer to check for primality: ")
    if n <= 1:
        print(n, "is not prime")
        return
    if n <= 3:
        print(n, "is prime")
        return
    if n % 2 == 0:
        print(n, "is not prime")
        return
    i = 3
    is_p = True
    while i * i <= n:
        if n % i == 0:
            is_p = False
            break
        i += 2
    print(n, "is prime" if is_p else "is not prime")


def fibonacci():
    terms = read_int("How many Fibonacci terms? (non-negative): ")
    if terms <= 0:
        print("No terms to show.")
        return
    a, b = 0, 1
    i = 0
    print("Fibonacci sequence:")
    while i < terms:
        print(a)
        a, b = b, a + b
        i += 1


def reverse_string():
    s = input("Enter a string to reverse: ")
    # reverse using loop (no slicing)
    rev = ''
    i = len(s) - 1
    while i >= 0:
        rev += s[i]
        i -= 1
    print("Reversed:", rev)


def count_vowels():
    s = input("Enter a string to count vowels: ")
    count = 0
    i = 0
    while i < len(s):
        ch = s[i].lower()
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1
        i += 1
    print("Vowel count:", count)


def number_pattern():
    n = read_int("Enter number of rows for a simple numeric pattern: ")
    if n <= 0:
        print("Nothing to print")
        return
    row = 1
    while row <= n:
        # print increasing numbers in a row separated by space
        col = 1
        line = ''
        while col <= row:
            line += str(col)
            if col != row:
                line += ' '
            col += 1
        print(line)
        row += 1


def menu():
    while True:
        print('\nMini Python Basics Project - Menu')
        print('1. Basic arithmetic')
        print('2. Even/Odd check')
        print('3. Factorial')
        print('4. Prime check')
        print('5. Fibonacci (iterative)')
        print('6. Reverse a string')
        print('7. Count vowels')
        print('8. Number pattern')
        print('9. Exit')
        choice = read_int('Choose an option (1-9): ')
        if choice == 1:
            basic_arithmetic()
        elif choice == 2:
            even_odd()
        elif choice == 3:
            factorial()
        elif choice == 4:
            is_prime()
        elif choice == 5:
            fibonacci()
        elif choice == 6:
            reverse_string()
        elif choice == 7:
            count_vowels()
        elif choice == 8:
            number_pattern()
        elif choice == 9:
            print('Goodbye')
            break
        else:
            print('Invalid option. Try again.')


if __name__ == '__main__':
    menu()
