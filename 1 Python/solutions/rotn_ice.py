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
    encoded = ''
    for char in message:
        index = alphabet.find(char)
        if index == -1: # if char is not a letter
            encoded += char
        else:
            encoded += translate[index]
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
            print('-'*60)
            print('Here is your encoded message: ')
            print(encode(message, n))
            print('-'*60)
        else:
            print('-'*60)
            print('Here is your decoded message: ')
            print(decode(message, n))
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