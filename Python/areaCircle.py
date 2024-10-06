import math

radius = input()           #Default : In[String]
#radius = float(input())   : str -> float
#input()    : int, float, str, list, tuple, dict, set

#area = math.pi * (radius ** 2)     : TypeError  
area = math.pi * (float(radius) ** 2)

print("Area of Circle : {:.2f}".format(area))