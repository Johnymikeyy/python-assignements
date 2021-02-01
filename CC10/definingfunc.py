#Write a function called divisible that takes as input parameters two numbers and returns “divisible” if the first is a factor of the second, “not divisible” if it isn’t, and “error” if the second parameter is a zero. 


def divisible(x, y):
    if y % x != 0:
        return "not divisible"
    elif y == 0:
        return "error"
    else:
        return "divisible"
    
        
print(divisible(2, 1))

###
def divisible(x, y):
    if y == 0:
        return "error"
    elif y % x != 0:
        return "not divisible"
    else:
        return "divisible"
    
print(divisible(2, 1))
