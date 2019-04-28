import wejscie
import fileOperation
from generator import generatorKluczy
from generatorTablicy import genTablicy
from kryotografia import compEnc, compDec

from prompt_toolkit.validation import Validator
from prompt_toolkit import prompt


menuMain = {}
menuMain['1'] = 'Wygeneruj klucze'
menuMain['2'] = 'Wygeneruj tablicę szyfrową'
menuMain['3'] = 'Zaszyfruj tekst'
menuMain['4'] = 'Odszyfruj tekst'
menuMain['5'] = 'Eksportuj'
menuMain['8'] = 'Wyświetl opcje'
menuMain['9'] = 'Wyjście'
optionsMenuMain = menuMain.keys()

menuExport = {}
menuExport['1'] = 'Eksportuj parę kluczy'
menuExport['2'] = 'Eksportuj klucz publiczny'
menuExport['3'] = 'Eksportuj klucz prywatny'
menuExport['7'] = 'Wróć do main menu'
menuExport['8'] = 'Wyświetl opcje'
menuExport['9'] = 'Wyjście'
optionsMenuExport = menuExport.keys()


def printMenu(menu='main', space=2):
    type = ''
    toPrint = ''
    if menu == 'main':
        type = optionsMenuMain
        toPrint = menuMain
    elif menu == 'export':
        type = optionsMenuExport
        toPrint = menuExport

    if space != 0:
        print('\n' * (space - 1))
    for i in type:
        print(f'{i}. {toPrint[i]}')


def wygenerujKlucze():
    global lN, lE, lD, lK1, lK2
    wejscie.main()
    lN, lE, lD, lK1, lK2 = generatorKluczy()


def wygenerujTablice():
    global lEncSymbols, lEncNumbers
    lEncSymbols, lEncNumbers = genTablicy(iloscCyfr=3)


def zakodujTekst():
    pass


def zaszyfrujTekst():
    global szyfrogram

    def isInList(text):
        for i in text:
            if i not in lEncSymbols:
                return False
        return True

    def validInput():
        validator = Validator.from_callable(
            isInList,
            error_message='Znak nie występuje w tablicy szyfrującej',
            move_cursor_to_end=True)

        tekst = prompt('Podaj tekst: ', validator=validator)
        return tekst

    szyfrogram = compEnc(validInput(), lEncSymbols,
                         lEncNumbers, lE, lN)


def odszyfrujTekst():
    global tekstJawny
    tekstJawny = compDec(szyfrogram, lEncSymbols, lEncNumbers, lD, lN)


def zdekodujTekst():
    pass


def export():
    printMenu('export', 1)

    def output(dane):
        fileOperation.export(dane)

    while 1:
        selection = input('|| ')
        if selection == '1':
            output(list([lK1.export(), lK2.export()]))
        elif selection == '2':
            output(list([lK1.export()]))
        elif selection == '3':
            output([list(lK2.export())])
        elif selection == '7':
            printMenu()
            break
        elif selection == '8' or selection == 'menu':
            printMenu('export')
        elif selection == '9' or selection == 'exit':
            quit()
        else:
            print('Zaznaczono nieznaną opcje')

# wejscie.main()


def main():
    # global wygenerujKluczeDone
    wygenerujKluczeDone = False
    wygenerujTabliceDone = False
    zaszyfrujTekstDone = False
    printMenu(space=0)
    while 1:
        selection = input('|| ')
        if selection == '1' or selection == 'gen':
            wygenerujKlucze()
            wygenerujKluczeDone = True

        elif selection == '2' or selection == 'gent':
            wygenerujTablice()
            wygenerujTabliceDone = True

        elif selection == '3' or selection == 'encr':
            if wygenerujKlucze and wygenerujTablice:
                print('do tej czynnosci wymagany jest klucz i tablica')
            else:
                zaszyfrujTekst()
                zaszyfrujTekstDone = True

        elif selection == '4' or selection == 'decr':
            if zaszyfrujTekstDone:
                print('najpierw trzeba cos zaszyfrowac')
            else:
                odszyfrujTekst()

        elif selection == '5' or selection == 'export':
            if wygenerujKlucze:
                print('aby eksportowac, stworz klucze')
            else:
                export()
        elif selection == 'enco':
            pass
        elif selection == 'deco':
            pass
        elif selection == '8' or selection == 'menu':
            printMenu()
        elif selection == '9' or selection == 'exit':
            quit()
        else:
            print('Zaznaczono nieznaną opcje')


if __name__ == '__main__':
    main()
