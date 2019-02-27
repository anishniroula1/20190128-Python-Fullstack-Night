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
        for card in self.cards:
            points += card.points
        return points


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

    def visible_points(self):
        """
        returns points of all cards except the one face down
        """
        points = 0
        for card in self.cards[1:]:
            points += card.points
        return points

    def reveal(self):
        print(super().__repr__())


deck = Deck()
deck.shuffle()
player = Hand(deck.draw(), deck.draw())
print(player)
player.add(deck.draw())
print(player)
dealer = Dealer(deck.draw(), deck.draw())
print(dealer)
dealer.reveal()