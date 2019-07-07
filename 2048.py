raw_board = [input().split(' ') for i in range(4)]
board = [list(map(int, row)) for row in raw_board]

direction = input()

BOARD_SIZE = len(board)


def merge_to_left(array):
    array = list(filter(None, array))  # Delete 0's
    array_len = len(array)
    new_array = []

    skip_next = False
    for i in range(array_len):
        if skip_next:
            skip_next = False
            continue
        if i < array_len-1 and array[i] == array[i+1]:
            new_array.append(array[i]*2)
            skip_next = True
        else:
            new_array.append(array[i])
    return new_array + [0]*(BOARD_SIZE-len(new_array))


if direction == '0':  # Moved left
    for row_no in range(BOARD_SIZE):
        board[row_no] = merge_to_left(board[row_no])

if direction == '2':  # Moved right
    for row_no in range(BOARD_SIZE):
        board[row_no] = merge_to_left(board[row_no][::-1])[::-1]        

if direction == '1':  # Moved up
    for cell in range(BOARD_SIZE):
        array = [board[x][cell] for x in range(BOARD_SIZE)]
        for i, value in enumerate(merge_to_left(array)):
            board[i][cell] = value

if direction == '3':  # Moved down
    for cell in range(BOARD_SIZE):
        array = [board[x-1][cell] for x in range(BOARD_SIZE, 0, -1)]
        for i, value in enumerate(merge_to_left(array)[::-1]):
            board[i][cell] = value

for row in board:
    print(' '.join(map(str, row)))
