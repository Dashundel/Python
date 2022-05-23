
def importData(firstName, name, phone, description, format):  
    with open('phonebook.csv', 'w', encoding='utf-8') as file:
        for i in range(0, len(firstName)):
            if format == 'строка':
                file.write(f'{firstName[i]},{name[i]},{phone[i]},{description[i]}\n')
                print(f'{firstName[i]},{name[i]},{phone[i]},{description[i]}\n')
            elif format == 'столбик':
                file.write(f'{firstName[i]}\n{name[i]}\n{phone[i]}\n{description[i]}\n\n') 
                print(f'{firstName[i]}\n{name[i]}\n{phone[i]}\n{description[i]}\n')   
            else: print('Неверный формат записи данных')    

   