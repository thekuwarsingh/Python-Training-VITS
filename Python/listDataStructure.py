myList = [1, "Harry Potter", "Hogwarts", 15]

print(myList)
print(myList[1])
print(myList[1][6:])
print(myList[2][0])

for i in myList:
    print(i)
    
print('-'*40) 
   
count = 0
for i in myList:
    #print(count,"->", i)
    print("myList[{}] -> {}".format(count, i))
    count += 1

print('-'*40)

for i in myList:
    print("myList[{}] -> {}".format(myList.index(i), i))
    
print('-'*40)

i = 0
while i < len(myList):
    print(i,"->",myList[i])
    i += 1

print('-'*40)
    
myList[1] = "Hermione Granzer"

for i in myList:
    print(f"myList[{myList.index(i)}] -> {i}")
    
