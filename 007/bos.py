for i in range(2, 101):
    print(i)
    for j in range(2,i):
        print(j)
 
 
year = int(input("Enter a year: "))
if year % 4 == 0:
  if year % 400 == 0:
    print(f"{year} is a leap year")
  elif year % 100 == 0:
    print(f"{year} is a not leap year")
  else:
    print(f"{year} is a leap year")
else:
  print(f"{year} is a not leap year")



sentence = input("Enter a sentence: ")
letters_count = {}

for i in sentence:
     if i in letters_count:
        print(i)