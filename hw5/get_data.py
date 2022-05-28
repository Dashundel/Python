from calendar import c
from itertools import zip_longest
from unittest import result

def getData():
    with open('name.csv', 'r', encoding='utf-8') as n:
        name = n.readlines()

    with open('class.csv', 'r', encoding='utf-8') as c:
        classe = c.readlines()

    with open('adress.csv', 'r', encoding='utf-8') as ad:
        adress = ad.readlines()
    
    
    for i in range(len(name)):
        strName = name[i].rstrip('\n').replace(';', ', ')
        strCls = classe[i].rstrip('\n').replace(';', ', ')
        strAdr = adress[i].rstrip('\n').replace(';', ', ')

        print(strName + ', ' + strCls + ', ' + strAdr)



