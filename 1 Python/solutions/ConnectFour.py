# ConnectFour.py
from collections import namedtuple

Player = namedtuple('Player', ['name', 'color'])

# class Player:
#   def __init__(self, name, color):
#       self.name = name 
#       self.color = color

class Game:
    DEPTH = 6
    WIDTH = 7

    def __init__(self):
        self.board = [['-' for x in range(self.WIDTH)] for y in range(self.DEPTH)]

    def __repr__(self):
        board = ''
        for row in self.board:
            board += '|'.join(row) + '\n'
        return board

    def __get_height(self, position):
        counter = 0
        for i in range(len(self.board)-1, -1, -1):
            find_token = self.board[i][position-1]
            if find_token == '-':
                break
            counter += 1
        return counter

    def move(self, player, position):
        x = position - 1
        y = 5 - self.__get_height(position)
        if y < 0:
            raise IndexError('Error: Column full. Choose another')
        self.board[y][x] = player.color

    def calc_winner(self):
        for y in range(self.DEPTH-1, -1, -1):
            for x in range(self.WIDTH):
                # check horizontal win
                if x < self.WIDTH-3:
                    chunk = self.board[y][x:x+4]
                    if all(item == self.board[y][x] and item != '-' for item in chunk):
                        return self.board[y][x]

                # check vertical win
                if y < self.DEPTH-3:
                    chunk = []
                    chunk.append(self.board[y][x])
                    chunk.append(self.board[y+1][x])
                    chunk.append(self.board[y+2][x])
                    chunk.append(self.board[y+3][x])
                    if all(item == self.board[y][x] and item != '-' for item in chunk):
                        return self.board[y][x]

                # check diagonal wins
                if y < self.DEPTH-3 and x < self.WIDTH-3:
                    chunk = []
                    chunk.append(self.board[y][x:x+4])
                    chunk.append(self.board[y+1][x:x+4])
                    chunk.append(self.board[y+2][x:x+4])
                    chunk.append(self.board[y+3][x:x+4])

                    if chunk[0][0] == chunk[1][1] == chunk[2][2] == chunk[3][3] and chunk[0][0] != '-':
                        return chunk[0][0]
                    elif chunk[3][0] == chunk[1][2] == chunk[2][1] == chunk[0][3] and chunk[3][0] != '-':
                        return chunk[3][0]
        

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == '-':
                    return False
        return True

    def is_game_over(self):
        return self.calc_winner() or self.is_full()


if __name__ == '__main__':
    game = Game()
    player1 = Player('1', 'Y')
    player2 = Player('2', 'R')
    current_round = 1

    while not game.is_game_over():
        print(game)
        if current_round % 2 != 0:
            current_player = player1 
        else:
            current_player = player2

        while True:
            move = input('Enter your move: ')
            try:
                position = int(move)
                if position < 1 or position > 7:
                    raise ValueError
                game.move(current_player, position)
                break
            except ValueError:
                print('Error: Enter a number between 1 and 7.')
            except IndexError as e:
                print(e)

        current_round += 1

    print(game)
    # calculate winner
    winner = game.calc_winner()
    if winner:
        print(f'{winner} wins!')
    else:
        print("You're all losers!")
