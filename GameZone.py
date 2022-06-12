from Card import Card, CardSuit, CardRank
from random import randint
from Deck import Deck
from CardInRow import CardinRow
from Row import Row


class Gamezone:
    def __init__(self):
        self.stockpile = Deck()
        self.wastepile = Deck()
        self.pyramide = [Row(None, index=i) for i in range(7)]
        self.fill()

    def fill(self):
        startdeck = Deck()
        for suit in CardSuit:
            for rank in CardRank:
                startdeck.append(Card(rank, suit))

        self.fillPyramide(startdeck)
        self.fillstockpile(startdeck)

    def fillPyramide(self, deck):
        capacity = 1
        for row in self.pyramide:
            i = 0
            while i < capacity:
                card = CardinRow(deck.pop(randint(0, len(deck)-1)))

                row.append(card)
                i+=1
            capacity += 1
        for index, row in enumerate(self.pyramide):
            if index > len(self.pyramide)-2:
                continue
            for cardindex, card in enumerate(row):
                card.leftcard = self.pyramide[index+1][cardindex]
                card.rightcard = self.pyramide[index+1][cardindex+1]

    def fillstockpile(self, deck):
        while len(deck) > 0:
            card = deck.pop(randint(0, len(deck)-1))
            card.flip()
            self.stockpile.append(card)





