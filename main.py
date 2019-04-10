import random as r
from math import ceil, sqrt

while(1):
    # ostatnia pierwsza przed liczbą będzie podana
    liczba = input('podaj liczbe: ')
    try:
        liczba = int(liczba)
        break
    except ValueError:
        print('nie podano liczby')

# ostatni wyraz tablicy
lastTab = ceil(sqrt(liczba)) ** 2
print(lastTab)
