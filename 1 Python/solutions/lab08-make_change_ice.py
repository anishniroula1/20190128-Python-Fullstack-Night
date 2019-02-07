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
    
total_dollars = total_pennies // 100
total_pennies %= 100
total_quarters = total_pennies // 25
total_pennies %= 25 
             # = total_pennies - total_quarters * 25
total_dimes = total_pennies // 10
total_pennies %= 10
total_nickles = total_pennies // 5
total_pennies %= 5

# change = total // denomination 
# total %= denomination

print(f'You have {total_dollars} dollars, {int(total_quarters)} quarters, {int(total_dimes)} dimes, {int(total_nickles)} nickles, and {int(total_pennies)} pennies.')
