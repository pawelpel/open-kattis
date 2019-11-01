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

for t in range(BANK_TIME):
    keys = que.keys()
    if not keys:
        break
    
    # print('T:', BANK_TIME-t)

    que_comp = {}
    for k, v in que.items():
        v_len = len(v)
        
        if k in [0, 1] and v_len >= k + 1:
            que_comp[k] = v[-k-1]
        elif k > 1 and (v_len > k or v_len > BANK_TIME-t):
            que_comp[k] = v[-k]

    # print(que)
    # print(que_comp)

    if len(que_comp):
        to_pop_key = sorted(que_comp.items(), key=operator.itemgetter(1), reverse=True)[0][0]
    else:
        to_pop_key = sorted(que.items(), key=operator.itemgetter(1), reverse=True)[0][0]
        
    # print('Pop:', que[to_pop_key][-1])

    cash += que[to_pop_key].pop()

    que = {k-1: v for k, v in que.items() if len(v) and k-1 >= 0}

print(cash)
