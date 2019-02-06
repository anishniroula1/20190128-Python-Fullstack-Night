# sock_sorter.py
"""
Hints:
- Loop through 100
- Use a dictionary as a counter for your socks
- At the end, use a little math to figure out if your 
  sock count is even 
"""

# counter = {}

# # creating a count 
# counter['thing'] = 1 

# # increasing count 
# counter['thing'] += 1

# # or, in one line,
# # if count['thing'] exists, increase its count by 1
# # else, set its count as 1
# counter['thing'] = counter.get('thing', 0) + 1

import random

sock_list = []
sock_types = ['ankle', 'crew', 'calf', 'thigh']
colors = ['black', 'white', 'blue']
sock_counter = {}

for i in range(100):
    sock = random.choice(sock_types)
    color = random.choice(colors)
    sock_list.append((sock, color))
    
    sock_counter[(sock, color)] = sock_counter.get((sock, color), 0) + 1
# 
#     # equivalent to above
#     # if sock in sock_counter:
#     #     sock_counter[sock] += 1 
#     # else:
#     #     sock_counter[sock] = 1

print(sock_list)
print(sock_counter)

for sock in sock_counter:
    print(f'{sock} has {sock_counter[sock]%2} loner(s)')
    # print(f'{sock} has {sock_counter.get(sock)%2} loner(s)') # equivalent to above


# # there's a built in type for this!
# from collections import Counter
# counter = Counter(sock_list)
# print(counter)

