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
    # double = ''
    # for char in text:
    #     double += char * 2
    # return double

    # double = []
    # for char in text:
    #     double.append(char*2)
    # return ''.join(double)

    return ''.join([char*2 for char in text])

print(double_letters('hello'))

def random_element(l):
    """
    returns random element in list l
    """
    print('in random_element', combined)
    if l:
        index = random_integer(0, len(l)-1)
        return l[index]
    return 'empty list'


def lists_to_dict(keys, values):
    """
    returns dictionary of keys mapped to values
    :keys: list
    :values: list

    >>> lists_to_dict(['a','b','c'], ['aardvark','bear','coyote']) 
    {'a': 'aardvark', 'b': 'bear', 'c': 'coyote'}
    """
    # combined = {}
    # for i in range(len(keys)):
    #     # print(i, keys[i], values[i])
    #     combined[keys[i]] = values[i]
    # return combined

    # # equivalent to above
    # return {keys[i]:values[i] for i in range(len(keys))}

    return dict(zip(keys, values))


def average_values(dictionary):
    """
    returns the average values in dictionary

    >>> average_values({'apple':1.2, 'banana':3.3, 'pear':2.1})
    2.2
    """
    # running_sum = 0
    # for val in dictionary.values():
    #     running_sum += val
    # return running_sum/len(dictionary)

    return round(sum(dictionary.values())/len(dictionary), 2)


def eveneven(num_list):
    """
    returns true if there is an even number of even numbers in nums
    :nums: list of ints
    """
    # nums = 0
    # for item in num_list:
    #     if item % 2 == 0:
    #         nums += 1
    # # if nums % 2 == 0:
    # #     return True 
    # # else:
    # #     return False
    # return nums % 2 == 0

    evens = [num for num in num_list if num % 2 == 0]
    # print(evens, len(evens))
    return len(evens) % 2 == 0


print(eveneven([5, 6, 2]), 'should =', True)
print(eveneven([5, 5, 2]), 'should =', False)
print(eveneven([1,2,3,4,5,6,7,8]), 'should =', True)
