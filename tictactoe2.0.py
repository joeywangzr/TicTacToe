# TO DO: CLEAR BOARD, p1 and p2 print.............

import random

print('Welcome to TicTacToe!')

def print_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

# Functions for 1st player
def player_one(board):
    while True:
        try:
            while True:
                p1_position = int(input('Player 1, select a position between 1 and 9: '))
                if p1_position > 9 or p1_position < 1:
                    print('Please input an integer between 1 and 9.')
                else:
                    break
# Check is position is free
            if board[p1_position] in ['1','2','3','4','5','6','7','8','9']:
                board[p1_position] = 'X'
                break
            else:
                print('Not available.')
    # Check if input valid
        except ValueError:
            print('Please input an integer between 1 and 9.')

# Functions for 2nd player
def player_two(board):
    while True:
        try:
            while True:
                p2_position = int(input('Player 2, select a position between 1 and 9: '))
                if p2_position > 9 or p2_position < 1:
                    print('Please input an integer between 1 and 9.')
                else:
                    break
# Check is position is free
            if board[p2_position] in ['1','2','3','4','5','6','7','8','9']:
                board[p2_position] = 'O'
                break
            else:
                print('Not available.')
    # Check if input valid
        except ValueError:
            print('Please input an integer between 1 and 9.')

# Functions for computer
def comp(board):
    while True:
        comp_position = random.randint(1,9)
        if board[comp_position] in ['1','2','3','4','5','6','7','8','9']:
            board[comp_position] = 'O'
            break

# Check win
def check_win(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # row 1
    (board[4] == mark and board[5] == mark and board[6] == mark) or # row 2
    (board[7] == mark and board[8] == mark and board[9] == mark) or # row 3
    (board[1] == mark and board[4] == mark and board[7] == mark) or # column 1
    (board[2] == mark and board[5] == mark and board[8] == mark) or # column 2
    (board[3] == mark and board[6] == mark and board[9] == mark) or # column 3
    (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal 1
    (board[3] == mark and board[5] == mark and board[7] == mark)) #diagonal 2

def check_tie(board):
    pass

def clear(board):
    for i in [1,2,3,4,5,6,7,8,9]:
        board[i] = str(i)

# Select number of players:
while True:
    try:
        vs = int(input('How many players? (1 or 2): '))
        if vs not in range(1,3):
            print('Please input 1 or 2.')
        else:
            break
    except ValueError:
        print('Please input an integer.')

if vs == 1:
    # 1 Player:
    board = ['#','1','2','3','4','5','6','7','8','9']
    pa = True
    while pa == True:
        print_board(board)
        player_one(board)

        if check_win(board, 'X'):
            print_board(board)
            print('You win!')
            again = input('Play again? (y/n): ')
            while True:
                if again.lower() == 'n':
                    print('Thanks for playing.')
                    pa = False
                    break
                elif again.lower() == 'y':
                    clear(board)
                    break
                else: 
                    print('Please input y or n.')

        if check_win(board, 'O'):
            print_board(board)
            print('You lose!')
            again = input('Play again? (y/n): ')
            while True:
                if again.lower() == 'n':
                    print('Thanks for playing.')
                    pa = False
                    break
                elif again.lower() == 'y':
                    clear(board)
                    break
                else: 
                    print('Please input y or n.')
        if check_tie(board):
            print('Tie.')
            again = input('Play again? (y/n): ')
            while True:
                if again.lower() == 'n':
                    print('Thanks for playing.')
                    pa = False
                    break
                elif again.lower() == 'y':
                    clear(board)
                    break
                else: 
                    print('Please input y or n.')
        comp(board)

else:
    # 2 Players
    board = ['#','1','2','3','4','5','6','7','8','9']
    pa = True
    while pa == True:
        print_board(board)
        player_one(board)
        print_board(board)

        if check_win(board, 'X'):
            print_board(board)
            print('Player one wins!')
            again = input('Play again? (y/n): ')
            while True:
                if again.lower() == 'n':
                    print('Thanks for playing.')
                    pa = False
                    break
                elif again.lower() == 'y':
                    clear(board)
                    break
                else: 
                    print('Please input y or n.')

        if check_win(board, 'O'):
            print_board(board)
            print('Player 2 wins!')
            again = input('Play again? (y/n): ')
            while True:
                if again.lower() == 'n':
                    print('Thanks for playing.')
                    pa = False
                    break
                elif again.lower() == 'y':
                    clear(board)
                    break
                else: 
                    print('Please input y or n.')
        if check_tie(board):
            print('Tie.')
            again = input('Play again? (y/n): ')
            while True:
                if again.lower() == 'n':
                    print('Thanks for playing.')
                    pa = False
                    break
                elif again.lower() == 'y':
                    clear(board)
                    break
                else: 
                    print('Please input y or n.')

        player_two(board)