x = [([1], [2, 3], (4, 5, 6))]

for i in x:
    for j in i:
        for k in j:
            print(k)

print(set(tuple([k for i in x for j in i for k in j])))

print(set(k for i in x for j in i for k in j))

print(set(iter for items in x for count in items for iter in count))


