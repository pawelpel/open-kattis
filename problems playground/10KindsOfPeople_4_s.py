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

def get_board_value(x, y):
    if x < 0 or y < 0 or x >= board_x or y >= board_y:
        return
    return board[x][y]

zones = {
    '0': [],
    '1': [],
}

def build_zones():
    visited = set()

    for row in range(board_x):
        for column in range(board_y):
            if (row, column) in visited:
                continue

            zone = set()

            def breadth_first_walk(start, repr_person):
                visited.add(start)
                zone.add(start)
                stack = deque((start,))
                while len(stack):
                    x, y = stack.pop()
                    for direction in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
                        if direction not in visited and get_board_value(*direction) == repr_person:
                            visited.add(direction)
                            zone.add(direction)
                            stack.append(direction)

            repr_person = get_board_value(row, column)            
            breadth_first_walk((row, column), repr_person)            
            zones[repr_person].append(zone)

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
