# make_change_ice.py
while True: # input validation
    total_pennies = input('How much money do you have?: ').strip().strip('$')
    try: 
        # this will give you a ValueError if you try to turn a string into a number
        total_pennies = round(float(total_pennies) * 100)
        if total_pennies < 0:
            raise ValueError
        break # if no error occurs, we break out of the inf loop and continue in our program
    except ValueError: # we catch and print an error message
        print('Please enter a non-negative dollar amount')

denomination = {
    'hundreds': 10000,
    'fifties': 5000,
    'twenties': 2000,
    'tens': 1000,
    'fives': 500,
    'ones': 100,
    'quarters': 25,
    'dimes': 10,
    'nickles': 5,
    'pennies': 1
}

change = ['Your change is']

for d in denomination:
    d_change = total_pennies // denomination[d]
    total_pennies %= denomination[d]
    change.append(f'{round(d_change)} {d}')

print(', '.join(change))
