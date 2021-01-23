num = int(input("Enter a number: "))

length = len(str(num))


total = 0
new_num = num

while new_num > 0:
    digit = new_num % 10
    total += digit ** length
    new_num //= 10
 
if num == total:
    print(num,"is an Armstrong number")
    
else:
    print(num,"is not an Armstrong number")


   
   
 
