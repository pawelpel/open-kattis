ile = int(input())
no = []
for i in range(ile):
    no.append(int(input()))

for n in no:
    if n % 2 == 0:
        print(str(n)+' is even')
    else:
        print(str(n)+' is odd')

