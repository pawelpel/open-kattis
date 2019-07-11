import copy
import sys
sys.setrecursionlimit(2000000000)

N_lines, M_cells = tuple(map(int, input().split(' ')))
board = []

board.append(list(map(int, list('0'*(M_cells+2)))))
for line in range(N_lines):
    board.append(list(map(int, list('0'+input()+'0'))))
board.append(list(map(int, list('0'*(M_cells+2)))))

board_size = len(board), len(board[0])

visited = set()

def mark_sea(row, col):
    if board[row][col] == 1:
        return       
    visited.add((row, col))
    
    if col-1 >= 0 and (row, col-1) not in visited:
        mark_sea(row, col-1)
    if col+1 <= board_size[1]-1 and (row, col+1) not in visited:
        mark_sea(row, col+1)
    if row-1 >= 0 and (row-1, col) not in visited:
        mark_sea(row-1, col)
    if row+1 <= board_size[0]-1 and (row+1, col) not in visited:
        mark_sea(row+1, col)
    return

mark_sea(0, 0)

for v in visited:
    board[v[0]][v[1]] = 'X'

def check_neighbours(row, col):
    neighbours = (
        board[row-1][col],  # top
        board[row+1][col],  # bottom
        board[row][col+1],  # rigth
        board[row][col-1],  # left
    )
    return sum(n == 'X' for n in neighbours)

coast_len = 0
for row_no in range(board_size[0]):
    for col_no in range(board_size[1]):
        if board[row_no][col_no] != 'X':
            coast_len += check_neighbours(row_no, col_no)
            
print(coast_len)