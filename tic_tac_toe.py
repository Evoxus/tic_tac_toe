board = []
x_win = False
o_win = False
cats_game = False
replay_response_check = ['y', 'yeah', 'yes', 'yea']
X_row = 0
X_col = 0
O_row = 0
O_col = 0

for x in range(3):
    board.append(['__'] * 3)

def display_board():
    for row in board:
        print ('|'.join(row))

def reset_board():
    for lst in board:
        for i in range(3):
            lst[i] = '__'

def X_input_row():
    global X_row
    while True:
        X_row = int(input('X, enter 1-3 for your row: ')) - 1
        if X_row >= 3 or X_row < 0:
             print ("That row doesn't exist. Please enter a number between 1 and 3.")
        else:
             break
    return X_row

def X_input_col():
    global X_col
    while True:
        X_col = int(input('X, enter 1-3 for your column: ')) - 1
        if X_col >= 3 or X_col < 0:
             print ("That column doesn't exist. Please enter a number between 1 and 3.")
        else:
             break
    return X_col

def O_input_row():
    global O_row
    while True:
        O_row = int(input('O, enter 1-3 for your row: ')) - 1
        if O_row >= 3 or O_row < 0:
             print ("That row doesn't exist. Please enter a number between 1 and 3.")
        else:
             break
    return O_row

def O_input_col():
    global O_col
    while True:
        O_col = int(input('O, enter 1-3 for your column: ')) - 1
        if O_col >= 3 or O_col < 0:
             print ("That column doesn't exist. Please enter a number between 1 and 3.")
        else:
             break
    return O_col

def check_board():
    global x_win
    global o_win
    global cats_game
    if 'X' == board[0][0] and 'X' == board[0][1] and 'X' == board[0][2]:
        x_win = True
        return True
    elif 'X' == board[1][0] and 'X' == board[1][1] and 'X' == board[1][2]:
        x_win = True
        return True
    elif 'X' == board[2][0] and 'X' == board[2][1] and 'X' == board[2][2]:
        x_win = True
        return True
    elif 'X' == board[0][0] and 'X' == board[1][0] and 'X' == board[2][0]:
        x_win = True
        return True
    elif 'X' == board[0][1] and 'X' == board[1][1] and 'X' == board[2][1]:
        x_win = True
        return True
    elif 'X' == board[0][2] and 'X' == board[1][2] and 'X' == board[2][2]:
        x_win = True
        return True
    elif 'X' == board[0][0] and 'X' == board[1][1] and 'X' == board[2][2]:
        x_win = True
        return True
    elif 'X' == board[0][2] and 'X' == board[1][1] and 'X' == board[2][0]:
        x_win = True
        return True
    elif 'O' == board[0][0] and 'O' == board[0][1] and 'O' == board[0][2]:
        o_win = True
        return True
    elif 'O' == board[1][0] and 'O' == board[1][1] and 'O' == board[1][2]:
        o_win = True
        return True
    elif 'O' == board[2][0] and 'O' == board[2][1] and 'O' == board[2][2]:
        o_win = True
        return True
    elif 'O' == board[0][0] and 'O' == board[1][0] and 'O' == board[2][0]:
        o_win = True
        return True
    elif 'O' == board[0][1] and 'O' == board[1][1] and 'O' == board[2][1]:
        o_win = True
        return True
    elif 'O' == board[0][2] and 'O' == board[1][2] and 'O' == board[2][2]:
        o_win = True
        return True
    elif 'O' == board[0][0] and 'O' == board[1][1]and 'O' == board[2][2]:
        o_win = True
        return True
    elif 'O' == board[0][2] and 'O' == board[1][1] and 'O' == board[2][0]:
        o_win = True
        return True
    elif ('__') not in board[0] and ('__') not in board[1] and ('__') not in board[2]:
        cats_game = True
        return True
    else:
        return False

def main():
    print(' ')
    print("Let's play Tic Tac Toe!")
    print(' ')
    display_board()
    while check_board() != True:
        if check_board() != True:
            print(' ')
            print("X's turn.")
            print(' ')
            X_input_row()
            X_input_col()
            if board[X_row][X_col] != '__':
                while True:
                    if board[X_row][X_col] == '__':
                         board[X_row][X_col] = 'X'
                         break
                    else:
                         print ('  ')
                         print ('That space is taken!')
                         print(' ')
                         X_input_row()
                         X_input_col()
            else:
                board[X_row][X_col] = 'X'
            print (' ')
            display_board()
            if check_board() and x_win:
                print(' ')
                print ('Congratulations X, you win!')
                break
            elif check_board() and cats_game:
                print(' ')
                print('Cats game!')
                break
            if check_board() != True:
                print(' ')
                print("O's turn.")
                print(' ')
                O_input_row()
                O_input_col()
                if board[O_row][O_col] != '__':
                    while True:
                        if board[O_row][O_col] == '__':
                             board[O_row][O_col] = 'O'
                             break
                        else:
                             print ('  ')
                             print ('That space is taken!')
                             print (' ')
                             O_input_row()
                             O_input_col()
                else:
                    board[O_row][O_col] = 'O'
                print (' ')
                display_board()
                if check_board() and o_win:
                    print(' ')
                    print ('Congratulations O, you win!')
                    break
                elif check_board() and cats_game:
                    print(' ')
                    print('Cats game!')
                    break
    print(' ')
    replay = input('Would you like to play again (Y/N): ')
    if replay.lower() in replay_response_check:
        reset_board()
        main()
    else:
        print(' ')
        print('Hope to see you again soon.')

main()
