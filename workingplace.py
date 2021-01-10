
left_hand = set("qwertasdfgzxcvb")
right_hand = set("yuıophjklnm")

word = set(input("Type a word and find out comfortable word :"))

left_result = word.difference(left_hand)
right_result = word.difference(right_hand)

print(left_result)
print(right_result)

print(bool(left_result))

