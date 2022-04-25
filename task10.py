#Найти расстояние между двумя точками пространства
from cmath import sqrt

text = input('введите координаты первой точки  ')
a = text.split()

text = input('введите координаты второй точки  ')
b = text.split()

a1 = list(map(int, a))
b1 = list(map(int, b))

if len(a) == 3 : 
    print(sqrt((b1[0]-a1[0])**2 + (b1[1]-a1[1])**2 + (b1[2]-a1[2])**2))
elif len(a) == 2 :
    print(sqrt((b1[0]-a1[0])**2 + (b1[1]-a1[1])**2))
else: 
    print("координаты заданы неверно")