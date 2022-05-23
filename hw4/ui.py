import exportData
import importData

def initial():
    type = input('Введите тип операции (импорт, экспорт): ')
    format = input('Введите формат данных (строка, столбик): ')

    if type == 'импорт':
        n = int(input('Введите кол-во записей: '))
        
        firstName = []
        name = []
        pnone = []
        description = []
        
        for i in range(n):
            firstName.append(input('Введите фамилию: '))
            name.append(input('Введите имя: '))
            pnone.append(input('Введите телефон: '))
            description.append(input('Введите описание: '))
            print('\n') 
        importData.importData(firstName, name, pnone, description, format)    

    elif type == 'экспорт':
        save = input('Сохранить результат (да, нет)?: ')
        exportData.exportData(format, save)

    else: print('Неверный тип операции')       

