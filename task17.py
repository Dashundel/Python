#Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
from random import randint

print('Введите число N')
n = int(input())
p = 1
num = list(range(-n, n + 1))
print(num)

сс

data = open('file.txt', 'r') 
     
for i in data:
    p = p * num[int(i) - 1]

data.close() 
print(p)