from math import ceil, sqrt
from random import choice, randrange


def pierwsze(od, do, coIle, dlugosc):
    pierwsze = []
    for i in range(od, do, coIle):
        if tab[i] is True and len(pierwsze) < dlugosc:
            pierwsze.append(i)
    return pierwsze


while(1):
    # ostatnia pierwsza przed liczbą będzie podana
    liczba = input('podaj liczbe: ')
    try:
        liczba = int(liczba)
        break
    except ValueError:
        print('nie podano liczby')

# ostatni wyraz tablicy
granica = ceil(sqrt(liczba))**3
lastTab = (granica ** 3)

print(f'ostatni wyraz w tablicy: {lastTab}')

# sito eratostenesa init
tab = [True] * (lastTab + 1)
tab[0] = False
tab[1] = False

# samo sito
pierwszeMain = []
for i in range(2, granica):
    if tab[i]:
        for j in range(i * 2, len(tab), i):
            tab[j] = False
print(f'pierwsze main: {pierwszeMain}')

pierwszeP = pierwsze(liczba, 2, -1, 10)
print(f'pierwszeP {pierwszeP}')

p1 = choice(pierwszeP)
pierwszeP.remove(p1)
p2 = choice(pierwszeP)
print(f'{p1} i {p2}')
n = p1 * p2
print(f'n {n}')

# wibieranie e
fi = (p1 - 1) * (p2 - 1)
print(f'fi {fi}')

# TODO zwiekszy dlugosc (teraz 10)
pierwszeE = pierwsze(max(p1, p2) + 2, len(tab) - 2, 2, 10)
print(f'pierwszeE {pierwszeE}')
e = choice(pierwszeE)
print(f'e = {e}')

# wyznaczanie d
# x = 3 dla przyspieszenia procesu
x = 3
pierwszeD = []
while len(pierwszeD) < 5:
    if tab[x]:
        if (x * e) % fi == 1:
            print(f'{x} = 1')
            pierwszeD.append(x)
    x += 2
d = choice(pierwszeD)
print(f'd = {d}')
