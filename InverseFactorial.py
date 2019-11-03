import sys
import math

fac = sys.stdin.readline().replace('\n', '')
fac_len = len(fac)

if fac_len < 4:
    x = 1
    while 1:
        if math.factorial(x) == int(fac):
            print(x)
            break
        x += 1
else:
    result = 0
    x = 1
    while 1:
        result += math.log10(x)
        if math.floor(result) + 1 == fac_len:
            print(x)
            break
        x += 1
