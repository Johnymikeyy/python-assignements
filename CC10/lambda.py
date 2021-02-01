#Task - 1 (Lambda Functions)

#you are given a list of lists (a nested list). Write a Python program to print the list with maximum length in this nested list. The output should be in the form (list, list_length)


lst = [['C', 'L'], ['A', 'R', 'U'], ['S', 'W', 'A', 'Y']]

def findmaxlength(lst):
    maxList = max(lst, key = lambda i:len(i))
    maxLength = len(maxList)
    
    return maxList, maxLength
print(findmaxlength(lst))

max(map(len, lst))        

 