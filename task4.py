#Показать первую цифру дробной части числа
num = float(input('Введи дробное число '))
num1 = int((num*10)%10)
print(round(num1))