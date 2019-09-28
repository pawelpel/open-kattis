import sys
import threading


def read_map():

    visited = []
    height, width = map(int, input().split(" "))
    mapa = [list(' ' * (width + 2))]
    visited .append(['False' for _ in range(width+2)])
    for _ in range(height):
        roww = input()
        mapa.append(list(' '+roww+' '))
        visited.append(['False' for _ in range(width+2)])
    mapa.append(list(' '*(width+2)))
    visited.append(['False' for _ in range(width+2)])
    return mapa, height, width, visited


def coast_length(mapa, height, width, visited):
    zero, jeden, x = ['0', '1', ' ']


    def check_sea(h, w):
        if visited[h][w] == 'False':
            if mapa[h][w] == zero or mapa[h][w] == x:
                    mapa[h][w] = x
                    visited[h][w] = 'True'
                    if h == 0:
                        if w == 0:
                            check_sea(h, w+1)
                            check_sea(h+1, w)
                        elif w == width:
                            check_sea(h+1, w)
                            check_sea(h, w-1)
                        else:
                            check_sea(h, w-1)
                            check_sea(h, w+1)
                            check_sea(h+1, w)
                    elif h == height+1:
                        if w == 0:
                            check_sea(h, w+1)
                            check_sea(h-1, w)
                        elif w == width:
                            check_sea(h, w-1)
                            check_sea(h-1, w)
                        else:
                            check_sea(h-1, w)
                            check_sea(h, w-1)
                            check_sea(h, w+1)
                    else:
                        try:
                            check_sea(h+1, w)
                        except IndexError:
                            pass
                        try:
                            check_sea(h-1, w)
                        except IndexError:
                            pass
                        try:
                            check_sea(h, w+1)
                        except IndexError:
                            pass
                        try:
                            check_sea(h, w-1)
                        except IndexError:
                            pass

    check_sea(0, 0)

    counter = 0
    for h in range(1, height+1):
        for w in range(1, width+1):
            if mapa[h][w] == jeden:
                if h == 1:
                    if w == 1:
                        counter += 2
                        if mapa[h + 1][w] == x:
                            counter += 1
                        if mapa[h][w + 1] == x:
                            counter += 1
                    elif w == width:
                        counter += 2
                        if mapa[h + 1][w] == x:
                            counter += 1
                        if mapa[h][w - 1] == x:
                            counter += 1
                    else:
                        counter += 1
                        if mapa[h + 1][w] == x:
                            counter += 1
                        if mapa[h][w + 1] == x:
                            counter += 1
                        if mapa[h][w - 1] == x:
                            counter += 1
                elif h == height:
                    if w == 0:
                        counter += 2
                        if mapa[h - 1][w] == x:
                            counter += 1
                        if mapa[h][w + 1] == x:
                            counter += 1
                    elif w == width:
                        counter += 2
                        if mapa[h - 1][w] == x:
                            counter += 1
                        if mapa[h][w - 1] == x:
                            counter += 1
                    else:
                        counter += 1
                        if mapa[h - 1][w] == x:
                            counter += 1
                        if mapa[h][w + 1] == x:
                            counter += 1
                        if mapa[h][w - 1] == x:
                            counter += 1
                else:
                    if w == 0:
                        counter += 1
                        if mapa[h - 1][w] == x:
                            counter += 1
                        if mapa[h][w + 1] == x:
                            counter += 1
                        if mapa[h + 1][w] == x:
                            counter += 1
                    elif w == width:
                        counter += 1
                        if mapa[h - 1][w] == x:
                            counter += 1
                        if mapa[h][w - 1] == x:
                            counter += 1
                        if mapa[h + 1][w] == x:
                            counter += 1
                    else:
                        if mapa[h - 1][w] == x:
                            counter += 1
                        if mapa[h][w - 1] == x:
                            counter += 1
                        if mapa[h + 1][w] == x:
                            counter += 1
                        if mapa[h][w + 1] == x:
                            counter += 1
    print(counter)


def main():
    mapa_, height_, width_, visited_ = read_map()
    coast_length(mapa_, height_, width_, visited_)


if __name__ == "__main__":
    sys.setrecursionlimit(2000000000)
    threading.stack_size(259999999)
    thread = threading.Thread(target=main)
    thread.start()