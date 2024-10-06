def factorial(n):
    fact = 1
    for i in range(n, 1, -1):
        fact = fact * i
    return fact

def pow(x, y):
    power = 1
    for i in range(y):
        power = power * x
    return power