# practice.py

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


print('5 is even: ', is_even(5))
print('6 is even: ', is_even(6))

print(opposite(1, 2))
print(opposite(-1, -2))
print(opposite(1, -2))
print(opposite(-1, 2))
