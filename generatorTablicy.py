from string import ascii_letters, digits, punctuation, whitespace
from secrets import randbelow


def slownik(lis1, lis2):
    return dict(zip(lis1, lis2))


def genTablicy(iloscCyfr=3):
    encSymbols = (list(ascii_letters) + list(digits)
                  + list(punctuation) + list(whitespace))
    encNumbers = []
    while len(encNumbers) < len(encSymbols):
        rng = randbelow(10 ** iloscCyfr)
        if rng >= 10 ** (iloscCyfr - 1) and rng not in encNumbers:
            encNumbers.append(rng)
    return encSymbols, encNumbers


if __name__ == '__main__':
    li1, li2 = genTablicy()
    print(li1)
    print(li2)
    print(slownik(li1, li2))
