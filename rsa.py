import wejscie
import generator
import fileOperation

wejscie.sprawdzanie(wejscie.wejscieZKonsoli())
generator.generatorKluczy()
# fileOperation.export(generator.k1)
dane = list(['k1', generator.k1.p1, generator.k1.n,
             'k2', generator.k2.p1, generator.k2.n])
fileOperation.export(dane)
