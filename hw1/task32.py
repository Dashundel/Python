#32.	Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

n = int(input("Введите длину списка: "))
list = []

#list1 = list(set(list))
#print(list1)

for i in range(n):
    list.append(random.randint(1,10))

print(list)    

for j in list:
    if list.count(j) > 1: 
        list.remove(j)

print(list)
