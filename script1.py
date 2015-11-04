#!/usr/bin/env python2.7

def checkio(data):
    return [x for x in data if data.count(x)>1]

def soma(fator1, fator2):
    return(fator1 + fator2)


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert soma(2, 3) == 5, " Teste um"
