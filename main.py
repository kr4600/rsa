from math import ceil, sqrt
from random import choice, randrange


class klucz:
    def __init__(self, l1, l2, *, rodzaj='publiczny'):
        self.p1 = l1
        self.n = l2
        print(f'kucz {rodzaj}: l{l1}, l2{l2}')


def pierwsze(od, do, coIle, **kwargs):
    dlugosc = 10
    pierwsze = []
    for i in range(od, do, coIle):
        if tab[i] is True and len(pierwsze) < dlugosc:
            print(i)
            pierwsze.append(i)
    return pierwsze


def szukanieD(dlugosc=3):
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


'''
while(1):
    # ostatnia pierwsza przed liczbą będzie podana
    liczba = input('podaj liczbe: ')
    try:
        liczba = int(liczba)
        break
    except ValueError:
        print('nie podano liczby')

# ostatni wyraz tablicy
granica = ceil(sqrt(liczba))
lastTab = granica ** 2
'''

lol = 100
liczba = lol
lastTab = int(lol ** 3)
granica = int(sqrt(lol) ** 3)
#   print(f'ostani {lastTab}')

# sito eratostenesa init
tab = [True] * (lastTab + 1)
tab[0] = False
tab[1] = False

# samo sito
# for i in range(2, granica):
for i in list([2]) + list(range(3, granica, 2)):
    # print(i)
    if tab[i]:
        for j in range(i * 2, len(tab), i):
            tab[j] = False

pierwszeP = pierwsze(liczba, 2, -1)
print(f'pierwszeP {pierwszeP}')

p1 = choice(pierwszeP)
pierwszeP.remove(p1)
p2 = choice(pierwszeP)
print(f'{p1} i {p2}')
n = p1 * p2

# wibieranie e
# <max(p1,p2)+1;n-1>
fi = (p1 - 1) * (p2 - 1)
print(f'fi {fi}')
# "len(tab) - 2" bo -1 od długości, i -1 z przedziału
# "max(p1, p2)+2" bo 2 nigdy nie będzie większe, a wszystkieinne pierwsze
# są nieparzyste

# TODO zwiekszy dlugosc (teraz 10)
pierwszeE = pierwsze(max(p1, p2) + 2, len(tab) - 2, 2, dlugosc=20)
print(f'pierwszeE {pierwszeE}')
e = choice(pierwszeE)
print(f'e = {e}')

pierwszeD = szukanieD(5)
d = choice(pierwszeD)
print(f'd = {d}')

k1 = klucz(e, n)
k2 = klucz(d, n, rodzaj='prywatny')
