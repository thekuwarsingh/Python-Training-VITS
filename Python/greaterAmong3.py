x, y, z = int(input()), int(input()), int(input())

""" 
if x > y and  x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z) 
"""

""" 
Nested if-else

if x > y:
    if x > z:
        print(x)
    else:
        print(z)
else:
    print(y)     
"""
print(max(x, y, z))