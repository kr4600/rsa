from secrets import choice

import wejscie


class klucz:
    def __init__(self, l1, l2, name, *, rodzaj='publiczny'):
        # name potrzebne było do łatwiejszego eksportu
        self.name = name
        self.p1 = l1
        self.n = l2
        print(f'klucz {rodzaj}: {l1}, {l2}')

    def export(self):
        return list([self.name, self.p1, self.n])


def pierwsze(od, do, coIle, tab, dlugosc=10):
    pierwsze = []
    for i in range(od, do, coIle):
        if tab[i] is True and len(pierwsze) < dlugosc:
            # print(i)
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

    # liczba +5 żeby mie pewnoc że bdzie wystarczająco liczb
    # aby n było wiesksze od 10
    pierwszeP = pierwsze(lLiczba + 5, 1, -1, lTab)
    # print(pierwszeP)
    while(1):
        pierwszePBak = pierwszeP
        p1 = choice(pierwszePBak)
        # print(p1)
        pierwszePBak.remove(p1)
        p2 = choice(pierwszePBak)
        # print(p2)
        n = p1 * p2
        if n >= 10:
            break

    print(f'p1 {p1} \np2 {p2}')
    print(f'n {n}')

    # wibieranie e
    # <max(p1,p2)+1;n-1>
    fi = (p1 - 1) * (p2 - 1)
    print(f'fi {fi}')

    # TODO zwiekszy dlugosc (teraz 10)
    pierwszeE = pierwsze(max(p1, p2) + 2, len(lTab) - 2, 2, lTab, dlugosc=12)
    # "len(tab) + 2" bo +1 od długości, i +1 z przedziału
    # "max(p1, p2)+2" bo 2 nigdy nie będzie większe, a wszystkieinne pierwsze
    # są nieparzyste
    print(f'pierwszeE {pierwszeE}')
    e = choice(pierwszeE)
    print(f'e = {e}')

    pierwszeD = szukanieD(lTab, 5)
    d = choice(pierwszeD)
    print(f'd = {d}')

    k1 = klucz(e, n, 'k1')
    k2 = klucz(d, n, 'k2', rodzaj='prywatny')

    return n, e, d


def main():
    wejscie.sprawdzanie()
    generatorKluczy()


if __name__ == '__main__':
    main()
