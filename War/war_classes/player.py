class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = [] # A player has no cards initially.

    def add_cards(self, cards):

        if type(cards) == type([]): # If There are multiple cards to add to player's deck (List of Cards)
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards) # if a single card is to be added to Player's Deck.

    def remove_card(self):
        return self.all_cards.pop(0) # Removing a Card from The Top of Player's Deck.

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards.'

# Un-Comment The Following Code to Test The Module Independently.
# if __name__ == '__main__':
#     print('Testing Player Class:')
#     from card import Card
#     from deck import Deck
#     from card_details_ini import ranks, suits, values

#     player1 = Player('Shailya')
#     print(player1)
#     print(player1.name)

#     print('-----------------------------')
#     c1 = Card('Spades', 'Three')
#     player1.add_cards(c1)
#     print(player1)

#     print('-----------------------------')
#     c2 = Card('Hearts', 'Queen')
#     c3 = Card('Clubs', 'King')
#     player1.add_cards([c2, c3])
#     print(player1)

#     print('-----------------------------')
#     removed_card = player1.remove_card()
#     print(removed_card)

#     print(player1)
