from Cards import Cards
import random


class Deck:
    def __init__(self):
        self.deck = []

    def create_deck(self):
        for j in range(0, 4):  # color
            for i in range(7, 15):  # value
                self.deck.append(Cards(j, i))
        random.shuffle(self.deck)
