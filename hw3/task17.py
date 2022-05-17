#17.	Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
from functools import reduce 

n = int(input('Введите число N: '))
p = 1
with open('file17.txt', 'w') as f:
    for i in range(1, n // 2 + 2):
        f.write(str(random.randint(1, n*2)) + '\n')
    
num = list(range(-n, n + 1))
print(num)

with open('file17.txt', 'r') as f:
    dlist = [int(i.strip()) for i in f]
print(dlist)
        
for i in dlist: p = p * num[int(i) - 1]

print(p)