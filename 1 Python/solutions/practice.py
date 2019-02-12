# practice.py
# import random
import time
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

    >>> eveneven([5, 6, 2])
    True
    >>> eveneven([5, 5, 2])
    False
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


def powers_of_two(n):
    """
    returns list of the first n powers of two

    >>> powers_of_two(10)
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    """
    return [2**i for i in range(0, n)]


def evens_to_n(n):
    """
    returns list of the first n even numbers

    >>> evens_to_n(10)
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    """
    return [i*2 for i in range (1,n+1)]


def evens_from_n(n):
    """
    returns filter of even numbers from 0 to n

    >>> evens_from_n(20)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    return [i for i in range(n) if not i % 2]


def extract_less_than_ten(nums):
    """
    returns list of only numbers less than ten from nums
    :nums: list of numbers
    """
    return [i for i in nums if i < 10]

    # less_ten = []
    # for i in nums:
    #     if i < 10:
    #         less_ten.append(i)
    # return less_ten


def common_elements(nums1, nums2):
    """
    returns list of common elements in num1 and nums2
    :nums1: list of numbers
    :nums2: list of numbers
    """
    # return [n for n in nums1 if n in nums2]

    # common = []
    # for n in nums1:
    #     if n in nums2:
    #         common.append(n)
    # return common

    # return list(set(nums1) & set(nums2))
    return list(set(nums1).intersection(set(nums2)))


def common_comprehension(nums1, nums2):
    return [n for n in nums1 if n in nums2]


def common_loop(nums1, nums2):
    common = []
    for n in nums1:
        if n in nums2:
            common.append(n)
    return common


def common_set_intersection(nums1, nums2):
    return list(set(nums1).intersection(set(nums2)))


def reverse(l):
    r = []
    for i in range(len(l)-1, -1, -1):
        r.append(l[i])
    return r


def reverse_slice(l):
    return l[::-1]


def reverse_in_place(l):
    l.reverse()
    return l


nums = list(range(20))
nums2 = evens_from_n(40)
# print(nums, extract_less_than_ten(nums))
start = time.clock()
print('comprehension:', common_comprehension(nums, nums2), time.clock() - start)
start = time.clock()
print('loop:', common_loop(nums, nums2), time.clock() - start)
start = time.clock()
print('set:', common_set_intersection(nums, nums2), time.clock() - start)

start = time.clock()
print('reverse by hand:', reverse(nums), time.clock() - start)
start = time.clock()
print('reverse slice:', reverse_slice(nums), time.clock() - start)
start = time.clock()
print('reversed built in:', reversed(nums), time.clock() - start)
start = time.clock()
print('reverse built in:', reverse_in_place(nums), time.clock() - start)
