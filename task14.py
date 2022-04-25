#14.	Подсчитать сумму цифр в вещественном числе

print('Введите вещественное число: ')
num = input() 

strNum = num.replace('.', '')
listNum = list(strNum)
listNum2 = map(int, listNum)
sum = sum(listNum2)

print(f"Сумма цифр вещественного числа равна = {sum}")