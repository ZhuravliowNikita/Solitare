from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from GameZone import Gamezone
from GamePlay import GamePlay
from PyramideWidget import PyramideWidget
from SWPile import StockAndWastePileWidget
import sys


class Solitare(QWidget):
    def __init__(self, parent = None):
        super(Solitare, self).__init__()
        self.ui = uic.loadUi("Solitare.ui")
        self.GameZone = Gamezone()
        self.GamePlay = GamePlay(self.GameZone)
        self.SWPile = StockAndWastePileWidget(self.GameZone.stockpile, self.GameZone.wastepile)
        self.PyramideWidget = PyramideWidget(self.GameZone.pyramide)
        self.SWPile.StockPileWidget.clicked.connect(self.stockPileWidgetClicked)
        self.SWPile.WastePileWidget.clicked.connect(self.wastePileWidgetClicked)
        self.PyramideWidget.signal.cardClicked.connect(self.cardClicked)
        self.ui.layout().addWidget(self.SWPile)
        self.ui.layout().addWidget(self.PyramideWidget)

        self.setLayout(self.ui.layout())
    def show(self):
        self.SWPile.show()
        self.PyramideWidget.show()
        super().show()

    def stockPileWidgetClicked(self):
        if self.GameZone.stockpile.isEmpty():
            self.GamePlay.sendToStockPileFromWastePile()
        else:
            self.GamePlay.sendToWastePileFromStockPile()
        self.refresh()

    def refresh(self):
        self.SWPile.refresh(self.GameZone.stockpile, self.GameZone.wastepile)
        self.PyramideWidget.refresh(self.GameZone.pyramide)
        self.show()

    def wastePileWidgetClicked(self):
        self.GamePlay.choiceCardinWaste()
        self.GamePlay.isCompare()
        self.refresh()

    def cardClicked(self, cardIndex, rowIndex):
        self.GamePlay.choiceCardinPyramide(rowIndex, cardIndex)
        self.GamePlay.isCompare()
        self.refresh()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Solitare()
    window.show()
    sys.exit(app.exec())