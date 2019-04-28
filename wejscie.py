from prompt_toolkit.validation import Validator
from prompt_toolkit import prompt
from math import ceil, sqrt


def wejscieZKonsoli():

    def is_number(text):
        if text.isdigit():
            if int(text) >= 5:
                return True
        else:
            return False

    validator = Validator.from_callable(
        is_number,
        error_message='Na wejsciu znajduja sie nie tylko cyfry lub liczba < 5',
        move_cursor_to_end=True)

    number = int(prompt('Podaj zakres: ', validator=validator))
    return number


def sprawdzanie(liczbaInput=100):
    global liczba, granica, tab
    liczba = int(liczbaInput)
    if liczba == 0:
        raise ValueError
    # ostatni wyraz tablicy
    granica = ceil(sqrt(liczba))
    # **3 to zwiększenie wielkości tablicy aby móc swobodnie pracowac
    # na liczbach (zwiększa to jednak zużycie ramu)
    lastTab = (granica ** 2) ** 3
    granica **= 3

    # sito eratostenesa init
    tab = [True] * (lastTab + 1)
    tab[0] = False
    tab[1] = False


def main():
    # ostatnia pierwsza przed liczbą będzie podana
    while(1):
        try:
            sprawdzanie(wejscieZKonsoli())
            break
        except MemoryError:
            print('zabrakło pamięci prawdopodobnie podana liczba jest za duża')
        except OverflowError:
            print('liczby za duże żeby wykonać obliczenia')


if __name__ == '__main__':
    main()
