from random import choice

import wejscie


class klucz:
    def __init__(self, l1, l2, *, rodzaj='publiczny'):
        self.p1 = l1
        self.n = l2
        print(f'kucz {rodzaj}: l{l1}, l2{l2}')


def pierwsze(od, do, coIle, tab, dlugosc=10):
    pierwsze = []
    for i in range(od, do, coIle):
        if tab[i] is True and len(pierwsze) < dlugosc:
            pierwsze.append(i)
    return pierwsze


def szukanieD(tab, dlugosc=3):
    # wyznaczanie d
    # x = 3 dla przyspieszenia procesu
    x = 3
    lista = []
    while len(lista) < dlugosc:
        if tab[x]:
            if (x * e) % fi == 1:
                print(f'{x} = 1')
                lista.append(x)
        x += 2
    return lista


def generatorKluczy():
    # kącik globali
    lLiczba = wejscie.liczba
    lGranica = wejscie.granica
    lTab = wejscie.tab
    global n, e, fi, d, k1, k2
    # samo sito
    # for i in range(2, granica):
    for i in list([2]) + list(range(3, lGranica, 2)):
        if lTab[i]:
            for j in range(i * 2, len(lTab), i):
                lTab[j] = False

    pierwszeP = pierwsze(lLiczba, 2, -1, lTab)
    p1 = choice(pierwszeP)
    pierwszeP.remove(p1)
    p2 = choice(pierwszeP)
    print(f'p1 {p1} \np2 {p2}')
    n = p1 * p2
    print(f'n {n}')

    # wibieranie e
    fi = (p1 - 1) * (p2 - 1)
    print(f'fi {fi}')

    # TODO zwiekszy dlugosc (teraz 10)
    pierwszeE = pierwsze(max(p1, p2) + 2, len(lTab) - 2, 2, lTab, dlugosc=12)
    print(f'pierwszeE {pierwszeE}')
    e = choice(pierwszeE)
    print(f'e = {e}')

    pierwszeD = szukanieD(lTab, 5)
    d = choice(pierwszeD)
    print(f'd = {d}')

    k1 = klucz(e, n)
    k2 = klucz(d, n, rodzaj='prywatny')


def main():
    wejscie.sprawdzanie()
    generatorKluczy()


if __name__ == '__main__':
    main()
