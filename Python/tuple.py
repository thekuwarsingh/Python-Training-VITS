#Tuple  :   It is an immutable Data Type. It is a collection of 
#           non-homogeneous data item in a sequential manner.

Tuple = ()          #Empty Tuple
Tuple1 = tuple()    #Empty Tuple

"""
print(type(List, List))    
    Exception has occurred: TypeError
        -   type() takes 1 or 3 arguments
"""
print(type(Tuple), type(Tuple1))

print("Tuple : ", Tuple)

Tuple1 = (12,13,14,"Python")
print("Tuple : ", Tuple1)

#Tuple1[1] = 13     :   TypeError

del Tuple

#print("Tuple : ", Tuple)   :   NameError