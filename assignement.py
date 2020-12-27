escapes = ["\n\t", ("\t", "\t\t"), ["\n", "\n\t\t"]]

words = ["eat", "tea", "tan", "ate", "nat", "bat"]


words1 = []
words1.append(words[3])
words1.append(words[0]) 
words1.append(words[1])

words2 = []
words2.append(words[2])
words2.append(words[4])

words3 = []
words3.append(words[-1])

print(words1)
print(words2)
print(words3)

