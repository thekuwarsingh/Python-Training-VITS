Sum = 0
print("Odd : ", end='')
for i in range(1, 11):
    if (i % 2 != 0):
        print(i, end=" ")
        Sum = Sum + i
print()
print("Sum :", Sum)
        