from timeit import timeit


def czas():
    lLastTab = 1000000
    lTab = [True] * (lLastTab + 1)
    lTab[0] = False
    lTab[1] = False
    lGranica = 1000
    for i in list([2]) + list(range(3, lGranica, 2)):
        if lTab[i]:
            for j in range(i * i, len(lTab), i):
                lTab[j] = False


def czas2():
    lLastTab = 1000000
    lTab = [True] * (lLastTab + 1)
    lTab[0] = False
    lTab[1] = False
    lGranica = 1000
    for i in list([2]) + list(range(3, lGranica, 2)):
        if lTab[i]:
            for j in range(i ** 2, len(lTab), i):
                lTab[j] = False


def czas3():
    from numpy import ones, arange, int16, int32
    lLastTab = 1000000
    lTab = ones((lLastTab + 1), dtype=bool)
    lTab[0] = False
    lTab[1] = False
    lGranica = 1000
    for i in list([2]) + arange(3, lGranica, 2, dtype=int16):
        for j in arange(i * i, len(lTab), i, dtype=int32):
            lTab[j] = False


def czas4():
    from numpy import ones
    lLastTab = 1000000
    lTab = ones((lLastTab + 1), dtype=bool)
    lTab[0] = False
    lTab[1] = False
    lGranica = 1000
    for i in list([2]) + list(range(3, lGranica, 2)):
        for j in range(i ** 2, len(lTab), i):
            lTab[j] = False


def sito():
    print(timeit('czas()', setup='from __main__ import czas', number=10))
    print(timeit('czas2()', setup='from __main__ import czas2', number=10))
    print(timeit('czas3()', setup='from __main__ import czas3', number=10))
    print(timeit('czas4()', setup='from __main__ import czas4', number=10))


def mnozenie():
    powtorzenia = 1000
    numb = 1000
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    for i in range(powtorzenia):
        x += timeit('(i * i for i in range(1000000000000000000000000000))',
                    number=numb)
        y += timeit('(i ** 2 for i in range(1000000000000000000000000000))',
                    number=numb)
        x2 += timeit('(i * i for i in range(1000000000000000000000000000))',
                     number=numb)
        y2 += timeit('(i ** 2 for i in range(1000000000000000000000000000))',
                     number=numb)
    print(x / powtorzenia)
    print(y / powtorzenia)
    print(x2 / powtorzenia)
    print(y2 / powtorzenia)


if __name__ == '__main__':
    sito()
    #mnozenie()
