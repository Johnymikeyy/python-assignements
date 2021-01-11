ps4_price = 250

saved_amount = int(input('Please enter your saved amount: '))

if saved_amount <= ps4_price/2:
    print("You must save more, keep saving!")

elif saved_amount > ps4_price:
    print("Yippee! You can buy your PS4")
    
else: 
    print("You saved more than half, keep saving!")
    
    
math_mark = int(input('Please enter the mark: '))

if math_mark > 85:
    print("A (Excellent)")
elif 70 < math_mark < 84:
    print("B (Good)")
elif 60 < math_mark < 69:
    print("C (Medium)") 
elif 45 < math_mark < 59:
    print("D (Not Bad)")
else:
    print("F (Failed)")