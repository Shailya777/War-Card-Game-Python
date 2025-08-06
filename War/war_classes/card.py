from card_details_ini import ranks, suits, values

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


if __name__ == '__main__':
    print('Testing Card Class:')
    print('=' * 10)

    c1 = Card('Spades', 'Ace')
    print(c1.suit)
    print(c1.rank)
    print(c1.value)
    print(c1)
    print('=' * 10)

    c2 = Card('Diamonds', 'Nine')
    print(c2.suit)
    print(c2.rank)
    print(c2.value)
    print(c2)