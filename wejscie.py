from prompt_toolkit.validation import Validator
from prompt_toolkit import prompt
from math import ceil, sqrt


def wejscieZKonsoli():

    def is_number(text):
        if text.isdigit():
            if int(text) >= 5:
                return True
            return True
        else:
            return False

    validator = Validator.from_callable(
        is_number,
        error_message='Na wejsciu nie znajdują sie tylko cyfry',
        move_cursor_to_end=True)

    print('Liczba powinna mieścić w zakresie <5;100>')
    print('Zwiększenie znacząco wydłuży czas generowania')
    number = int(prompt('Podaj zakres: ', validator=validator))
    return number


def sprawdzanie(liczbaInput=100):
    global liczba, granica, tab
    if liczbaInput < 5:
        print('liczba jest mniejsza niż 5, zmienianie na minimalną')
        liczbaInput = 5
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
        except MemoryError:
            print('zabrakło pamięci prawdopodobnie podana liczba jest za duża')
        except OverflowError:
            print('liczby za duże żeby wykonać obliczenia')


if __name__ == '__main__':
    main()
