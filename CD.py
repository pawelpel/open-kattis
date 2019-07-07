import sys

while True:

    no_cds_jack, no_cds_jill = tuple(map(int, sys.stdin.readline().split(' ')))

    if no_cds_jack == 0 and no_cds_jill == 0:
        break

    jack_cds = set(sys.stdin.readline() for _ in range(no_cds_jack))
    
    count = 0
    for _ in range(no_cds_jill):
        if sys.stdin.readline() in jack_cds:
            count += 1

    print(count)
