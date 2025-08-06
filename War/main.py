# Initializing Card Details:

from war_classes.card_details_ini import ranks, suits, values
from war_classes.card import Card
from war_classes.deck import Deck
from war_classes.player import Player

# Creating 2 Players:
player1 = Player('Bruce')
player2 = Player('Clark')


# Creating A New Deck of Cards:
new_deck = Deck()

# Shuffling The Deck:
new_deck.shuffle_deck()

# Dividing The Deck Between Two Players:
for index in range(26):
    player1.add_cards(new_deck.deal_one_card())
    player2.add_cards(new_deck.deal_one_card())


# Main Game Logic:
game_round = 0
game_on = True

while game_on:

    game_round += 1
    print(f'This is Round: {game_round}')

    # Checking if Either Player is out of Cards:
    if len(player1.all_cards) == 0:
        print(f'{player1.name} is OUT OF TROOPS!!')
        print(f'{player2.name} has WON!')
        break

    if len(player2.all_cards) == 0:
        print(f'{player2.name} is OUT OF TROOPS!!')
        print(f'{player1.name} has WON!')
        break

    # Starting a New Round and Resetting Cards on The Table:
    player1_cards_on_table = [player1.remove_card()]
    print(f"{player1.name}'s new card on Table: {player1_cards_on_table[-1]}")
    print(f"{player1.name} has {len(player1.all_cards)} cards.")

    player2_cards_on_table = [player2.remove_card()]
    print(f"{player2.name}'s new card on Table: {player2_cards_on_table[-1]}")
    print(f"{player2.name} has {len(player2.all_cards)} cards.")
    print('-' * 20)
    print('\n')
    while True:
        # Comparing Values of Cards on Top of The Table

        # Player1 Gets Card(s) from the Table:
        if player1_cards_on_table[-1].value > player2_cards_on_table[-1].value:
            player1.add_cards(player1_cards_on_table)
            player1.add_cards(player2_cards_on_table)
            break

        # Player2 Gets Card(s) from The Table:
        elif player1_cards_on_table[-1].value < player2_cards_on_table[-1].value:
            player2.add_cards(player1_cards_on_table)
            player2.add_cards(player2_cards_on_table)
            break

        # When Cards at Top of The Table has Same Value:
        else:
            print("THERE'S WAR FELLAS! Let's GO!!")

            # Checking if Player's have Enough Cards for War:
            if len(player1.all_cards) < 3:
                print(f'{player1.name} has INSUFFICIENT TROOPS for WAR!!')
                print(f'{player2.name} has WON!!')
                game_on = False
                break

            elif len(player2.all_cards) < 3:
                print(f'{player2.name} has INSUFFICIENT TROOPS for WAR!!')
                print(f'{player1.name} has WON!!')
                game_on = False
                break

            else:
                # Both Players have More Than 2 Cards, So we'll add Cards to The Table
                for i in range(3):
                    player1_cards_on_table.append(player1.remove_card())
                    player2_cards_on_table.append(player2.remove_card())