inp = raw_input  # raw_input for Python 2, input for Python 3

rows, columns = map(int, inp().split())

vertices_reprs = list(range(rows * columns))
vertices_values_board = [list(inp()) for r in range(rows)]

# Union-Find (https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
def find(data, x):
    while x != data[x]:
        x = data[x]
    return x

def union(data, i, j):
    pi = find(data, i)
    pj = find(data, j)
    if pi != pj:
        data[pi] = pj


for row in range(rows):
    for col in range(columns):

        if col < columns - 1 and vertices_values_board[row][col] == vertices_values_board[row][col+1]:
            union(vertices_reprs, row * columns + col, row * columns + (col + 1))

        if row < rows - 1 and vertices_values_board[row][col] == vertices_values_board[row+1][col]:
            union(vertices_reprs, row * columns + col, (row + 1) * columns + col)

for _ in range(int(inp())):
    x1, y1, x2, y2 = map(lambda x: int(x)-1, inp().split())
    if find(vertices_reprs, x1 * columns + y1) == find(vertices_reprs, x2 * columns + y2):
        print('decimal' if vertices_values_board[x1][y1] == '1' else 'binary')
    else:
        print('neither')
