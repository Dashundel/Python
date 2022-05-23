import saveData

def exportData(format, save): 
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()

    if len(data) == 0: print('Телефонная книга пуста')

    i = 0
    dataSave = []
    
    while i < len(data):
        #экспорт данных из файла в формате строки
        if format == 'строка':
            #экспорт данных, если данные в файле записаны в формате столбика
            if str(data[i]).find(',') == -1 and data[i] != '\n':
                dataSave.append(data[i].replace('\n',',') + data[i+1].replace('\n',',') + data[i+2].replace('\n',',') + data[i+3])
                print(data[i].replace('\n',',') + data[i+1].replace('\n',',') + data[i+2].replace('\n',',') + data[i+3])
                i = i + 4
            #экспорт данных, если данные в файле записаны в формате строки    
            else:
                print(data[i].replace('\n',''))
                dataSave.append(data[i].replace('\n',''))
                i += 1
        
        #экспорт данных из файла в формате столбца    
        elif format == 'столбик': 
            #экспорт данных, если данные в файле записаны в формате столбика
            if str(data[i]).find(',') == -1 and data[i] != '\n': 
                print(data[i].replace('\n',''))
                dataSave.append(data[i])
            #экспорт данных, если данные в файле записаны в формате строки    
            else:
                print(data[i].replace(',', '\n'))
                dataSave.append(data[i].replace(',', '\n'))
            i += 1
            
    #сохранение данных, если необходимо        
    if save == 'да': saveData.saveData(dataSave)       

               