""" 
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end ='')
    print() 
"""
"""
*
**
***
****
*****
"""
for i in range(1, int(input()) + 1):
    for j in range(1, i + 1):
       print("*", end ='')
    print()
 
"""
1
12
123
1234
12345
"""   
for i in range(1, int(input()) + 1):
    for j in range(1, i + 1):
        print(j, end ='')
    print()
    
"""
12345
1234
123
12
1
"""
print('-----------------------------------')
x = 5
for i in range(1,6):  
    for j in range(1, x + 1):
        print(j,end="") 
    x = x - 1
    print()
    
"""
1
22
333
4444
55555
"""
print('-----------------------------------')
""" 
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end='')
    print()
 """    
for i in range(1, 6):
    print(str(i) * i)

"""
1
2 3
4 5 6
7 8 9 10

Analysis :
-------------------------------------------------
i(row)  :   1   2   3   4
j(col)  :   1   2   3   4
"""
print('-----------------------------------')
count = 1
for i in range(1, 5):
    for j in range(1, i + 1):
        print(count, end=' ')
        count += 1
    print()

"""
    *
   **
  ***
 ****
*****
"""
print("-"*50)
for i in range(1, 5):
    for j in range(4, i, -1):
        print("-", end='')
    for k in range(1, i + 1):
        print("*", end='')
    print()
        
"""
    *
   ***
  *****
"""
print("-"*50)
for i in range(1, 4):
    for j in range(3, i, -1):
        print(" ", end='')
   #for k in range(1, i + 1):
   #    print("*", end='')
   #for p in range(1, i):
   #    print("*", end='')
    for k in range(1, ((2 * i)-1) + 1):
        print("*", end='')
    print()