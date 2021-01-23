num = input("Enter a number: ")

list_num = list(num)
length = len(num)


total = 0

if not num.isdigit():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
  
else:
    for i in list_num:
        total += int(i) ** length
    if int(num) == total:
        print(num,"is an Armstrong number")    
    else:
        print(num,"is not an Armstrong number")


   
   
 
