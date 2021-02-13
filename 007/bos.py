for i in range(2, 101):
    print(i)
    for j in range(2,i):
        print(j)
 
 
year = int(input("Please enter a year: "))
if not year % 400 or (not year % 4 and year % 100):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year") 
