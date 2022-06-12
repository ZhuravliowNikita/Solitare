from Card import Card
from StackIterator import StackIterator

class Deck:
    def __init__(self, deck=None):
        self.deck = []
        self.append(deck)

    def append(self, deck):
        if deck is None or deck == []:
            return
        if isinstance(deck, Card):
            self.deck.append(deck)
        elif isinstance(deck, list):
            for card in deck:
                self.append(card)
        elif isinstance(deck, Deck):
            self.append(deck.copycards())

    def copycards(self):
        return self.deck.copy()

    def pop(self, index):
        return self.deck.pop(index)

    def popAllCards(self):
        temp = self.copycards()
        self.deck.clear()
        return Deck(temp)


    def getIndex(self, card):
        for index, item in enumerate(self.deck):
            if item == card:
                return index
        return None

    def showAllCardsStats(self):
        for card in self:
            if not card.isCardVisible:
                card.flip()

    def hideAllCardsStats(self):
        for card in self:
            if card.isCardVisible:
                card.flip()

    def reverse(self):
        self.deck = self.deck[::-1]

    def __iter__(self):
        return StackIterator(self.deck)

    def __getitem__(self, item):
        if self.isEmpty():
            return None
        if isinstance(item, int):
            return self.deck[item]
        return None

    def __len__(self):
        return len(self.deck)

    def isEmpty(self):
        if len(self) == 0:
            return True
        return False