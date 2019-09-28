ile = int(input())
queue = list(map(int, input().split(" ")))

counting = []
for i in range(6):
    counting.append(queue.count(i+1))

counting.reverse()

if 1 in counting:
    ktory = 6
    for _ in counting:
        if _ == 1:
            print(queue.index(ktory)+1)
            break
        ktory -= 1
else:
    print('none')