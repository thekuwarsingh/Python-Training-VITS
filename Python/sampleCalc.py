#Simple Arithmetic Calculator

print('-'*20,'Arithmetic Calculator','-'*20)
print("Arithmetic :   +, -, x, /, r, e, i")
while True:
    print("Operation : ", end = '')
    choice = input()
    x = float(input("x : "))
    y = float(input("y : "))
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
    control = input("Do you want to perform another operation (y/n) : ")
    if control.lower() == 'n':
        break
