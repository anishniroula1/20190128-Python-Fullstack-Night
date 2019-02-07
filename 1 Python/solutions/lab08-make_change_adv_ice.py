# make_change_ice.py
while True: # input validation
    total = input('How much money do you have?: ').strip().strip('$')
    try: 
        # this will give you a ValueError if you try to turn a string into a number
        total = round(float(total) * 100)
        if total < 0:
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

for d in denomination: # loop through all denominations (d is key)
    d_change = total // denomination[d] # get change by floor dividing total with denom
    total %= denomination[d] # remove denomination from total
    change.append(f'{round(d_change)} {d}') # add change + denom name to change list

print(', '.join(change)) # print final change
