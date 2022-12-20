# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import os
import random
os.system('cls')

num = int(input('Введите число: '))
my_list = []
for _ in range(num):
        my_list.append(random.randint(-num, num + 1))
print("Список:", my_list)
index_list = []
res = 1
with open('file.txt', 'r') as data:
    for x in data:
               index_list += [int(x)]
               res *= my_list[int(x)]
print("Индексы из файла:", index_list)
#Список начинается с 0 индекса
print("Произведение элементов на указанных позициях равно:", res)

