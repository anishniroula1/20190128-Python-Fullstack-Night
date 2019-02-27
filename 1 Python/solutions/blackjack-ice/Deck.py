"""
# Deck.py
Card and Deck classes
"""
from random import shuffle as rand_shuf


class Card:
    """
    Card represented by suit and rank
    """

    def __init__(self, rank, suit):
        points = {'A': 1}
        nums = dict(zip(range(2,11), range(2,11)))
        face = {k: 10 for k in 'JQK'} 
        points.update(nums)
        points.update(face)

        self.rank = rank
        self.suit = suit
        self.points = points.get(rank)

    def __repr__(self):
        return f'Card({self.rank} of {self.suit})'

    def __eq__(self, card):
        return self.rank == card.rank

    def __ne__(self, card):
        return self.rank != card.rank


class Deck:
    """
    Deck as a list of card
    """

    def __init__(self):
        ranks = ['A'] + list(range(2, 11)) + list('JQK') 
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        # # equivalent to above
        # for suit in suits:
        #     for rank in ranks:
        #         self.cards.append(Card(rank, suit))

    def __repr__(self):
        cards = ''
        for card in self.cards:
            cards += str(card) + '\n'
        return cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    # def __add__(self, deck):
    #     return self.cards + deck.cards

    def shuffle(self):
        """
        shuffles cards in place
        """
        rand_shuf(self.cards)

    def cut(self, index):
        """
        cuts the deck at index
        """
        self.cards = self.cards[index:] + self.cards[:index]

    def draw(self):
        """
        pops card off top of deck
        """
        return self.cards.pop()        


deck = Deck()
print(len(deck))
card1 = deck.cards[0]
card2 = deck.cards[1]
card3 = deck.cards[13]
card4 = card1
card5 = Card('A', 'Clubs')
print(card1, '=', card2, card1 == card2)
print(card1, '!=', card2, card1 != card2)
print(card1, '=', card3, card1 == card3)
print(card1, '!=', card3, card1 != card3)
print(card1, '==', card4, card1 == card4)
print(card1, '==', card5, card1 == card5)
print(card1.points)
print(Card(2, 'Clubs').points)
print(Card(9, 'Clubs').points)
print(Card('J', 'Hearts').points)
print(Card('Q', 'Hearts').points)
print(Card('K', 'Hearts').points)
print(deck[-1])
deck.shuffle()
deck2 = Deck()
deck2.cut(150)
print(deck2)