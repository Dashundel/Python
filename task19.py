# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел
import time
from datetime import datetime

print('Введите количество цифр в числе:')
n = int(input())
dec = 1
num = int(time.time())
for i in range(n):
    dec *= 10
num = num % dec    
print(num)
