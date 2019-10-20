import sys
import math
from collections import namedtuple

sys.setrecursionlimit(2000000000)

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

def calculate_distance(x1, y1, x2, y2):
   return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

Direction = namedtuple('Direction', 'name x y distance')

def check_move(move):
    x1, y1 = move[0]  # Start
    x2, y2 = move[1]  # Finish

    person, repr_person = get_type_of_person(x2, y2)

    visited = set()

    def walk(x, y):
        if (x, y) == (x2, y2):
            raise Exception(person)

        if (x, y) in visited:
            return
        
        visited.add((x, y))

        directions = [
            Direction('left', x, y-1, calculate_distance(x, y-1, x2, y2)),
            Direction('right', x, y+1, calculate_distance(x, y+1, x2, y2)),
            Direction('up', x-1, y, calculate_distance(x-1, y, x2, y2)),
            Direction('down', x+1, y, calculate_distance(x+1, y, x2, y2)),
        ]

        for direction in sorted(directions, key=lambda x: x.distance, reverse=True):
            if get_board_value(direction.x, direction.y) == repr_person:
                walk(direction.x, direction.y)

    try:
        walk(x1, y1)
    except Exception as e:
        return e
    return 'neither'

for move in moves:
    print(check_move(move))
