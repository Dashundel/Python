#34.	Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random
#генерация файла с многочленом
def genData(k, file):
    list = []

    for i in range(k + 1):
        list.append(random.randint(0,10))

    f = str(list[1]) + " * x + " + str(list[0]) + " = 0"

    if k > 1:
        for deg in range(2, len(list)):
            f = str(list[deg]) + " * x ^ " + str(deg) + " + " + f  
    else:
        f = str(list[0]) + " * x ^ 0 = " + str(list[0]) 
              
    with open(file, 'w') as data:
        data.write(f)
    print(f)
    
#извлечение коэфициентов многочлена
def getKoef(str):
    list = []
    i = -1
    j = 0

    for j in range(k):
        ind = str.index('*x', i+1) 
        list.append(str[i+1:ind]) 
        i = str.index('+', i+1)

    list.append(str[i+1 : str.index('=0')])

    return list
      
    
k = int(input("Введите степень k: "))

#генериуем файлы с многочленами
genData(k, 'f34_1.txt')
genData(k, 'f34_2.txt')

#избавляемся от пробелов      
with open('f34_1.txt', 'r') as f:
    func1 = (f.readline()).replace(' ', '') 

with open('f34_2.txt', 'r') as f:
    func2 = (f.readline()).replace(' ', '')

#получаем коэфициенты многочлена
list1 = getKoef(func1)
list2 = getKoef(func2)

#суммируем многочлен
sum = ''
for i in range(0, k - 1):
    sum = sum + str(int(list1[i]) + int(list2[i])) + ' * x ^ ' + str(k - i) + " + " 
    
sum = sum + str(int(list1[i + 1]) + int(list2[i + 1])) + ' * x + ' + str(int(list1[i + 2]) + int(list2[i + 2])) + ' = 0 ' 

#записываем результат в файл  
with open('f34_res.txt', 'w') as data:
    data.write(sum)
    
print(sum)    