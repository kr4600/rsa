from timeit import timeit
from decimal import Decimal, quantize, ROUND_HALF_EVEN


def test(komenda, powtorzenia=10, powtorzeniaTimeIt='pass', startup='pass'):
    time = 0
    if startup == 'pass':
        startup = ''
    for i in range(powtorzenia):
        print(f'{i+1} z {powtorzenia}')
        time += timeit(komenda, number=powtorzeniaTimeIt,
                       setup='from __main__ import ' + komenda[:-2]
                       + startup)
    lap = time / powtorzenia
    print(lap)
    return lap


def procenty(dane1, dane2):
    procent = (1-(dane1/dane2))*100
    decProcent = Decimal(str(procent)).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN)
    print(procent)
    print(f'poprawa o {decProcent}%')

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
    return lTab


def czas2():
    limit = 1000000
    a = [True] * (limit + 1)
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            # yield i
            for n in range(i * i, limit, i):
                a[n] = False
    # dodane do celów testowych
    return a


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
    lLastTab = 1000000
    lTab = [True] * (lLastTab + 1)
    lTab[0] = False
    lTab[1] = False
    lGranica = 1000
    for i in list([2]) + list(range(3, lGranica, 2)):
        if lTab[i]:
            for j in range(i * 2, len(lTab), i):
                lTab[j] = False
    return lTab


def sito():
    print(timeit('czas()', setup='from __main__ import czas', number=10))
    #print(timeit('czas2()', setup='from __main__ import czas2', number=10))
    #print(timeit('czas3()', setup='from __main__ import czas3', number=10))
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


def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):     # Mark factors non-prime
                a[n] = False


if __name__ == '__main__':
    # sito()
    # print('lel')
    # print(len(czas2()))
    # print('heh')
    # print(len(czas()))
    # primes_sieve2(100)
    # mnozenie()
    t1 = test('czas()', 30, 150)
    t2 = test('czas4()', 30, 150)
    procenty(t1, t2)
