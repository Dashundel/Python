#39.	Создайте программу для игры с конфетами человек против человека.

import random

def play(count, swCount, player):  
    while (count > maxSweet) or (count > swCount):
        count = int(input(f'Кол-во конфет должно быть от 0 до {maxSweet} \n и не должно превыщать остаток. \n Попробуй еще раз: ')) 
    
    if swCount - count == 0: print(f'Выиграл {player}. Поздравляем!!!')
    else: 
        swCount = swCount - count
        print(f'Осталось {swCount} конфет')
    return swCount
        
        
sweetCount = 2021
maxSweet = 28
count = 0
messages = ['игрок 1', 'игрок 2']

firstPlayer = random.choice(messages)
messages.remove(firstPlayer)
secondPlayer = messages[0]
print(f'Первым ход делает {firstPlayer}')

while sweetCount != 0:
    count = int(input(f'{firstPlayer} введите количество конфет: '))
    sweetCount = play(count, sweetCount, firstPlayer)
    
    count = int(input(f'{secondPlayer} введите количество конфет: '))
    sweetCount = play(count, sweetCount, secondPlayer)

