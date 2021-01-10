flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers)
count2 = 0

while count1>0 :
    print(flowers[count2])
    count1 -= 1
    count2 += 1

for i in {'n1' : 'one', 'n2' : 'two'} : print(i) 


iterable = [1, 2, 3, 4]

for i in iterable:
    print(i**2)

n = int(input('enter a number between 1-10'))

for i in range(11):
    print('{}x{} = '.format(n, i), n*i)
    
print(18**2)


