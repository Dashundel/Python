#35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

file = open('Num.txt','w')
file.write('0 1 2 3 4 5 6 7 8 9 10 11 12')

file = open('Num.txt','r')

strNum = file.readline()
print(strNum)

splitNum = strNum.split()
for i in range(0, len(splitNum)):
    if int(splitNum[i]) + 1 != i + 1:
        findNum = i
        break

print(findNum)   

file.close

