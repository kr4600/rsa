from json import dumps
import zstandard as zstd


def comp(data):
    cctx = zstd.ZstdCompressor(level=3, write_checksum=True)
    compressed = cctx.compress(data.encode())
    return compressed


def decomp(data):
    dctx = zstd.ZstdDecompressor()
    decompressed = dctx.decompress(data, max_output_size=1048576)
    return decompressed


def export(data='test', *, fileName='klucze', compression=False):
    jsonData = dumps(data)
    if compression is True:
        fileName += 'Com'
        jsonData = comp(jsonData)
        typZapisu = 'b'
    else:
        typZapisu = 't'
    try:
        f = open(fileName, 'x' + typZapisu)
    except FileExistsError:
        print('plik istnieje, dane zostaną dopisane do pliku')
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


if __name__ == '__main__':
    main()
