# War Card Game (Python):

A simple text based implementation of the classic “War” card game in Python.
Built as a practice project to apply object-oriented programming concepts using multiple files, classes, and game logic.

## 📋 Game Description:

War is a card game played between two players.

Each round, both players play the top card from their deck.

The player with the higher card value wins the round and collects both cards and moves them to their stack.

If the two cards played are of equal value, then there is a "war". Both players place the next card from their pile face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

## 🚀 What This Project Covers

- **Object-Oriented Design:** Player, Card, and Deck classes.
- **Deck Shuffling & Game Logic:** Random deck, comparison, card transfer.
- **Modular Coding:** Multi-file structure with imports.
- **CLI Gameplay:** Play in a text-based terminal interface.

## 🗂️ File Structure

- `main.py` – Starts and runs the game loop.
- `card.py` – Card class definition.
- `deck.py` – Deck class and shuffling logic.
- `player.py` – Player class and their hands.
- `card_details_ini.py` – Constants (e.g., card values, suits).

## 🧑‍💻 How to Run

1. Clone/download this repo
2. Make sure all `.py` files are in the same folder
3. Run in terminal:
   python main.py


## ✏️ What I Practiced

- Python OOP: classes, methods, instance vs class variables.
- Handling program structure with multiple .py files.
- Importing modules and managing game logic state.

---

*Created by Shailya Gandhi (https://github.com/Shailya777) as part of learning journey. Feedback and suggestions are very welcome!*
