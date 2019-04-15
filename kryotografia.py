from generatorTablicy import slownik


def lis2str(data):
    ciag = ''
    for i in range(len(data)):
        ciag += data[i]
    return ciag


def int2len(data):
    return len(str(data))


def sekwencjonowanie(ciag, dlugosc):
    lista = list(ciag[i:i + dlugosc]
                 for i in range(0, len(ciag), dlugosc))
    return lista


def krypt(lista, x, n, szyfrowanie=True):
    krypto = ''
    for i in range(len(lista)):
        liczba = int(lista[i])
        encrLiczba = str(liczba ** x % n)
        if szyfrowanie is True:
            lenEncrLiczba = int2len(encrLiczba)
            lenN = int2len(n)
            if lenEncrLiczba < lenN:
                encrLiczba = '0' * (lenN - lenEncrLiczba) + encrLiczba
        else:
            if i == len(lista) - 1:
                print('dodano')
                encrLiczba = str('0' * int(encrLiczba)) + encrLiczba
        krypto += encrLiczba
    return krypto


def kodowanie(tekst, lisSymbole, lisLiczby, n):
    print('kodowansko')
    cyfry = ''
    encodeTab = slownik(lisSymbole, lisLiczby)
    try:
        for i in tekst:
            print(f'{i} = {encodeTab[i]}')
            cyfry += str(encodeTab[i])
        print(cyfry)
        lenghtN = int2len(n) - 1
        modCyfry = len(cyfry) % lenghtN
        brakuje = lenghtN - modCyfry

        if brakuje >= 2:
            brakuje -= 1
            cyfry += '0' * (brakuje) + str(brakuje)
        else:
            brakuje += lenghtN - 1
            cyfry += '0' * (brakuje) + str(brakuje)
        print(cyfry)

        cyfry = sekwencjonowanie(cyfry, lenghtN)
        print(cyfry)
        return cyfry
    except KeyError:
        print('znak przeznaczony do zakodowania nie istnieje w tablicy')


def dekodowanie(lista, lisSymbole, lisLiczby):
    print('dekodowansko')
    decodeTab = slownik(lisLiczby, lisSymbole)
    ciag = lis2str(lista)
    print(ciag)
    print('redukcja')
    ciag = ciag[:-(int(ciag[-1]) + 1)]
    print(ciag)

    iloCyfrowa = list(decodeTab.keys())
    iloCyfrowa = int2len(iloCyfrowa[0])
    print(iloCyfrowa)
    lista = sekwencjonowanie(ciag, iloCyfrowa)
    print(lista)
    zdekodowane = ''
    for i in range(len(lista)):
        klucz = decodeTab[int(lista[i])]
        print(f'{lista[i]} = {klucz}')
        zdekodowane += klucz
    return zdekodowane


def szyfrowanie(lista, e, n):
    print('szyfrowando')
    szyfrogram = krypt(lista, e, n)
    print(szyfrogram)
    return szyfrogram


def deszyfrowanie(ciag, d, n):
    print('deszyfrowando')
    lista = sekwencjonowanie(ciag, int2len(n))
    print(lista)
    tekstJawny = krypt(lista, d, n, False)
    print(tekstJawny)
    return tekstJawny


def compEnc(tekst, lisSymbole, lisLiczby, e, n):
    lista = kodowanie(tekst, lisSymbole, lisLiczby, n)
    return szyfrowanie(lista, e, n)


def compDec(ciag, lisSymbole, lisLiczby, d, n):
    lista = deszyfrowanie(ciag, d, n)
    dekodowanie(lista, lisSymbole, lisLiczby)


def main():
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#',
             '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
             ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{',
             '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']

    list2 = [323, 176, 602, 700, 297, 462, 496, 374, 790, 314, 714, 326, 438,
             772, 341, 134, 214, 258, 233, 860, 817, 444, 550, 344, 141, 615,
             861, 521, 894, 171, 856, 776, 246, 917, 903, 877, 120, 409, 562,
             686, 338, 307, 486, 801, 180, 799, 107, 256, 330, 168, 588, 932,
             966, 524, 695, 286, 713, 840, 977, 677, 868, 668, 684, 329, 558,
             479, 453, 512, 696, 723, 350, 468, 800, 385, 902, 209, 279, 780,
             663, 310, 365, 725, 268, 160, 507, 767, 871, 621, 106, 301, 389,
             245, 485, 784, 399, 869, 715, 127, 262, 821]

    # encDic = genTablicy()
    zakodowane = kodowanie('lo leh', list1, list2, 4087)
    print(zakodowane)

    szyfro = szyfrowanie(zakodowane, 73, 4087)
    zdeszyfro = deszyfrowanie(szyfro, 4177, 4087)

    zdekodo = dekodowanie(zdeszyfro, list1, list2)
    print(zdekodo)


if __name__ == '__main__':
    main()
