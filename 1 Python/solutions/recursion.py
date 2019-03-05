"""
recursion.py

Examples of recursive functions

All recursive functions consist of two parts:

1. Base case(s)
    This is where the function 'bottoms out' or 'starts'. 
    Without a base case you're stuck with an infinite loop.

2. Recursive case
    This is where the function calls itself.
"""
import time

def factorial(n):
    """
    returns n x (n-1) x (n-2) x ... x 1
    """
    if n == 1:
        print('bottoming out')
        return 1
    print('n =', n)
    f = n * factorial(n-1)
    print (f'{n}! = {f}')
    return f


def countup(n):
    """
    recursively prints from 1 to n
    """
    if n < 1:
        return
    countup(n-1)
    print(n)
     

def countdown(n):
    """
    recursively prints from n to 1
    """
    if n < 1:
        return
    print(n)
    countdown(n-1)
     

def summation(n):
    """
    return n + (n-1) + (n-2) + ... + 0
    """
    if n == 0:
        return 0
    return n + summation(n-1)


def fibonacci(n):
    """
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) 
    """
    if n <= 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


fibonacci_cache = [0, 1]
def memoized_fibonacci(n):
    """
    uses cached fibonacci numbers to calculate the nth fibonacci number
    """
    if n >= len(fibonacci_cache):
        fib = memoized_fibonacci(n-1) + memoized_fibonacci(n-2)
        fibonacci_cache.append(fib)
        return fib

    return fibonacci_cache[n]


def iterative_search(l, target):
    for i, elem in enumerate(l):
        if elem == target:
            print(i)
            return i
    print(i)
    return 'Not found'


def binary_search(l, target, start, end):
    """
    recursively searches for target in list
    """
    mid = start + ((end - start) // 2)
    print(f'searching {l[start:end]}')
    print(f'l[{mid}] = {l[mid]}')
    if target == l[mid]:
        print('Target found')
        return mid
    elif end <= start:
        print('Bottomed out')
        return 'Not found'
    else:
        if target < l[mid]:
            print(f'{target} < {l[mid]} ... searching left half of list')
            return binary_search(l, target, start, mid)
        elif l[mid] < target:
            print(f'{target} > {l[mid]} ... searching right half of list')
            return binary_search(l, target, mid + 1, end)


def merge(l1, l2):
    """
    merges two sorted lists
    """
    merged = []
    i = 0
    j = 0

    # print(l1, l2)
    while i < len(l1) and j < len(l2):
        # print(l1[i])
        # print(l2[j])
        # print()
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
        # print(merged)
    merged += l1[i:]
    merged += l2[j:]
    return merged


def mergesort(l):
    """
    divide and conquer sorts list l
    """
    if len(l) <= 1:
        return l
    elif len(l) == 2:
        if l[0] < l[1]:
            return l
        else:
            return [l[1], l[0]]
    else:
        mid = len(l) // 2 
        return merge(mergesort(l[:mid]), mergesort(l[mid:]))


if __name__ == '__main__':
    print(factorial(5))
    countup(10)
    countdown(10)
    print(summation(10))
    print(summation(5))
    start = time.time()
    print(fibonacci(40))
    print(time.time() - start)

    start = time.time()
    n = 200000
    for i in range(n):
        memoized_fibonacci(i)
    print(memoized_fibonacci(n))
    print(time.time() - start)

    nums = ['ash', 'bart', 'bob', 'carl', 'coral', 'devin', 'devon', 'frenchy', 'le-a', 'letron', 'toiletta', 'vaselen']
    print(binary_search(nums, 'bobra', 0, len(nums)))
    print(iterative_search(nums, 'vaselen'))

    print(mergesort([3,2,1,5,6,111,34,-4,222]))