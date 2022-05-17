#36.	Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.

import os
os.system("cls")

nums = [3, 1, 2, 3, 4, 6, 1, 7]

def get_create(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups    

print(get_create(nums))