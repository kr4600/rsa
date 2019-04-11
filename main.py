from math import ceil, sqrt
from random import choice, randrange

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
print(f'ostatni wyraz w tablicy: {lastTab}')

# sito eratostenesa init
tab = [True] * (lastTab + 1)
tab[0] = False
tab[1] = False
# samo sito
for i in range(2, granica):
    for j in range(i * 2, len(tab), i):
        tab[j] = False


pierwsze = []
for i in range(len(tab) - 1, 2, -1):
    if tab[i] is True and len(pierwsze) < 10:
        print(f'pierwsza: {i}')
        pierwsze.append(i)

p1 = choice(pierwsze)
p2 = choice(pierwsze)

print(f'wylosowane p1: {p1} i p2: {p2}')
