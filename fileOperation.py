import json


def export(data='test', *, fileName='klucze'):
    jsonData = json.dumps(data)
    try:
        f = open(fileName, 'xt')
    except FileExistsError:
        print('plik istnieje, dane zostaną dopisane do pliku')
        f = open(fileName, 'at')
        jsonData = '\n' + jsonData
    f.write(jsonData)
    f.close()


def main():
    export()
    with open('klucze', 'rt') as f:
        read_data = f.read()
    print(read_data)


if __name__ == '__main__':
    main()
