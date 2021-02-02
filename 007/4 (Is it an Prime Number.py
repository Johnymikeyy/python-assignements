num = int(input("Enter a number to learn whether it is prime number or not: \n"))

for i in range(2, num):
    if num % i == 0:
      print(f"{num} is not a prime number")
      break
    
else:
  print(f"{num} is a prime number")
  
  
###

number = int(input("Please enter the number you want to learn whether is Prime Number or not:\n"))
primekey = 0

for i in range(2, number):
    if number % i == 0:
        print("{} is not a Prime Number.".format(number))
        primekey += 1
        break

print((not primekey) * f"{number} is a Prime Number.")