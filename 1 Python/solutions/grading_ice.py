# grading_ice.py

while True: # loop through grading program until the user says they are done
    grade = int(input('Enter your number grade: '))
    ones_digit = grade % 10 # calculates + or -

    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    sign = ''
    if letter_grade != 'F':
        if ones_digit < 4:
            sign = '-'
        elif ones_digit > 7:
            sign = '+'

    if letter_grade == 'A':
        if grade >= 100:
            sign = '+'
        elif 4 < ones_digit < 100:
            sign = ''

    print(str(letter_grade) + sign)

    valid_inputs = ['yes', 'y', 'no', 'n']
    while True: # input validation
        play_again = input('Do you want to continue: ').strip().lower()
        if play_again in valid_inputs:
            break

    if play_again.startswith('n'): # break out of infinite loop
        print('Goodbye!')
        break
    # elif play_again.startswith('y'): # redundant
    #     continue