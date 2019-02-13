# pick6_ice.py
from random import randint
from time import time

def pick6():
    """
    returns a list of 6 random numbers from 1-99 

    >>> len(pick6())
    6
    >>> ticket = pick6()
    >>> all([1 <= num <= 99 for num in ticket])
    True
    """
    return [randint(1,99) for n in range(6)]


def calc_payout(ticket, winning):
    """
    calculates number of matches between two tickets and
    returns payout

    >>> calc_payout([1,1,1,1,1,1], [1,1,1,1,1,1])
    25000000
    >>> calc_payout([1,1,1,1,0,0], [1,1,1,1,1,1])
    50000
    >>> calc_payout([1,1,1,1,1,1], [1,1,1,1,1,0])
    1000000
    >>> calc_payout([1,1,1,1,1,1], [0,0,0,0,0,0])
    0
    """
    payout = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
    # payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    # payout = (0, 4, 7, 100, 50000, 1000000, 25000000)

    # matches = 0
    # for i in range(len(ticket)):
    #     if winning[i] == ticket[i]:
    #         matches += 1
    # return payout[matches]
    # print(list(zip(ticket, winning)))

    # matches = len([i for i in range(len(ticket)) if ticket[i] == winning[i]])
    matches = len([i for i,j in zip(ticket, winning) if i == j])
    return payout[matches]


def play_100k():
    winning = pick6()
    balance = 0

    # loop 100k
    for i in range(100000):
        ticket = pick6()
        balance -= 2
        payout = calc_payout(winning, ticket)
        balance += payout
        if payout > 100:
            print('Winner!')
            print(winning)
            print(ticket)
            print(f'Balance: {balance}, payout: {payout}')

    print(f'Balance: {balance}')


def run_until_win(payout=50000):
    start = time()
    winning = pick6()
    win = 0
    count = 0

    while win < payout:
        ticket = pick6()
        win = calc_payout(winning, ticket)
        count += 1

    print(f'Won ${win} with {count} tickets at {time()-start}s.')


def main():
    for i in range(10):
        play_100k()
    # run_until_win(1000000)


if __name__ == '__main__':
    main()