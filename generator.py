from secrets import choice
import wejscie


class klucz:
    def __init__(self, l1, l2, name, *, rodzaj='publiczny'):
        self.name = name
        self.p1 = l1
        self.n = l2
        print(f'klucz {rodzaj}: {l1}, {l2}')

    #funkcja bezposrednio do exportu
    def export(self):
        return list([self.name, self.p1, self.n])

# zwraca pewna ilosc liczb z podanego przydzialu
def pierwsze(od, do, coIle, tab, dlugosc=10):
    pierwsze = []
    for i in range(od, do, coIle):
        if tab[i] is True and len(pierwsze) < dlugosc:
            pierwsze.append(i)
    return pierwsze


def szukanieD(tab, dlugosc=3):
    x = 3
    lista = []
    while len(lista) < dlugosc:
        if tab[x]:
            if (x * e) % fi == 1:
                lista.append(x)
        x += 2
    return lista


def generatorKluczy():
    lLiczba = wejscie.liczba
    lGranica = wejscie.granica
    lTab = wejscie.tab
    global n, e, fi, d, k1, k2
    # samo sito
    for i in list([2]) + list(range(3, lGranica, 2)):
        if lTab[i]:
            for j in range(i * 2, len(lTab), i):
                lTab[j] = False

    pierwszeP = pierwsze(lLiczba + 5, 1, -1, lTab)
    while(1):
        pierwszePBak = pierwszeP
        p1 = choice(pierwszePBak)
        pierwszePBak.remove(p1)
        p2 = choice(pierwszePBak)
        n = p1 * p2
        if n >= 10:
            break

    print(f'p1 {p1} \np2 {p2}')
    print(f'n {n}')

    # wibieranie e
    fi = (p1 - 1) * (p2 - 1)
    print(f'fi {fi}')

    pierwszeE = pierwsze(max(p1, p2) + 2, len(lTab) - 2, 2, lTab, dlugosc=12)
    e = choice(pierwszeE)
    print(f'e {e}')

    pierwszeD = szukanieD(lTab, 5)
    d = choice(pierwszeD)
    print(f'd {d}')

    k1 = klucz(e, n, 'k1')
    k2 = klucz(d, n, 'k2', rodzaj='prywatny')

    return n, e, d, k1, k2


def main():
    wejscie.sprawdzanie()
    generatorKluczy()


if __name__ == '__main__':
    main()
