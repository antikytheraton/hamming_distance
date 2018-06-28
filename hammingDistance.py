"""
Hamming distance snippets
http://code.activestate.com/recipes/499304-hamming-distance/
"""

import itertools
from operator import ne
import time


def hamdist(str1, str2):
    """
    Count the # of diferences between 
    equal length strings str1 and str2
    """
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1
    return diffs

def bearophile(str1, str2):
    assert len(str1) == len(str2)
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def dalke(str1, str2):
    assert len(str1) == len(str2)
    return sum(map(ne, str1, str2))

def numeric_hamming(num1, num2):
    assert len(num1)== len(num2)
    return sum(num1 != num2)

def seq3(i):
    return 'A' * i

def seq4(seq, i):
    return seq[:i//2] + 'B' + seq[i//2+1:]

def go(i):
    str1 = seq3(i)
    str2 = seq4(str1, i)
    print(i)
    for func in (hamdist, bearophile, dalke):
        t1 = time.time()
        func(str1, str2)
        func(str1, str2)
        func(str1, str2)
        func(str1, str2)
        func(str1, str2)
        func(str1, str2)
        func(str1, str2)
        func(str1, str2)
        func(str1, str2)
        func(str1, str2)
        t2 = time.time()
        print(t2-t1)
    print('\t')


go(1000000)
