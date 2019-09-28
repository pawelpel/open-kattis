
chess_board = []
for _ in range(8):
    line = list(input())
    chess_board.append(line)

queens_pos = []
for i in range(len(chess_board)):
    for j in range(len(chess_board[i])):
        if chess_board[i][j] == '*':
            queens_pos.append(str(i)+' '+str(j))


def check_diagonals(x,y):
    # print(x,y)
    # skrajne przydadki
    if x == 0:
        # z gory w prawo
        if y == 0:
            tmpx = x+1
            tmpy = y+1
            for i in range(7):
                if chess_board[tmpx][tmpy] == '*':
                    return 'invalid'
                tmpx += 1
                tmpy += 1
        # z gory w lewo
        elif y == 7:
            tmpx = x+1
            tmpy = y-1
            for i in range(7):
                if chess_board[tmpx][tmpy] == '*':
                    return 'invalid'
                tmpx += 1
                tmpy -= 1
        # z gory w prawo i lewo
        else:
            # prawo
            tmpx = x+1
            tmpy = y+1
            for i in range(7-(y+1)):
                if chess_board[tmpx][tmpy] == '*':
                    return 'invalid'
                tmpx += 1
                tmpy += 1
            # lewo
            tmpx = x+1
            tmpy = y-1
            for i in range(y):
                if chess_board[tmpx][tmpy] == '*':
                    # print('dupa', tmpx, tmpy)
                    return 'invalid'
                tmpx += 1
                tmpy -= 1
    elif x == 7:
        # z dolu w prawo
        if y == 0:
            tmpx = x-1
            tmpy = y+1
            for i in range(7):
                if chess_board[tmpx][tmpy] == '*':
                    return 'invalid'
                tmpx -= 1
                tmpy += 1
        # z dolu w lewo
        elif y == 7:
            tmpx = x-1
            tmpy = y-1
            for i in range(7):
                if chess_board[tmpx][tmpy] == '*':
                    return 'invalid'
                tmpx -= 1
                tmpy -= 1
        # z dolu w prawo i lewo
        else:
            # prawo
            tmpx = x-1
            tmpy = y+1
            for i in range(7-(y+1)):
                if chess_board[tmpx][tmpy] == '*':
                    return 'invalid'
                tmpx -= 1
                tmpy += 1
            # lewo
            tmpx = x-1
            tmpy = y-1
            for i in range(y):
                if chess_board[tmpx][tmpy] == '*':
                    return 'invalid'
                tmpx -= 1
                tmpy -= 1
    # przypadek ze srodka
    else:
        # z gory w prawo
        tmpx = x+1
        tmpy = y+1
        for i in range(7-(y+1)):
            if chess_board[tmpx][tmpy] == '*':
                return 'invalid'
            tmpx += 1
            tmpy += 1
            if tmpx == 8:
                break
        # z gory w lewo
        tmpx = x+1
        tmpy = y-1
        for i in range(y):
            if chess_board[tmpx][tmpy] == '*':
                return 'invalid'
            tmpx += 1
            tmpy -= 1
            if tmpx == 8:
                break
        # prawo
        tmpx = x-1
        tmpy = y+1
        for i in range(7-(y+1)):
            if chess_board[tmpx][tmpy] == '*':
                return 'invalid'
            tmpx -= 1
            tmpy += 1
            if tmpx == -1:
                break
        # lewo
        tmpx = x-1
        tmpy = y-1
        for i in range(y):
            if chess_board[tmpx][tmpy] == '*':
                return 'invalid'
            tmpx -= 1
            tmpy -= 1
            if tmpx == -1:
                break
    return 'valid'


pos_x = []
pos_y = []
odp = 'valid'
for i in range(len(queens_pos)):
    x,y = map(int, queens_pos[i].split(" "))
    odp = check_diagonals(x,y)
    if odp == 'invalid':
        break
    pos_x.append(x)
    pos_y.append(y)

if len(set(pos_x)) != 8:
    odp = 'invalid'

if len(set(pos_x)) != len(pos_x) or len(set(pos_y)) != len(pos_y):
    odp = 'invalid'

print(odp)