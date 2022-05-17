#41.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

n = input("Введите строку символов: ")

with open('file41с.txt', 'w') as f:
    f.writelines(n)

with open('file41с.txt', 'r') as f:
    text = (f.readline())

#кодирование
    
count = 0  
output = ''
currentSybmol = text[0]  

for i in text:
    if i == currentSybmol: 
        count = count + 1
    else:
        output = output + str(count) + currentSybmol
        currentSybmol = i
        count = 1

output = output + str(count) + currentSybmol  
print(output)

with open('file41d.txt', 'w') as f:
    f.writelines(output)
    
#декодирование

with open('file41d.txt', 'r') as f:
    text = (f.readline()) 
    
output = ''    
for i in text:
    if i.isdigit(): 
        num = i
    else:
        for j in range(0, int(num)):
           output = output + i
print(output)  

with open('file41c.txt', 'w') as f:
    f.writelines(output)
