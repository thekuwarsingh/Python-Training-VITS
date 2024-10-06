#List   :   It is a mutable Data Type. It is a collection of 
#           non-homogeneous data item in a sequential manner.

List = []           #Empty List
List1 = list()      #Empty List

"""
print(type(List, List))    
    Exception has occurred: TypeError
        -   type() takes 1 or 3 arguments
"""
print(type(List), type(List1))

print("List : ", List)
List.append(12)
print("List : ", List)
List.append(23)
print("List : ", List)
List[1] = 10
print("List : ", List)
List.remove(10)
print("List : ", List)

# ()  function call
# ()  tuple
# ()  any-operation
# {}  Dictionary
# {}  Set
# []  List
# []  Accessing or Modifying Sequence 