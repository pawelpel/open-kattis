import sys
import bisect

N, T = map(int, sys.stdin.readline().replace('\n', '').split())

que = {}

for _ in range(N):
    cash, time = sys.stdin.readline().replace('\n', '').split()
    cash = int(cash)
    if time in que:
        que[time].append(cash)
    else:
        que[time] = [cash]

cash = 0
que_line = []

for time in range(T, -1, -1):
    time = str(time)
    
    if time in que:
        for person in que[time]:
            bisect.insort(que_line, person)
    
    if len(que_line):
        cash += que_line.pop()

print(cash)
