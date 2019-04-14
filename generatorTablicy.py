from string import ascii_letters, digits, punctuation
from secrets import randbelow


def genTablicy(iloscCyfr=3):
    # global encDic

    # liczna powinna być CO NAJMNIEJ:
    #   3-cyfrowa dla wszystkich [93] (ascii_letters, digits, punctuation)
    #
    # 52 to ascii_letters (wielkie 26 i małe 26)
    # 10 to digits
    # 32 to punctuation

    # inna opcja to użycie ord() i chr() do zamiany liter na ascii
    # i wymienienie reszty
    encSymbols = list(ascii_letters) + list(digits) + list(punctuation)
    encNumbers = []
    while len(encNumbers) < len(encSymbols):
        # 10 ** iloscCyfr, bo 3-cyfrowe są mniejsze od 10**3
        rng = randbelow(10 ** iloscCyfr)
        if rng >= 10 ** (iloscCyfr - 1) and rng not in encNumbers:
            encNumbers.append(rng)

    encDic = dict(zip(encSymbols, encNumbers))
    return encDic


if __name__ == '__main__':
    print(genTablicy())
