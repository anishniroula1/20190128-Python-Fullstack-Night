# loop_example.py
while True:
    # input validation
    while True:
        keep_looping = input('Keep looping? ').strip().lower()
        if keep_looping in ['yes', 'no', 'y', 'n']:
            break
        print('Invalid input')
    if keep_looping.startswith('y'):
        continue
    print('Done looping')
    break