#Реализовать алгоритм перемешивания списка

from random import shuffle

print('Введите число:')
n = int(input())

list = list(range(-n, n + 1))
print(list)
    
shuffle(list)
print(list)