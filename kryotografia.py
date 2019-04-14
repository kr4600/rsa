# import generatorTablicy


def lis2str(data):
    ciag = ''
    for i in range(len(data)):
        ciag += data[i]
    return ciag


def sekwencjonowanie(ciag, dlugosc):
    # dzielenie ciągu na liste po %dlugosc znaków
    lista = list(ciag[i:i + dlugosc]
                 for i in range(0, len(ciag), dlugosc))
    return lista


def kodowanie(tekst, encodeTab, lN=100):
    cyfry = ''
    try:
        # konwersja znaków na liczby
        for i in tekst:
            print(f'{i} = {encodeTab[i]}')
            cyfry += str(encodeTab[i])
        # print(encodeTab)
        print(cyfry)
        lenghtN = len(str(lN)) - 1
        modCyfry = len(cyfry) % lenghtN
        brakuje = lenghtN - modCyfry

        # dopełnianie do pełnych sekwencji
        if brakuje >= 2:
            brakuje -= 1
            cyfry += '0' * (brakuje) + str(brakuje)
        else:
            brakuje += lenghtN - 1
            cyfry += '0' * (brakuje) + str(brakuje)

        cyfry = sekwencjonowanie(cyfry, lenghtN)
        return cyfry
    except KeyError:
        print('znak przeznaczony do zakodowania nie istnieje w tablicy')


def dekodowanie(lista, decodeTab):
    ciag = lis2str(lista)
    print(ciag)
    # redukcja dopełnienia aka magia
    #
    # ciag[:]       wypisanie czesci znakow
    # ciag[-1]      ostatnia liczba okreslająca ilosc wypełnienia
    # ciag[-1] + 1  uwzgldnienie samego wyznacznika
    # int()         konwertuje/umożliwia dzikie działania na liczbach
    # -(int())      okresla koncowy znak
    ciag = ciag[:-(int(ciag[-1]) + 1)]

    iloCyfrowa = list(decodeTab.keys())
    iloCyfrowa = len(str(iloCyfrowa[1]))
    print(iloCyfrowa)
    lista = sekwencjonowanie(ciag, iloCyfrowa)
    print(lista)
    tekstJawny = ''
    for i in range(len(lista)):
        # decodeTab[int(lista[i])]
        # decideTab[] - tablica dekodując
        # int() - konwersja na inta
        # lista[i] robi za klucz w słowniku
        klucz = decodeTab[int(lista[i])]
        print(f'{lista[i]} = {klucz}')
        tekstJawny += klucz
    return tekstJawny


def szyfrowanie(cia):
    pass


def deszyfrowanie():
    pass


def main():
    defaultDic = {'a': 888, 'b': 990, 'c': 654, 'd': 335, 'e': 864, 'f': 961,
                  'g': 351, 'h': 919, 'i': 596, 'j': 742, 'k': 747, 'l': 252,
                  'm': 292, 'n': 629, 'o': 540, 'p': 957, 'q': 588, 'r': 660,
                  's': 776, 't': 666, 'u': 791, 'v': 953, 'w': 940, 'x': 653,
                  'y': 775, 'z': 991, 'A': 101, 'B': 946, 'C': 657, 'D': 461,
                  'E': 635, 'F': 418, 'G': 358, 'H': 503, 'I': 277, 'J': 832,
                  'K': 258, 'L': 517, 'M': 923, 'N': 446, 'O': 717, 'P': 859,
                  'Q': 799, 'R': 230, 'S': 139, 'T': 344, 'U': 176, 'V': 415,
                  'W': 452, 'X': 189, 'Y': 136, 'Z': 481, '0': 676, '1': 552,
                  '2': 581, '3': 695, '4': 571, '5': 726, '6': 290, '7': 309,
                  '8': 306, '9': 514, '!': 918, '"': 147, '#': 477, '$': 819,
                  '%': 908, '&': 516, "'": 830, '(': 399, ')': 987, '*': 377,
                  '+': 981, ',': 486, '-': 448, '.': 609, '/': 174, ':': 529,
                  ';': 834, '<': 756, '=': 179, '>': 569, '?': 591, '@': 722,
                  '[': 668, '\\': 188, ']': 769, '^': 405, '_': 863, '`': 903,
                  '{': 371, '|': 682, '}': 862, '~': 460, ' ': 279, '\t': 774,
                  '\n': 251, '\r': 528, '\x0b': 977, '\x0c': 134}

    defDecDic = {888: 'a', 990: 'b', 654: 'c', 335: 'd', 864: 'e', 961: 'f',
                 351: 'g', 919: 'h', 596: 'i', 742: 'j', 747: 'k', 252: 'l',
                 292: 'm', 629: 'n', 540: 'o', 957: 'p', 588: 'q', 660: 'r',
                 776: 's', 666: 't', 791: 'u', 953: 'v', 940: 'w', 653: 'x',
                 775: 'y', 991: 'z', 101: 'A', 946: 'B', 657: 'C', 461: 'D',
                 635: 'E', 418: 'F', 358: 'G', 503: 'H', 277: 'I', 832: 'J',
                 258: 'K', 517: 'L', 923: 'M', 446: 'N', 717: 'O', 859: 'P',
                 799: 'Q', 230: 'R', 139: 'S', 344: 'T', 176: 'U', 415: 'V',
                 452: 'W', 189: 'X', 136: 'Y', 481: 'Z', 676: '0', 552: '1',
                 581: '2', 695: '3', 571: '4', 726: '5', 290: '6', 309: '7',
                 306: '8', 514: '9', 918: '!', 147: '"', 477: '#', 819: '$',
                 908: '%', 516: '&', 830: "'", 399: '(', 987: ')', 377: '*',
                 981: '+', 486: ',', 448: '-', 609: '.', 174: '/', 529: ':',
                 834: ';', 756: '<', 179: '=', 569: '>', 591: '?', 722: '@',
                 668: '[', 188: '\\', 769: ']', 405: '^', 863: '_', 903: '`',
                 371: '{', 682: '|', 862: '}', 460: '~', 279: ' ', 774: '\t',
                 251: '\n', 528: '\r', 977: '\x0b', 134: '\x0c'}
    # encDic = genTablicy()
    zakodowane = kodowanie('lo le', defaultDic)
    print(zakodowane)

    '''
    odwrocenie dzialania słownika
    k = list(defaultDic)
    v = list(defaultDic.values())
    print(k, v)
    print(generatorTablicy.slownik(v,k))
    '''

    zdekodo = dekodowanie(zakodowane, defDecDic)
    print(zdekodo)


if __name__ == '__main__':
    main()
