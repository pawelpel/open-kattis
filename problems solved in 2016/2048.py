LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
SIZE = 4


def scan_input():
    tab = []
    for y in range(SIZE):
        tmp = input().split(" ")
        tab.append([int(str(x)) for x in tmp])
    move = input()
    return tab, move


# LEFT
def move0(tab):
    for y in range(SIZE):
        """OPERATION ON ROW"""
        for x in range(SIZE):
            i = 1
            while True:
                if x+i > 3:
                    break
                if tab[y][x] == tab[y][x+i]:
                    tab[y][x] += tab[y][x+i]
                    tab[y][x+i] = 0
                    break
                if tab[y][x+i] == 0:
                    i += 1
                else:
                    break
        for x in range(SIZE):
            if x == SIZE-1:
                break
            i = 1
            while True:
                if x+i > 3:
                    break
                if tab[y][x] == 0:
                    tab[y][x] = tab[y][x+i]
                    tab[y][x+i] = 0
                    i += 1
                else:
                    i += 1
                    break
    return tab


# UP
def move1(tab):
    for x in range(SIZE):
        """OPERATION ON ROW"""
        for y in range(SIZE):
            i = 1
            while True:
                if y+i > 3:
                    break
                if tab[y][x] == tab[y+i][x]:
                    tab[y][x] += tab[y+i][x]
                    tab[y+i][x] = 0
                    break
                if tab[y+i][x] == 0:
                    i += 1
                else:
                    break
        for y in range(SIZE):
            if y == SIZE-1:
                break
            i = 1
            while True:
                if y+i > 3:
                    break
                if tab[y][x] == 0:
                    tab[y][x] = tab[y+i][x]
                    tab[y+i][x] = 0
                    i += 1
                else:
                    i += 1
                    break
    return tab


# RIGHT
def move2(tab):
    for y in range(SIZE):
        """OPERATION ON ROW"""
        for x in range(SIZE-1, -1, -1):
            i = 1
            while True:
                if x-i < 0:
                    break
                if tab[y][x] == tab[y][x-i]:
                    tab[y][x] += tab[y][x-i]
                    tab[y][x-i] = 0
                    break
                if tab[y][x-i] == 0:
                    i += 1
                else:
                    break
        for x in range(SIZE-1, -1, -1):
            if x == 0:
                break
            i = 1
            while True:
                if x-i < 0:
                    break
                if tab[y][x] == 0:
                    tab[y][x] = tab[y][x-i]
                    tab[y][x-i] = 0
                    i += 1
                else:
                    i += 1
                    break
    return tab


# DOWN
def move3(tab):
    for x in range(SIZE):
        """OPERATION ON ROW"""
        for y in range(SIZE-1, -1, -1):
            i = 1
            while True:
                if y-i < 0:
                    break
                if tab[y][x] == tab[y-i][x]:
                    tab[y][x] += tab[y-i][x]
                    tab[y-i][x] = 0
                    break
                if tab[y-i][x] == 0:
                    i += 1
                else:
                    break
        for y in range(SIZE-1, -1, -1):
            if y == 0:
                break
            i = 1
            while True:
                if y-i < 0:
                    break
                if tab[y][x] == 0:
                    tab[y][x] = tab[y-i][x]
                    tab[y-i][x] = 0
                    i += 1
                else:
                    i += 1
                    break
    return tab


def select_move(move, tab):
    tab_1 = None
    if move == '0':
        tab_1 = move0(tab)
    if move == '1':
        tab_1 = move1(tab)
    if move == '2':
        tab_1 = move2(tab)
    if move == '3':
        tab_1 = move3(tab)
    return tab_1


def main():
    tab, move = scan_input()
    tab = select_move(move, tab)
    for y in range(len(tab)):
        for x in range(len(tab)):
            print(tab[y][x], end=' ')
        print()

main()
