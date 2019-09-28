wyniki = []
for i in range(5):
    oceny = input().split(" ")
    oceny = [int(o) for o in oceny]
    wyniki.append(sum(oceny))

for w in range(len(wyniki)):
    if wyniki[w] == max(wyniki):
        print(w+1, wyniki[w])