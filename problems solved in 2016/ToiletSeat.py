preferencje = input()


def seat_up(preferencje):
    changes = 0
    for p in range(len(preferencje)):
        if p == 1:
            continue
        if p == 0:
            if preferencje[0] == 'D' and preferencje[1] == 'U':
                changes += 1
                continue
            if preferencje[0] == 'U' and preferencje[1] == 'D':
                changes += 2
                continue
            if preferencje[0] == 'D' and preferencje[1] == 'D':
                changes += 1
                continue
        if preferencje[p] == 'D':
            changes += 2
    return changes


def seat_down(preferencje):
    changes = 0
    for p in range(len(preferencje)):
        if p == 1:
            continue
        if p == 0:
            if preferencje[0] == 'D' and preferencje[1] == 'U':
                changes += 2
                continue
            if preferencje[0] == 'U' and preferencje[1] == 'D':
                changes += 1
                continue
            if preferencje[0] == 'U' and preferencje[1] == 'U':
                changes += 1
                continue
        if preferencje[p] == 'U':
            changes += 2
    return changes


def seat_like_u_want(preferencje):
    changes = 0
    for p in range(1,len(preferencje)):
        if preferencje[p-1] != preferencje[p]:
            changes += 1
    return changes

print(seat_up(preferencje))
print(seat_down(preferencje))
print(seat_like_u_want(preferencje))