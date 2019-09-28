ile = int(input())
tem = list(map(int, input().split(" ")))
counter = 0
for i in tem:
    if i < 0:
        counter += 1
print(counter)
