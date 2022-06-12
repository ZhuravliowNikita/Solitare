from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import uic
from cards import Cards
from Deck import Deck
import sys

class Signals(QObject):
    dropCard = pyqtSignal(str, int)


class DeckWidget(QPushButton):
    def __init__(self, deck, parent=None):
        super(DeckWidget, self).__init__(parent)
        self.Layout = QVBoxLayout(self)
        self.ui = uic.loadUi("emptyDeck.ui")
        self.LastCard = Cards(deck[-1])
        self.LastCard.clicked.connect(self.clicked)
        self.deck = deck

        self.signals = Signals()

        self.Layout.addWidget(self.ui)
        self.Layout.addWidget(self.LastCard)

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.ui.minimumSize())
        self.setMaximumSize(self.ui.maximumSize())
        self.setLayout(self.Layout)


    def refresh(self, deck):
        self.deck = deck
        self.LastCard.setCard(self.deck[-1])

    def show(self) -> None:
        if self.deck.isEmpty():
            self.ui.show()
            self.LastCard.hide()
        else:
            self.refresh(self.deck)
            self.ui.hide()
            self.LastCard.show()
        super(DeckWidget, self).show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = Deck()
    window = DeckWidget(deck)
    window.show()
    sys.exit(app.exec())