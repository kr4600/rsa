from string import ascii_letters, digits, punctuation, whitespace
from secrets import randbelow


# spinanie list w słownik
def slownik(lis1, lis2):
    return dict(zip(lis1, lis2))


def genTablicy(iloscCyfr=3):
    # global encDic

    # liczna powinna być CO NAJMNIEJ:
    #   3-cyfrowa dla wszystkich [99]
    #
    # 52 to ascii_letters (wielkie 26 i małe 26)
    # 10 to digits
    # 32 to punctuation

    # inna opcja to użycie ord() i chr() do zamiany liter na ascii
    # i wymienienie reszty
    encSymbols = (list(ascii_letters) + list(digits)
                  + list(punctuation) + list(whitespace))
    encNumbers = []
    while len(encNumbers) < len(encSymbols):
        # 10 ** iloscCyfr, bo 3-cyfrowe są mniejsze od 10**3
        rng = randbelow(10 ** iloscCyfr)
        if rng >= 10 ** (iloscCyfr - 1) and rng not in encNumbers:
            encNumbers.append(rng)
    return encSymbols, encNumbers


if __name__ == '__main__':
    li1, li2 = genTablicy()
    print(slownik(li1, li2))
