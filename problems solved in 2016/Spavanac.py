H, M = input().split(" ")
H, M = int(H), int(M)
Ho = [n for n in range(0,23)]
Mi = [n for n in range(0,59)]

if H == 0:
    if M >= 45:
        print(H, M-45)
    else:
        print(23, 60+(M-45))
else:
    if M >= 45:
        print(H, M-45)
    else:
        print(H-1, 60+(M-45))