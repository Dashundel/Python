#Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

print('Введите число N')
n = int(input()) 

mas = []

for i in range(1, n+1):
    mas.append(1 + (1 / i) ** i)

print(f'{sum(mas):.2f}')    