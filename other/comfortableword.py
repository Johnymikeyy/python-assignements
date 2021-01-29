
word = set(input("enter a word:"))

right_hand = "hjklnmyuiop"
left_hand = "asdfgzxcvbqwert"

list1 = set(right_hand)
list2 = set(left_hand)


right_side = word.difference(list1)
left_side = word.difference(list2)


print(bool(left_side) and bool(right_side))









