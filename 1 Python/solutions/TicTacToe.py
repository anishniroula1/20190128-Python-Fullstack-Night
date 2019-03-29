from collections import namedtuple
# # We can use a namedtuple instead of our Player class since we don't need to 
# # define any methods or modify the properties of Player
Player = namedtuple('Player', ['name', 'token'])

# class Player:
#   def __init__(self, name, token):
#       self.name = name 
#       self.token = token 

#   def __repr__(self):
#       return f'Player(name={name}, token={token})'

class Game:
    def __init__(self):
        """ initialize board as dict with keys as ints 1-9 and values all as None
        """
        self.board = {key:None for key in range(1,10)}

    def __repr__(self):
        """ represent board as each position separated by | 
        """
        board = ''
        for i in range(1,10,3):  # loop over rows, i = [1,4,7]
            row = {key: self.board[key] for key in range(i, i+3)}
            # print token if the space is occupied or the key if it is unoccupied
            row = [str(v) if v else str(k) for k,v in row.items()]
            board += '|'.join(row) + '\n' # add a new line for each row
        return board

    def __check_match(self, i, j, k):
        """ returns token of board values at positions i == j == k 
        """
        a = self.board[i]
        b = self.board[j]
        c = self.board[k]

        if (a == b == c) and (a is not None):
            return a

    def __is_full(self):
        """ returns true if self.board has no empty spaces
        """
        game_spaces = self.board.values()
        return all(game_spaces)

    def calc_winner(self):
        """ returns token if any horizontal, vertical, or diagonal match is found
        """
        for i in range(3):
            # horizontal matches
            # [1,2,3] or [4,5,6] or [7,8,9]
            match = self.__check_match(3*i+1, 3*i+2, 3*i+3)
            if match:
                return match

            # vertical matches
            # [1,4,7] or [2,5,8] or [3,6,9]
            match = self.__check_match(i+1, i+4, i+7)
            if match:
                return match 

        # diagonal matches
        match = self.__check_match(1, 5, 9)
        if match:
            return match

        match = self.__check_match(3, 5, 7)
        if match:
            return match

    def game_over(self):
        """ returns true if a player has one or the board is full
        """
        return self.calc_winner() or self.__is_full()

    def place_token(self, player, position):
        """ assigns player token at the board position if the board position is occupied
        """
        occupied = self.board[position]
        if occupied:
            raise ValueError
        self.board[position] = player.token


if __name__ == '__main__':
    player1 = Player(input('Enter player 1: '), 'X')
    player2 = Player(input('Enter player 2: '), 'O')
    # keep track of scores
    scores = {player1.token: 0, player2.token: 0}
    current_round = 1
    keep_playing = True

    while keep_playing:
        game = Game() # initialize game object

        while not game.game_over():
            # alternate players based on round number
            current_player = player1 if current_round % 2 else player2
            print(game) # print game board

            # place player token on board if they enter a legal move
            while True:
                move = input(f'{current_player.name}: Enter your move: ')
                try:
                    move = int(move)
                    if move < 1 or move > 9:
                        raise ValueError

                    move = game.place_token(current_player, move)
                    break

                except ValueError:
                    print('Invalid move. Enter an unoccupied number between 1 and 9.')

            current_round += 1 # increment round number

        # game over
        print(game) # print game board

        winner = game.calc_winner()
        if winner: # print winning player if one exists
            print(f"Winner: {winner}")
            scores[winner] += 1 # increment winner's score
        else: # no winner: stalemate
            print("Tie!")

        # print scores
        print('\nScores:')
        for player, score in scores.items():
            print(f'{player}: {score}')

        while True:
            play_again = input('\nDo you want to play again? ').strip().lower()
            if play_again in ['yes', 'y', 'no', 'n']:
                break

        if play_again.startswith('n'):
            keep_playing = False
            print('Goodbye!')