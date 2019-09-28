import itertools
liczba = input()
cyferki = list(liczba)
kombinacje = list(itertools.permutations(cyferki))
kombinacje = [int(''.join(k)) for k in kombinacje]
kombinacje.sort()
index = kombinacje.index(int(liczba))
i = 1
while True:
    try:
        if kombinacje[index+i] == int(liczba):
            i += 1
        else:
            print(kombinacje[index+i])
            break
    except IndexError:
         print(0)
         break