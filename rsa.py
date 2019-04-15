import wejscie
from generator import generatorKluczy
from generatorTablicy import genTablicy
from kryotografia import compEnc, compDec
import fileOperation

# wejscie.main()


def main():
    wejscie.sprawdzanie()
    lN, lE, lD = generatorKluczy()
    lEncSymbols, lEncNumbers = genTablicy(iloscCyfr=3)
    doSzyfrowania = input('podaj tekst: ')
    szyfrogram = compEnc(doSzyfrowania, lEncSymbols,
                         lEncNumbers, lE, lN)
    tekstJawny = compDec(szyfrogram, lEncSymbols, lEncNumbers, lD, lN)
    # export
    '''dane = list([generator.k1.export(), generator.k2.export()])
    fileOperation.export(dane)'''


if __name__ == '__main__':
    main()
