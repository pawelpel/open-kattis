from collections import deque

read_input = input

def input_to_int():
    return map(int, read_input().split())

board_x, board_y = input_to_int()
board = [read_input() for x in range(board_x)]

moves = []
for n in range(int(read_input())):
    x1, y1, x2, y2 = input_to_int()
    moves.append(((x1-1, y1-1), (x2-1, y2-1)))

def get_type_of_person(x, y):
    if board[x][y] == '1':
        return 'decimal', '1'
    return 'binary', '0'

def get_board_value(pos):
    x, y = pos
    if x < 0 or y < 0 or x >= board_x or y >= board_y:
        return
    return board[x][y]

def breadth_first_search(start, finish, person, repr_person):
    visited = set((start,))
    stack = deque((start,))
    while len(stack):
        v = stack.pop()            
        if v == finish:
            return person
        x, y = v
        for direction in sorted(
                [(x, y-1), (x, y+1), (x-1, y), (x+1, y)], 
                key=lambda o: abs(o[0]-finish[0])+abs(o[1]-finish[1]),
                reverse=True,
            ):
            if direction not in visited and get_board_value(direction) == repr_person:
                visited.add(direction)
                stack.append(direction)

def check_move(move):
    if get_board_value(move[0]) != get_board_value(move[1]):
        return 'neither'
    p = get_type_of_person(move[0][0], move[0][1])
    return breadth_first_search(move[0], move[1], p[0], p[1]) or 'neither'

for move in moves:
    print(check_move(move))
