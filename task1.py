#По двум заданным числам проверить является ли одно квадратом второго 
import os
os.system('cls')

num1 = int(input('Введи число 1 '))
num2 = int(input('Введи число 2 '))

if num1**2 == num2 or num2**2 == num1:
    print('Является')
else:
    print('нет')    