# practice.py
# import random
from random import randint as random_integer

def is_even(a):
    """
    returns if a is even

    >>> is_even(1)
    False
    >>> is_even(2)
    True
    >>> is_even(0)
    True
    """
    # if a % 2 == 0:
    #     return True 
    # else:
    #     return False
    return a % 2 == 0

def opposite(a, b):
    """
    returns if a and b have opposite polarity

    >>> opposite(1,0)
    False
    >>> opposite(-1,-2)
    False
    >>> opposite(-1,1)
    True
    >>> opposite(1,-1)
    True
    """
    # if (a >= 0 and b >= 0) or (a < 0 and b < 0):
    #     return False
    # else:
    #     return True
    # return not ((a >= 0 and b >= 0) or (a < 0 and b < 0))
    return (a >= 0 and b < 0) or (a < 0 and b >= 0)


def double_letters(text):
    """
    returns string of each letter in text doubled

    >>> double_letters('hello')
    'hheelllloo'
    """
    double = ''
    for char in text:
        double += char * 2
    return double

    # double = []
    # for item in text:
    #     double.append(item*2)
    # return ''.join(double)

    # return ''.join([char*2 for char in text])


def random_element(l):
    """
    returns random element in list l
    """
    if l:
        index = random_integer(0, len(l)-1)
        return l[index]
    return 'empty list'


def lists_to_dict(keys, values):
    """
    returns dictionary of keys  mapped to values
    :keys: list
    :values: list

    >>> lists_to_dict(['a','b','c'], ['aardvark','bear','coyote'])
    {'a': 'aardvark', 'b': 'bear', 'c': 'coyote'}
    """
    pass
