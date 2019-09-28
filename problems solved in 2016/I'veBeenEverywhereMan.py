ile = int(input())
grupy_miast = []
for i in range(ile):
    ile_miast = int(input())
    miasta = []
    for m in range(ile_miast):
        miasta.append(input())
    grupy_miast.append(miasta)

for g in grupy_miast:
    print(len(set(g)))


