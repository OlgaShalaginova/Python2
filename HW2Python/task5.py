# Реализуйте алгоритм перемешивания списка.

import os
os.system('cls')

import random
my_list = [1,2,3,4,5,6]
print(f"Первоначальный список:", my_list)
new_list = my_list
for _ in new_list:
    x = random.randrange(len(new_list))
    y = random.randrange(len(new_list))
    n = new_list[x]
    new_list[x] = new_list[y]
    new_list[y] = n
print(f"Перемешанный список:",new_list)
