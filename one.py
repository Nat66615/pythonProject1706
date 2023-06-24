import random

board = []
for x in range(5):
    board.append(['0'] * 5)

print(board)


def print_board(board):
    for row in board:
        print(''.join(row))


print('Морской бой')
print_board(board)


def random_row(board):
    return random.randint(0, len(board)-1)


def random_col(board):
    return random.randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

#Основной цикл игры
for turn in range(4):
    print('Ход', turn + 1)
    guess_row = int(input('(0-4)'))
    guess_col = int(input('(0-4)'))


    #Проверка попадания
    if guess_row == ship_row and guess_col == ship_col:
        print('Победа!')
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print('Допустимые значения (0-4)...')
        elif board[guess_row][guess_col] == 'X':
            print('Нельзя!')
        else:
            print('Мимо!')
            board[guess_row][guess_col] = 'X'
            if turn == 3:
                print('Конец игры')
        print_board(board)
