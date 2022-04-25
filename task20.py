#Определить, присутствует ли в заданном списке строк, некоторое число 
import os

print('Введите строку:')
lst = str(input())

print('Введите число:')
n = str(input())

f = lst.find(n)
if f > 0:
    print(f)
else:
    print('Такого числа нет')    