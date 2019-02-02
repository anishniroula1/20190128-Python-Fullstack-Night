# practice.py
# import random
from random import randint as random_integer

def is_even(a):
    """
    returns if a is even
    """
    # if a % 2 == 0:
    #     return True 
    # else:
    #     return False
    return a % 2 == 0

def opposite(a, b):
    """
    returns if a and b have opposite polarity
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


print('5 is even: ', is_even(5))
print('6 is even: ', is_even(6))

print(opposite(1, 2))
print(opposite(-1, -2))
print(opposite(1, -2))
print(opposite(-1, 2))

print(double_letters('hello'))
print(random_element([]))