import wejscie
import generator
import fileOperation


def main():
    wejscie.sprawdzanie(wejscie.wejscieZKonsoli())
    generator.generatorKluczy()
    dane = list([generator.k1.export(), generator.k2.export()])
    fileOperation.export(dane)


if __name__ == '__main__':
    main()
