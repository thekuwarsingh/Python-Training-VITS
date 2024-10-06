#Operators : 
#   Unary  : {-, +}
#   Binary

a = 5
print(+a)
print(-a)

#Binary    :
#   Arithmetic  :   {+, -, *, /, //, %, **}
x, y = 5, 10

print(x + y)
print(x - y)
print("x * y", x * y)
print("x / y =", x / y)
print(x,'//',y,'=',x//y)
print(x,'%',y,'=',(x%y))
print('{} ** {} = {}')
print('{} ** {} = {}'.format(x,y,(x**y)))

#   Bitwise     :   {|, &, ~, ^, <<, >>} 

print(a>>2)
print(a<<2)
print(5&4)
print(7|5)
print(7^5)
print(~a)

#   Shorthand|Compound Assignment 
#               :   {+=, -=, *=, /=, %=, **=, //=}

n = 2
n += x  #n = n + x
print("n -> {}".format(n))

#   Relational  :   {<, >, <=, >=, ==, !=}     

x = a < 10
print("x - ", x)

x = a > 20
print("x - ", x)

#   Logical     :   {and, or, not} 

x = (a > 5 or a <= 10)
print("x - ", x)

x = (a > 2 and a <= 10)
print("x - ", x)

x = (not n)
print("x - ", x)

x = not(a <= 10)
print("x - ", x)

x = not(a < 2)
print("x - ", x)

x = n > 2
y = not(x)

#   Membership  :   {in, not in}

x = 5 in [1, 2, 3, 4, 5]
print("x - ", x)

Tuple = (2, 4, 6, 8)
x = 5 not in Tuple
print("x - ", x)

#   Identity    :   {is, is not}

y = x is 5
print("y - ", y)

x = 10
y = x is not 5
print("y - ", y)