
def saveData(data):
    print(data)
    with open('phonebookExp.csv', 'w', encoding='utf-8') as file:
        for i in range(0, len(data)):    
            file.write(data[i])
        
   