import get_data
import add_data

def find():
    action = str(input('Выберите действие: 1 - добавить информацию, 2 - получить данные? '))
        
    if action == '1':
        add_data.addData() 
        
    elif action == '2':
        get_data.getData()
        
    else: print('Неверный тип операции')
            