"""
# Blackjack.py
Blackjack module
"""
from Deck import Card, Deck

class Hand:
    """
    represents a player's hand
    """
    def __init__(self, card1, card2):
        self.cards = [card1, card2]

    def __repr__(self):
        ret = ''
        for card in self.cards:
            ret += str(card) + '\n'
        ret += f'Points: {self.points()}'
        return ret

    def add(self, card):
        """
        adds card to player's hand
        """
        if type(card) is Card:
            self.cards.append(card)
        else:
            raise TypeError('You can only add Card objects to a Hand')

    def points(self):
        """
        calculates points in player's hand
        """
        points = 0
        aces = 0
        for card in self.cards:
            if card.rank == 'A':
                aces += 1
            points += card.points

        while aces > 0 and points > 21:
            points -= 10
            aces -= 1

        return points

    def game_over(self):
        """
        returns 'Blackjack' if blackjack, 'Busted' if busted, or False otherwise
        """
        points = self.points()
        if points == 21:
            return 'Blackjack!'
        elif points > 21:
            return 'Busted'
        else:
            return False


class Dealer(Hand):
    """
    represents the dealer's hand
    """
    def __init__(self, card1, card2):
        super().__init__(card1, card2)

    def __repr__(self):
        ret = 'Card(Facedown)\n'
        for card in self.cards[1:]:
            ret += str(card) + '\n'
        ret += f'Points: {self.visible_points()}'
        return ret

        # # or you can extend the super __repr__
        # parent = super().__repr__()
        # parent = parent.split('\n')
        # ret = 'Card(Facedown)\n'
        # for card in parent[1:len(parent)-1]:
        #     ret += str(card) + '\n'
        # ret += f'Points: {self.visible_points()}'
        # return ret

    def visible_points(self):
        """
        returns points of all cards except the one face down
        """
        points = super().points()
        return points - self.cards[0].points

    def reveal(self):
        """
        reveal hidden card and total points
        """
        print(super().__repr__())

    def should_hit(self):
        """
        blackjack advice
        """
        return self.points() < 17


class Game:
    """
    contains logic for blackjack game
    """
    def __init__(self, cut_index=0, num_players=1):
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.cut(cut_index)
        self.players = [Hand(self.deck.draw(), self.deck.draw())
                        for i in range(num_players)]
        self.dealer = Dealer(self.deck.draw(), self.deck.draw())

    def play(self):
        """
        play a single blackjack game
        """
        player_finished = [False for i in range(len(self.players))]

        print('-'*60)
        print("Dealer's hand")
        print('-'*60)
        print(self.dealer)

        while not all(player_finished):
            for i, player in enumerate(self.players):
                print('-'*60)
                # skip over player if they are finished
                if player.game_over() or player_finished[i]:
                    print(f'Player {i+1} is finished')
                    player_finished[i] = True
                    continue

                print(f"Player {i+1}'s turn")
                print('-'*60)
                print(player)
                print('-'*60)

                invalid = True
                while invalid:
                    move = input("Do you want to hit or stay? \n>").strip().lower()
                    if move in ['h', 'hit', 's', 'stay']:
                        invalid = False

                if move.startswith('h'): # draw a card and add it to player's hand
                    player.add(self.deck.draw()) 
                    print(player)

                if move.startswith('s'):
                    player_finished[i] = True


        print('-'*60)
        print("Dealer's turn")
        print('-'*60)
        while self.dealer.should_hit():
            print('Dealer hits')
            print('-'*60)        
            self.dealer.add(self.deck.draw())
            print(self.dealer)

        # reveal final hands and results
        print('-'*60)
        print("Dealer's hand")
        print('-'*60)
        self.dealer.reveal()

        for i, player in enumerate(self.players):
            print('-'*60)
            print(f"Player {i+1}'s hand")
            print('-'*60)
            print(player)

            points = player.points()
            dealer_points = self.dealer.points()
            if points == 21:
                print('Blackjack!')
            elif (points > 21) or points <= dealer_points <= 21:
                print('You lose :(')
            else:
                print('You win!')


def main():
    loop = True
    while loop:
        while True:
            try:
                num_players = int(input('How many players? \n>'))
                break
            except ValueError:
                pass

        while True:
            try:
                cut_index = int(input('Cut the deck \n>'))
                break
            except ValueError:
                print('Enter index to cut deck by.')

        game = Game(num_players=num_players)
        game.play()

        while True:
            play_again = input('Do you want to play again? \n>').strip().lower()
            if play_again in ['yes', 'y', 'no', 'n']:
                break

        if play_again.startswith('n'):
            loop = False


if __name__ == '__main__':
    main()
