#30.	Вычислить число c заданной точностью d.
# Пример: при d = 0.001,  pi = 3.141. 10^(-1) <= d <= 10^(-10) 

import math
from math import pi

print("Введи точности числа Пи: ")
d = int(input())

print(f'Число Пи: {round(pi, d)}')
