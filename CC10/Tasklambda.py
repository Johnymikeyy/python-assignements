lst = [['C', 'L'], ['A', 'R', 'U'], ['S', 'W', 'A', 'Y']]

max(lst, key =len)
max(map(len, lst))   

maxLength = lambda x : (max(lst, key=len), max(map(len, lst)))
print(maxLength(lst))