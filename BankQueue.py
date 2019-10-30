import bisect
import operator

N, BANK_TIME = map(int, input().split())

que = {}

for _ in range(N):
    cash, time = map(int, input().split())
    if time in que:
        bisect.insort(que[time], cash)
    else:
        que[time] = [cash]

cash = 0

for _ in range(BANK_TIME):
    keys = que.keys()
    if not keys:
        break

    que_comp = {k: v[-k-1] for k, v in que.items() if len(v) >= k+1}
    if len(que_comp):
        to_pop_key = sorted(que_comp.items(), key=operator.itemgetter(1), reverse=True)[0][0]
        cash += que[to_pop_key].pop()
    else:
        cash += que[min(keys)].pop()

    que = {k-1: v for k, v in que.items() if len(v) and k-1 >= 0}

print(cash)
