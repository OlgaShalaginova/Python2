#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример:
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system('cls')

n = int(input('Введите число: '))
my_list = []
sum = 0
for i in range(1, n+1):
    my_list.append([i, round(pow(1 + (1/i),i), 2)])
    sum += (1 + 1 / i) ** i
print(dict(my_list))
print("Сумма всех чисел последовательности равна:", round(sum,2))