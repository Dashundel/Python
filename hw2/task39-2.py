#39.	Создайте программу для игры с конфетами человек против бота.

import random

def play(count, swCount, player): 
    if player == 'игрок': 
        count = int(input(f'{player} введите количество конфет: '))
        while (count > maxSweet) or (count > swCount):
            count = int(input(f'Кол-во конфет должно быть от 0 до {maxSweet} \n и не должно превыщать остаток. \n Попробуй еще раз: ')) 
    else:
        count = random.randint(1, maxSweet if swCount > maxSweet else swCount) 
        print(f'Бот взял {count} конфет') 
    
    swCount = swCount - count
        
    if swCount == 0: print(f'Выиграл {player}. Поздравляем!!!') 
    else: print(f'Осталось {swCount} конфет')     
    return swCount
        
              
sweetCount = 50
maxSweet = 10
count = 0
messages = ['игрок', 'бот']

firstPlayer = random.choice(messages)
messages.remove(firstPlayer)
secondPlayer = messages[0]
print(f'Первым ход делает {firstPlayer}')

player = firstPlayer
while sweetCount != 0:  
    sweetCount = play(count, sweetCount, player)
    if player == firstPlayer: player = secondPlayer
    else: player = firstPlayer

