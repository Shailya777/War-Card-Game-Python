import random
from card import Card
from card_details_ini import ranks, suits, values

class Deck:

    def __init__(self):

        self.all_cards = [] # Empty list / Deck of Cards.

        for suit in suits:
            for rank in ranks:
                temp_card = Card(suit, rank)
                self.all_cards.append(temp_card)


    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        return self.all_cards.pop()


if __name__ == '__main__':
    print('Testing Deck Class:')
    print('=' * 100)

    d1 = Deck()
    for card in d1.all_cards:
        print(card)

    print('=' * 100)

    d1.shuffle_deck()
    for card in d1.all_cards:
        print(card)

    temp = d1.deal_one_card()
    print(temp)
    print(temp.rank)
    print(temp.suit)
    print(temp.value)