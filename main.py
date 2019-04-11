from math import ceil, sqrt
from random import choice, randrange

def pierwsze(od, do, coIle, dlugosc):
    pierwsze = []
    for i in range(od, do, coIle):
        if tab[i] is True and len(pierwsze) < dlugosc:
            print(i)
            pierwsze.append(i)
    return pierwsze;
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
liczba = 400
lastTab = int(400*2)
granica = int(20*2)
print(f'ostani {lastTab}')

# sito eratostenesa init
tab = [True] * (lastTab + 1)
tab[0] = False
tab[1] = False
# samo sito
for i in range(2, granica):
    for j in range(i * 2, len(tab), i):
        tab[j] = False

pierwszeP = pierwsze(liczba, 2, -1, 10)
print(pierwszeP)

p1 = choice(pierwszeP)
pierwszeP.remove(p1)
p2 = choice(pierwszeP)
print(f'{p1} i {p2}')
print(f'pierwszeP {pierwszeP}')
n = p1*p2

# wibieranie e
# <max(p1,p2)+1;n-1>
fi = (p1-1)*(p2-1)
print(f'fi {fi}')
# "len(tab) - 2" bo -1 od długości, i -1 z przedziału
# "max(p1, p2)+2" bo 2 nigdy nie będzie większe, a wszystkieinne pierwsze
# są nieparzyste

# TODO zwiekszy dlugosc (teraz 10)
pierwszeE = pierwsze(max(p1, p2)+2, len(tab) - 2, 2, 10)
print(f'pierwszeE {pierwszeE}')
e = choice(pierwszeE)
print(f'e = {e}')
