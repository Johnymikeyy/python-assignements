num = input("Enter a number: ")

length = len(str(num))


total = 0
new_num = num

while int(new_num) > 0:
    digit = int(new_num) % 10
    total += int(digit) ** length
    int(new_num) //= 10
 
if num == total:
    print(num,"is an Armstrong number")
    
elif type(num) != type(5):
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

else:
    print(num,"is not an Armstrong number")