from itertools import count
from random import *
import os
os.system("cls")

nums = [randint(1,15) for i in range (21)]
print("list: ", nums, '\n')
nums1 = list(filter(lambda x: nums.count(x) == 1, 1))
nums2 = [i for i in nums if nums.count(i) == 1]

print("list elements: ", nums1)
print("list elements: ", nums2)