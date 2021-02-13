#Write a Python program that prints such as "2020 is a leap year" if the given year by the user is a leap year, 
#prints such as "2019 is not a leap year" otherwise.

year = int(input("Insert a 4-digit year:"))

if not year % 400 or (not year % 4 and year % 100):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    
    

