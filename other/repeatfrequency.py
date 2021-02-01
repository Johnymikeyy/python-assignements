numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

print("Given List:",numbers)
print(set(numbers))
print(type(numbers))
repeat = max(numbers, key = numbers.count) # finds the most repeated number

print(repeat)

print(numbers.count(repeat)) # finds the frequency of the most repeated number

print("the most frequent number is", int(repeat), "and", "it was repeated", numbers.count(3), "times")
