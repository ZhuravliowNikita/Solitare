from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication
from DeckWidget import DeckWidget
import sys
from Deck import Deck
from Card import Card

class StockAndWastePileWidget(QWidget):
    def __init__(self, stock, waste, parent=None):
        super(StockAndWastePileWidget, self).__init__(parent)

        self.StockPileWidget = DeckWidget(stock)
        self.WastePileWidget = DeckWidget(waste)

        self.Layout = QHBoxLayout()
        self.Layout.addWidget(self.WastePileWidget)
        self.Layout.addWidget(self.StockPileWidget)

        self.setLayout(self.Layout)

        g = self.StockPileWidget.minimumSize()
        g.setWidth(g.width()+150)
        self.setMinimumSize(g)

        self.Layout.setContentsMargins(15, 0, 0, 0)
        self.Layout.setSpacing(3)

    def show(self) -> None:
        self.StockPileWidget.show()
        self.WastePileWidget.show()
        super(StockAndWastePileWidget, self).show()

    def refresh(self, stockPile, wastePile):
        self.StockPileWidget.refresh(stockPile)
        self.WastePileWidget.refresh(wastePile)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck = Deck(Card("6", "Clubs"))
    window = StockAndWastePileWidget(deck, deck)
    window.show()
    sys.exit(app.exec())