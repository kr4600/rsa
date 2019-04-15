from math import ceil, sqrt


def wejscieZKonsoli():
    return input('podaj liczbę: ')


def sprawdzanie(liczbaInput=100):
    global liczba, granica, tab
    liczba = int(liczbaInput)
    if liczba == 0:
        raise ValueError
    granica = ceil(sqrt(liczba))
    lastTab = (granica ** 2) ** 3
    granica **= 3

    # sito eratostenesa init
    tab = [True] * (lastTab + 1)
    tab[0] = False
    tab[1] = False


def main():
    while(1):
        try:
            sprawdzanie(wejscieZKonsoli())
            break
        except ValueError:
            print('podana wartość jest niepoprawna')
        except MemoryError:
            print('zabrakło pamięci prawdopodobnie podana liczba jest za duża')
        except OverflowError:
            print('liczby za duże żeby wykonać obliczenia')


if __name__ == '__main__':
    main()
