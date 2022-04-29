#33.	Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k

import random

k = int(input("Введите степень k: "))
list = []

for i in range(k + 1):
    list.append(random.randint(0,100))

f = str(list[1]) + " * x + " + str(list[0]) + " = 0"

if k > 1:
    for deg in range(2, len(list)):
        f = str(list[deg]) + " * x ^ " + str(deg) + " + " + f  
else:
    f = str(list[0]) + " * x ^ 0 = " + str(list[0])       
 
print(f)    

data = open('file33.txt', 'w') 
data.writelines(f)
data.close() 