#Write a Python program that;
#takes a sentence from the user,
#counts the number of each letter of the sentence,
#collects the letters/chars as a key and the counted numbers as a value in a dictionary.

sentence = input("Please enter a sentence:\n")

letters_count = {}

for i in sentence:
  if i in letters_count:
    letters_count[i] += 1
  else:
    letters_count[i] = 1
print(letters_count)