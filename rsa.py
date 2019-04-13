import wejscie
import generator
import fileOperation

# wejscie.sprawdzanie(wejscie.wejscieZKonsoli())


def main():
    wejscie.sprawdzanie()
    generator.generatorKluczy()
    dane = list([generator.k1.export(), generator.k2.export()])
    fileOperation.export(dane)


if __name__ == '__main__':
    main()
