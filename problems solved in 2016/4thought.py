ile = int(input())
lista = []

for i in range(ile):
    lista.append(int(input()))

znak = ['*', '+', '-', '/']

rownania = []
rozwiazania = []

for i in range(4):
    for j in range(4):
        for k in range(4):
            r = '4 '+znak[i]+' 4 '+znak[j]+' 4 '+znak[k]+' 4'
            l = eval(str(r))
            l = int(l)
            r += ' = '+str(l)

            rownania.append(r)
            rozwiazania.append(l)

for r in rownania:
    print(r, rozwiazania[rownania.index(r)])


# for l in lista:
#     if l in rozwiazania:
#         idx = rozwiazania.index(l)
#         print(rownania[idx])
#     else:
#         print('no solution')