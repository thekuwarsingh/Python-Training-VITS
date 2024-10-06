#Simple Scientific Calculator

from math import *

print('-'*20,'Scientific Calculator','-'*20)
print("Arithmetic :   +, -, x, /, r, e, i")
print('Scientific :   L, S, s, c, t, f')
print('1 - Binary Operation')
print('2 - Unary Operation')
print('Operation Choice : ', end="")
O = int(input())
#Arithmetic :   +, -, x, /, r, e, i
#Scientific :   L, S, s, c, t, f
if (O == 1):
    print("Operation : ", end = '')
    choice = input()
    x = float(input())
    y = float(input())
    if choice == '+':
        print(x + y)
    elif choice == '-':
        print(x - y)
    elif choice == 'x':
        print(x * y)
    elif choice == '/':
        print(x / y)
    elif choice == 'r':
        print(x % y)
    elif choice == 'e':
        print(x ** y)
    elif choice == 'i':
        print(x // y)
    else:
        print("Invalid Operation!")
elif O == 2:
    print("Operation : ", end = '')
    choice = input()
    x = float(input())
    if choice == 'L':
        print(log(x))
    elif choice == 'S':
        print(sqrt(x))
    elif choice == 's':
        print(sin(x))
    elif choice == 'c':
        print(cos(x))
    elif choice == 't':
        print(tan(x))
    elif choice == 'f':
        if x >= 0:
            print(factorial(int(x)))
        else:
            print("Invalid Digit.")
    else:
        print("Invalid Operation!")