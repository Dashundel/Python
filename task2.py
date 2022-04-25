#Найти максимальное из пяти чисел
num1 = int(input('Введи число 1 '))
num2 = int(input('Введи число 2 '))
num3 = int(input('Введи число 3 '))
num4 = int(input('Введи число 4 '))
num5 = int(input('Введи число 5 '))

max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3
if num4 > max:
    max = num4  
if num5 > max:
    max = num5      

print ('Макс = ', max)        