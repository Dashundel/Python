#14.	Подсчитать сумму цифр в вещественном числе.

sum = sum(map(int, list(input('Введите вещественное число: ').replace('.', '') )))
print(f"Сумма цифр вещественного числа равна = {sum}")