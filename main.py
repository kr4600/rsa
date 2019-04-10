import random as r
from math import ceil, sqrt
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
lastTab = 100
granica = 10
print(lastTab)

#sito eratostenesa init
tab = [True] * (lastTab+1)
tab[0] = False
tab[1] = False
#samo sito
for i in range(2, granica):
    for j in range(i*2,len(tab),i):
        tab[j] = False


for i in range(len(tab)):
  if tab[i]==True:
      print(i)
