def saveData(lst):
    idDesk = int(lst[6])*100 + int(lst[5])*10 + int(lst[6])
    
    with open('name.csv', 'a', encoding='utf-8') as name:
        name.write(lst[0] + ';' + lst[1] + ';' + lst[2] + ';' + str(idDesk) + ';'+ lst[4])
        name.write('\n')
    with open('class.csv', 'a', encoding='utf-8') as classe:
        classe.write(str(idDesk) + ';' + lst[5] + ';'+ lst[6] + ';'+ lst[7])
        classe.write('\n')
    with open('adress.csv', 'a', encoding='utf-8') as adress:
        adress.write(lst[0] + ';' + lst[8] + ';'+ lst[9] + ';'+ lst[10]+ ';'+ lst[11]+ ';'+ lst[12])
        adress.write('\n')

def addData():
    with open('name.csv','r') as name:
        data = name.read()
    id = len(data)
    lst = []
    lst.append(str(id))    
    lst.append(input('Введите Фамилию: '))
    lst.append(input('Введите Имя: '))
    lst.append(str(input('Введите Класс: ')))
    lst.append(input('Введите Статус: '))
    lst.append(str(input('Введите Номер парты: ')))
    lst.append(str(input('Введите Ряд: ')))
    lst.append(str(input('Введите Вариант: ')))
    lst.append(input('Введите Город: '))
    lst.append(input('Введите Улица: '))
    lst.append(str(input('Введите Дом: ')))
    lst.append(str(input('Введите Квартира: ')))
    lst.append(input('Введите Примечание к адресу: '))
    
    saveData(lst)