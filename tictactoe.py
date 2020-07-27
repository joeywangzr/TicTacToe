import random

# FUNCTIONS: ###########################################################
def display(r1, r2, r3):
    print(str(r1)+'\n'+str(r2)+'\n'+str(r3))

def user_choice():
    while True:
        while True:
            try:
                user_row =  rows['row' + input('Select a row (1/2/3): ')]
                break
            except KeyError:
                print('Please input an integer from 1-3: ')
        while True:
            try:
                user_column = int(input('Select a column (1/2/3): ')) - 1
                break
            except KeyError:
                print('Please input an integer from 1-3: ')
        
        if user_row[user_column] == ' ':
            user_row[user_column] = 'X'
            break
        else:
            print('Tile already selected. Please choose a different position.')

def comp_choice():
    while True:
        cr = rows['row' + str(random.randint(1,3))]
        cc = random.randint(1,3) - 1
        if cr[cc] == ' ':
            cr[cc] = 'O'
            break

def check_win(d):
    return ((d['row1'][0] == 'X' and d['row1'][1] == 'X' and d['row1'][2] == 'X') or # row 1
    (d['row2'][0] == 'X' and d['row2'][1] == 'X' and d['row2'][2] == 'X') or # row 2
    (d['row3'][0] == 'X' and d['row3'][1] == 'X' and d['row3'][2] == 'X') or # row 3
    (d['row1'][0] == 'X' and d['row2'][0] == 'X' and d['row3'][0] == 'X') or # column 1
    (d['row1'][1] == 'X' and d['row2'][1] == 'X' and d['row3'][1] == 'X') or # column 2
    (d['row1'][2] == 'X' and d['row2'][2] == 'X' and d['row3'][2] == 'X') or # column 3
    (d['row1'][0] == 'X' and d['row2'][1] == 'X' and d['row3'][2] == 'X') or #diagonal 1
    (d['row1'][2] == 'X' and d['row2'][1] == 'X' and d['row3'][0] == 'X')) #diagonal 2

def check_lose(d):
    return ((d['row1'][0] == 'O' and d['row1'][1] == 'O' and d['row1'][2] == 'O') or # row 1
    (d['row2'][0] == 'O' and d['row2'][1] == 'O' and d['row2'][2] == 'O') or # row 2
    (d['row3'][0] == 'O' and d['row3'][1] == 'O' and d['row3'][2] == 'O') or # row 3
    (d['row1'][0] == 'O' and d['row2'][0] == 'O' and d['row3'][0] == 'O') or # column 1
    (d['row1'][1] == 'O' and d['row2'][1] == 'O' and d['row3'][1] == 'O') or # column 2
    (d['row1'][2] == 'O' and d['row2'][2] == 'O' and d['row3'][2] == 'O') or # column 3
    (d['row1'][0] == 'O' and d['row2'][1] == 'O' and d['row3'][2] == 'O') or #diagonal 1
    (d['row1'][2] == 'O' and d['row2'][1] == 'O' and d['row3'][0] == 'O')) #diagonal 2

def clear(board):
    for x in board:
        for i in range(0,3):
            board[x][int(i)] = ' '

########################################################################

# Start the game
print('tic tac toe !')
rows = {'row1':[' ',' ',' '],'row2':[' ',' ',' '],'row3':[' ',' ',' ']}

while True:
# Display Game Board
    display(rows['row1'], rows['row2'], rows['row3'])
# User selects position
    user_choice()
    comp_choice()
# Check if player or computer has won
    if check_win(rows):
        display(rows['row1'], rows['row2'], rows['row3'])
        print('You win!')
        
        again = input('Play again? (y/n): ')
        while True:
            if again.lower() == 'n':
                print('Thanks for playing.')
                break
            elif again.lower() == 'y':
                clear(rows)
            else: 
                print('Please input y or n.')
        
    if check_lose(rows):
        display(rows['row1'], rows['row2'], rows['row3'])
        print('You lose!')
        
        again = input('Play again? (y/n): ')
        while True:
            if again.lower() == 'n':
                print('Thanks for playing.')
                break
            elif again.lower() == 'y':
                clear(rows)
            else: 
                print('Please input y or n.')