import sys
raw_board = [list(input()) for _ in range(8)]

board = [list(map(lambda x: 0 if x == '.' else 1, b)) for b in raw_board]

BOARD_SIZE = len(board)

def is_valid_array(array):
    if not sum(array) == 1:
        print('invalid')
        sys.exit()

# check horizontal
for row in board:
    is_valid_array(row)

# check vertical
for cell_no in range(BOARD_SIZE):
    is_valid_array([board[x][cell_no] for x in range(BOARD_SIZE)])

def is_diagonal_valid(array):
    if not sum(array) <= 1:
        print('invalid')
        sys.exit()

# check diagonals /
for row_no in range(BOARD_SIZE):
    is_diagonal_valid([board[row_no-i][i] for i in range(row_no+1)])

for cell_no in range(1, BOARD_SIZE):
    is_diagonal_valid([board[BOARD_SIZE-1-i][cell_no+i] for i in range(BOARD_SIZE-cell_no)])

# check diagonals \
for row_no in range(BOARD_SIZE-1, -1, -1):
    is_diagonal_valid([board[row_no+i][i] for i in range(BOARD_SIZE-row_no)])

for cell_no in range(1, BOARD_SIZE):
    is_diagonal_valid([board[i][cell_no+i] for i in range(BOARD_SIZE-cell_no)])

print('valid')
