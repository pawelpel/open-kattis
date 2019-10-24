import sys
from functools import lru_cache
sys.setrecursionlimit(2000000)

def read_input():
    return sys.stdin.readline().replace('\n','')

def input_to_int_tuple(separator=' '):
    return tuple(map(int, read_input().split(separator)))

board_x, board_y = input_to_int_tuple()

board = []
for x in range(board_x):
    board.append(list(map(int, list(read_input()))))

number_of_moves = int(read_input())
moves = []
for n in range(number_of_moves):
    x1, y1, x2, y2 = input_to_int_tuple()
    moves.append(((x1-1, y1-1), (x2-1, y2-1)))


def get_type_of_person(x, y):
    if board[x][y]:
        return 'decimal', 1
    return 'binary', 0

def get_board_value(x, y):
    if x < 0 or y < 0 or x >= board_x or y >= board_y:
        return
    return board[x][y]

zones = {
    0: [],
    1: [],
}

def build_zones():
    visited = set()

    for row in range(board_x):
        for column in range(board_y):
            if (row, column) in visited:
                continue
            else:
                zone = set()

                @lru_cache(maxsize=None)
                def walk(x, y, group_type):
                    if (x, y) in visited or get_board_value(x, y) != group_type:
                        return
                    visited.add((x, y))

                    zone.add((x, y))

                    directions = [
                        (x, y-1),
                        (x, y+1),
                        (x-1, y),
                        (x+1, y),
                    ]

                    for direction in directions:
                        walk(direction[0], direction[1], group_type)

                walk(row, column, get_board_value(row, column))

                zones[get_board_value(row, column)].append(zone)

build_zones()


def check_move(move):
    x1, y1 = move[0]  # Start
    x2, y2 = move[1]  # Finish

    person, repr_person = get_type_of_person(x1, y1)

    for zone in zones[repr_person]:
        if (x1, y1) in zone and (x2, y2) in zone:
            return person
    return 'neither'

for move in moves:
    print(check_move(move))
