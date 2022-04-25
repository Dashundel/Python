#Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
x = int(input('Введи число x '))
y = int(input('Введи число y '))
z = int(input('Введи число z '))
if(not(x and y and z) == (not x and not y and not z) ): 
    print ('true') 
else:
    print ('false')