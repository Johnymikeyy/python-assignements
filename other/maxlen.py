x = [['C', 'L'], ['A', 'R', 'U'], ['S', 'W', 'A', 'Y']]

a = max(list(x), key=len)
b = len(max(list(x), key=len))
print(a)
print(b)
result = a, b
print(tuple(result))


import random

print(random.randrange(1, 10))