#38. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв"


def deleteWord(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

print('Введите текст: ')
text = input() 

text = deleteWord(text)
print(text)