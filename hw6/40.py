#Создайте программу для игры в "Крестики-нолики" при помощи PIP, т.е. визуализировать её.

import random
from tkinter import *

root = Tk()      
root.title('Крестики-нолики')

gameRun = True    
field = [] 
xCount = 0 

#отрисовка поля
def newGame():   
    for i in range(3):
        for j in range(3):
            field[i][j]['text'] = ' '
            field[i][j]['background'] = 'white'
    global gameRun
    gameRun = True
    global xCount
    xCount = 0

#обработка хода
def click(row, col):       
    if gameRun and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global xCount
        xCount += 1
        checkWin('X') 
        if gameRun and xCount < 5:
            computerMove()
            checkWin('O') 

#проверка хода
def checkWin(type):
    for i in range(3):
        checkLine(field[i][0], field[i][1], field[i][2], type)
        checkLine(field[0][i], field[1][i], field[2][i], type)
    checkLine(field[0][0], field[1][1], field[2][2], type)
    checkLine(field[2][0], field[1][1], field[0][2], type)

#проверка выигрышных линий
def checkLine(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        global gameRun
        gameRun = False
        
#проверка на победу
def canWin(a1, a2, a3, smb):   
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

#ход компьютера
def computerMove():
    for i in range(3):
        if canWin(field[i][0], field[i][1], field[i][2], 'O'):
            return
        if canWin(field[0][i], field[1][i], field[2][i], 'O'):
            return
    if canWin(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if canWin(field[2][0], field[1][1], field[0][2], 'O'):
        return

    while True: 
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

for row in range(3):
    line = []
    for col in range(3):
        button = Button(text=' ', width=6, height=3,
                        font=('Verdana', 22, 'bold'),
                        background='white',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

new_button = Button(text='Новая игра', command=newGame)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

root.mainloop()
