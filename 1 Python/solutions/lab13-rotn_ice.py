# rotn_ice.py
alphabet = 'abcdefghijklmnopqrstuvwxyz' 
rot13    = 'nopqrstuvwxyzabcdefghijklm'

def encode13(message):
    """
    returns encoded message by ROT13
    """
    encoded = ''
    for char in message:
        index = alphabet.find(char)
        if index == -1: # if char is not a letter
            encoded += char
        else:
            encoded += rot13[index]
    return encoded


def decode13(message):
    """
    returns decoded message by ROT13
    """
    decoded = ''
    for char in message:
        index = rot13.find(char)
        if index == -1: # if char is not a letter
            decoded += char
        else:
            decoded += alphabet[index]
    return decoded


def encode(message, n):
    """
    returns encoded message by n rotation
    """
    n %= 26 # wrap around 26
    translate = alphabet[n:] + alphabet[:n]
    #         =    right     +    left 

    translate = dict(zip(alphabet, translate))
    encoded = ''
    for char in message:
        encoded += translate.get(char, char)
    return encoded


def decode(message, n):
    """
    returns decoded message by n rotation
    """
    n %= 26 # wrap around 26
    translate = alphabet[n:] + alphabet[:n]
    #         =    right     +    left 
    encoded = ''
    for char in message:
        index = translate.find(char)
        if index == -1: # if char is not a letter
            encoded += char
        else:
            encoded += alphabet[index]
    return encoded


def cypher(message, n, decode=False):
    n %= 26 # wrap around 26
    translate = alphabet[n:] + alphabet[:n]
    #         =    right     +    left 

    if decode:
        translate = dict(zip(translate, alphabet))
    else:
        # encode logic
        translate = dict(zip(alphabet, translate))

    coded = ''
    for char in message:
        coded += translate.get(char, char)
    return coded        


def main():
    replay = True
    print('-'*60)
    print('Welcome to the ROT cypher')
    print('-'*60)
    while replay: # loop game

        while True: # input validation
            operation = input('Do you want to (e)ncode or (d)ecode: ').strip().lower()
            if operation in ['encode', 'e', 'decode', 'd']:
                break

        while True: # input validation
            try:
                n = int(input('How much do you want to rotate by: '))
                break
            except ValueError:
                print('Error: enter a number.')

        message = input('Enter message to cypher: ')

        if operation.startswith('e'):
            operation = 'encoded'
            decode = False
        else:
            operation = 'decoded'
            decode = True

        print('-'*60)
        print(f'Here is your {operation} message: ')
        print(cypher(message, n, decode))
        print('-'*60)            

        while True: # input validation
            play_again = input('Do you want to play again: ').strip().lower()
            if play_again in ['yes', 'y', 'no', 'n']:
                break 

        if play_again.startswith('n'):
            replay = False
            print('-'*60)
            print('Goodbye!')
            print('-'*60)            


if __name__ == '__main__':
    main()
