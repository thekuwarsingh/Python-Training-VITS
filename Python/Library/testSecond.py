import pack.arithmetic

print(help(pack.arithmetic))

a, b = map(int, input().split())
Sum = pack.arithmetic.add(a, b)
Prod = pack.arithmetic.prod(a, b)
print(f'Sum\t:', Sum)
print(f'Prod\t:', Prod)