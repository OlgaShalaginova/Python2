# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
os.system('cls')

number = int(input('Введите число: '))
num = 1
for i in range(number):
    i = i + 1
    num = num*i
    print(num, end= " ")