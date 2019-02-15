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

    >>> extract_less_than_ten([2,4,6,8,10,12,14,16,18,20])
    [2, 4, 6, 8]
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

    >>> common_elements([1,2,3], [3,4,5])
    [3]
    """
    # return [n for n in nums1 if n in nums2]

    # common = []
    # for n in nums1:
    #     if n in nums2:
    #         common.append(n)
    # return common

    # return list(set(nums1) & set(nums2))
    return list(set(nums1).intersection(set(nums2)))


def common_elements_using_comprehension(nums1, nums2):
    """
    returns common elements of nums1 and nums2 using comprehension

    >>> common_elements_using_comprehension([1,2,3,4], [3,4,5,6])
    [3, 4]
    """
    return [n for n in nums1 if n in nums2]


def common_elements_using_loop(nums1, nums2):
    """
    returns common elements of nums1 and nums2 using loop

    >>> common_elements_using_loop([1,2,3,4], [3,4,5,6])
    [3, 4]
    """
    common = []
    for n in nums1:
        if n in nums2:
            common.append(n)
    return common


def common_set_intersection(nums1, nums2):
    """
    returns common elements of nums1 and nums2 using set intersection

    >>> common_set_intersection([1,2,3,4], [3,4,5,6])
    [3, 4]
    """
    return list(set(nums1) & set(nums2))


def reverse(l):
    """
    reverses list by hand and returns it

    >>> reverse([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    """
    r = []
    for i in range(len(l)-1, -1, -1):
        r.append(l[i])
    return r


def reverse_slice(l):
    """
    returns reverse of l using slicing

    >>> reverse_slice([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    """
    return l[::-1]


def reverse_in_place(l):
    """
    reverses l in place and returns l

    >>> reverse_in_place([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    """
    l.reverse()
    return l


# nums = list(range(20))
# nums2 = evens_from_n(40)
# print(nums, extract_less_than_ten(nums))
# start = time.clock()
# print('comprehension:', common_elements_using_comprehension(nums, nums2), time.clock() - start)
# start = time.clock()
# print('loop:', common_elements_using_loop(nums, nums2), time.clock() - start)
# start = time.clock()
# print('set:', common_set_intersection(nums, nums2), time.clock() - start)

# start = time.clock()
# print('reverse by hand:', reverse(nums), time.clock() - start)
# start = time.clock()
# print('reverse slice:', reverse_slice(nums), time.clock() - start)
# start = time.clock()
# print('reversed built in:', reversed(nums), time.clock() - start)
# start = time.clock()
# print('reverse built in:', reverse_in_place(nums), time.clock() - start)


def count_letter(letter, word):
    """
    returns the number of letter occurances in a string
    :letter: str char
    :word: str

    >>> count_letter('i', 'antidisestablishmentterianism')
    5
    >>> count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')
    2
    """
    # count = 0
    # for i in word:
    #     if i == letter:
    #         count += 1 
    # return count

    return len([char for char in word if char == letter])


def combine_lists(list1, list2):
    """
    returns list of list1 and list2 elements alternating

    >>> combine_lists(['a','b','c'], [1,2,3])
    ['a', 1, 'b', 2, 'c', 3]
    """
    # combined = []
    # for i, j in zip(list1, list2):
    #     combined += [i, j]
    # return combined

    # combined = []
    # for i in range(len(list1)):
    #     combined.append(list1[i])
    #     combined.append(list2[i])
    # return combined

    return sum([list(i) for i in zip(list1, list2)], [])


def find_pair(nums, target):
    """
    returns first matching pair of numbers that sum up to the target number
    :nums: list of numbers
    :target: target sum
    :return: list of two numbers that add up to target, or None if no pair found

    >>> find_pair([5, 6, 2, 3], 7)
    [5, 2]

    """
    # # O(N^2) solution
    # combos = []
    # count = 0
    # for i in nums: # loop N times
    #     for j in nums: # N times
    #         if i == j:
    #             continue
    #         if i > j:
    #             break
    #         count += 1
    #         if i + j == target:
    #             combos.append([i, j])
    # print(f'looped {count} times')            
    # return combos

    nums.sort()
    combos = []
    count = 0
    for i in range(len(nums)-1): # (N)
        for j in range(len(nums)-1, 0, -1): # (N/2)
            if i >= j:
                return combos
            count += 1 
            if nums[i] + nums[j] == target:
                combos.append([nums[i], nums[j]])

    print(f'looped {count} times')            
    return combos

    # combos = []
    # count = 0
    # while len(nums) > 1:
    #     count += 1
    #     num = nums[-1]
    #     if num < target:
    #         difference = target - num
    #         if difference in nums:
    #             combos.append([num, difference])
    #     nums.pop()
    # print(f'looped {count} times')
    # return combos

    nums.sort() # O(nlog)
    seen = {}
    combos = []
    count = 0
    for i in range(len(nums)): # O(n)
        num = nums[i]
        if num > target:
            break
        difference = target - num
        if difference in nums:
            index_of_differences = [j for j in range(len(nums)) if nums[j] == difference] # O*n)
            for j in index_of_differences: # O(m), where m = number of differences in num
                count += 1
                if j not in seen.get(i, []): 
                    seen[j] = seen.get(j, []) + [i]
                    combos.append([num, difference])
                    print(f'num={num}, i={i}, j={j}, seen={seen}')
    print(f'looped {count} times')
    return combos


# print(find_pair([5, 6, 2, 3], 7))
print(find_pair([4, 3, 5, 2, 5, 2, 1], 7))
# print(find_pair([1,2,3,4,5,6,7], 7))