from GameZone import Gamezone



class GamePlay:
    def __init__(self, gamezone):
        self.gamezone = gamezone
        self.playerchoice = []


    def cardCompare(self):
        sum = 0
        for card in self.playerchoice:
            sum += int(card.rank)
        if sum == 13:
            return True
        return False


    def Deside(self):
        for card in self.playerchoice:
            self.findAndPop(card)


    def choiceCardinPyramide(self, index, cardindex):
        card = self.gamezone.pyramide[index][cardindex]
        if  card.islocked():
            self.playerchoice.append(card)
    def choiceCardinWaste(self):
        card = self.gamezone.wastepile[-1]
        if card is not None:
            self.playerchoice.append(card)


    def gameisend(self):
        if self.gamezone.pyramide == []:
            return True
        return False

    def appendToWastePile(self, card):
        if not card.isCardVisible:
            card.flip()
        self.gamezone.wastepile.append(card)

    def appendToStockPile(self, deck):
        if len(deck) != 0:
            deck.hideAllCardsStats()
            self.gamezone.stockpile.append(deck)


    def sendToWastePileFromStockPile(self):
        deck = self.gamezone.stockpile.pop(-1)
        self.appendToWastePile(deck)

    def sendToStockPileFromWastePile(self):
        deck = self.gamezone.wastepile.popAllCards()
        deck.reverse()
        self.appendToStockPile(deck)
    def isCompare(self):
        if len(self.playerchoice) > 2:
            self.playerchoice.clear()
            return False

        if self.cardCompare():
            self.Deside()
            self.playerchoice.clear()
    def findAndPop(self, card):
        if card == self.gamezone.wastepile[-1]:
            card1 = self.gamezone.wastepile.pop(-1)
        for Row in self.gamezone.pyramide:
            index = Row.getIndex(card)
            if index is not None:
                card2 = Row.pop(index)
                self.deleteCardChild(card2)
                return None

    def deleteCardChild(self, card1):
        for Row in self.gamezone.pyramide:
            for card in Row:
                if card.leftcard == card1:
                    card.leftcard = None
                if card.rightcard == card1:
                    card.rightcard = None