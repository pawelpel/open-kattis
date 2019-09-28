import sys
inp = sys.stdin.readline()
inp = "{0:b}".format(int(inp))
inp = inp[::-1]
print(int(inp, 2))