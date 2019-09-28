import sys
numerki = sys.stdin.readlines()
odp = []

for n in numerki:
    l1, l2 = n[:-1].split(" ")
    odp.append(int(l1)-int(l2))

for o in odp:
    if o < 0:
        print(o*-1)
    else:
        print(o)