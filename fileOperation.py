import json
import zstandard as zstd


def comp(data):
    # poziom kompresji to 0-22 (3, 6, 7-8, 19)
    # zapisywanie checksum jest opcjonalne lecz przydatne
    cctx = zstd.ZstdCompressor(level=3, write_checksum=True)
    compressed = cctx.compress(data.encode())
    return compressed


def decomp(data):
    dctx = zstd.ZstdDecompressor()
    # max_output_size służy do określenia maksumalnego wyjścia
    # (prawdopodobnie 1MiB, nie wiadomo czy wyrażone jest to w
    # bitach czy w bajtach)
    decompressed = dctx.decompress(data, max_output_size=1048576)
    return decompressed


def export(data='test', *, fileName='klucze', compression=False):
    jsonData = json.dumps(data)
    if compression is True:
        # kompresja wymaga modyfikacji pliku w spodób bitowy, a nie tekstowy
        # który jest domyślnym trybem, stąd zmienna "typZapisu"
        fileName += 'Com'
        jsonData = comp(jsonData)
        typZapisu = 'b'
    else:
        typZapisu = 't'
    try:
        f = open(fileName, 'x' + typZapisu)
    except FileExistsError:
        print('plik istnieje, dane zostaną dopisane do pliku')
        # obiekt g służy tylko i wyłącznie stworzeniu odstpu pomiędzy danymi
        with open(fileName, 'at') as g:
            g.write('\n' * 2)
        f = open(fileName, 'a' + typZapisu)
    f.write(jsonData)
    f.close()


def main():
    export(compression=True)
    with open('kluczeCom', 'rb') as f:
        read_data = f.readline()
    read_data = decomp(read_data)
    print(read_data)


def test():
    heh = 'l' * 100
    heh = json.dumps(heh)
    compr = comp(heh)
    decompr = decomp(compr)
    print(heh)
    print(decompr.decode())
    print(len(compr))
    f = open('lol', 'xb')
    f.write(compr)
    f.close()
    f = open('lol', 'rb')
    readed = f.read()
    f.close()
    print(readed)
    readed = decomp(readed)
    print(readed)


if __name__ == '__main__':
    main()
    # test()
