list_of_lists = []
while True:
    ile = int(input())
    if ile == -1:
        break
    lista = []
    for i in range(ile):
        lista.append(input())
    list_of_lists.append(lista)

sumy = []

for ll in list_of_lists:
    suma = []
    for l in range(len(ll)):
        miles, hours = ll[l].split(" ")
        miles, hours = int(miles), int(hours)

        if l == 0:
            suma.append(miles*hours)
        else:
            suma.append(miles*(hours - int(ll[l-1].split(" ")[1])))

    sumy.append(suma)

for s in sumy:
    print(str(sum(s))+' miles')