import keyword

# print(keyword.kwlist)
count = 0
for i in keyword.kwlist:
    print(i,end ='\t')
    count += 1
    if count % 5 == 0:
        print()