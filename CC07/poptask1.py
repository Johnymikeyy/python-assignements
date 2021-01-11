#Given a string (clarusway) and an index number int n (n=3), 
#return a new string where the character at index n has been removed.

my_word = 'clarusway'
print(my_word[2])
my_word1 = list(my_word)
print(my_word1)
my_word1.pop(3)
print(my_word1)



new_word = my_word.replace(my_word[3],"")
print(new_word)

