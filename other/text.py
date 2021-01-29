my_dict2 = {'even numbers': [2, 4, 6, 8, 10, 12, 14, 16]}

for v in my_dict2.values():
    my_list = []
    for y in v:
        my_list.append(y**2)
            
my_dict2['even_numbers'] = my_list
print(my_dict2)
    

