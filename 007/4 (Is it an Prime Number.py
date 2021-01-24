num = int(input("Enter a number to learn whether it is prime number or not: \n"))

for i in range(2, num):
    if num % i == 0:
      print(f"{num} is not a prime number")
      break
    
else:
    print(f"{num} is a prime number")