liczby = []
while True:
    no = input()
    if no == '0 0':
        break
    else:
        x, y = no.split(" ")
        x, y = int(x), int(y)
    liczby.append([x,y])

for l in liczby:
    print(str(l[0]//l[1])+' '+str(l[0]%l[1])+' / '+str(l[1]))