from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from cards import Cards
import sys
from GameZone import Gamezone
from PyQt5.QtCore import QObject, pyqtSignal

class Signals(QObject):
    cardClicked = pyqtSignal(int, int)
class PyramideWidget(QWidget):
    def __init__(self, pyramide, parent = None):
        super(PyramideWidget, self).__init__(parent)
        self.pyramide = pyramide
        self.ui = uic.loadUi("Pyramide.ui")
        self.cardwidget = []
        self.rows = [self.ui.Row1, self.ui.Row2, self.ui.Row3,
                     self.ui.Row4, self.ui.Row5, self.ui.Row6, self.ui.Row7]
        self.refresh(self.pyramide)
        self.signal = Signals()
        self.setLayout(self.ui.layout())

    def refresh(self, pyramide):
        self.pyramide = pyramide
        self.hideCards()
        self.deleteCards()
        self.cardwidget.clear()
        for Row in self.pyramide:
            for card in Row:
                cardWidget = self.addCardWidget(card)
                self.rows[Row.index].addWidget(cardWidget)

        self.cardConnect()
        self.showCards()

    def cardClickedHandle(self):
        indexes = self.findCard(self.sender().card)
        self.signal.cardClicked.emit(indexes[0], indexes[1])

    def findCard(self, card):
        cardIndex = None
        for index, Row in enumerate(self.pyramide):
            cardIndex = Row.getIndex(card)
            if cardIndex is not None:
                return(cardIndex, Row.index)
        return None

    def hideCards(self):
        for child in self.cardwidget:
            child.hide()

    def deleteCards(self):
        for child in self.cardwidget:
            child.deleteLater()

    def showCards(self):
        for child in self.cardwidget:
            child.show()

    def addCardWidget(self, card):
        self.cardwidget.append(Cards(card, parent=self))
        return self.cardwidget[-1]

    def cardConnect(self):
        for child in self.cardwidget:
            child.clicked.connect(self.cardClickedHandle)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Pyramide = Gamezone().pyramide
    window = PyramideWidget(Pyramide)
    window.show()
    sys.exit(app.exec())