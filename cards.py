from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton
from PyQt5 import uic, QtGui
from Card import Card
import sys



class Cards(QPushButton):
    def __init__(self, card = None, parent=None,):
        super().__init__(parent)
        self.card = card
        self.statecard = False
        self.frontSide = uic.loadUi("C:/Users/User/PycharmProjects/тымчук проект/rubashka_for_card.ui")
        self.backSide = uic.loadUi("C:/Users/User/PycharmProjects/тымчук проект/cardstats.ui")

        self.setCard(self.card)
        self.Layout = QVBoxLayout(self)
        self.Layout.addWidget(self.frontSide)
        self.Layout.addWidget(self.backSide)
        self.setLayout(self.Layout)
        self.setMaximumSize(self.backSide.maximumSize())
        self.setMinimumSize(self.backSide.maximumSize())
        self.Layout.setContentsMargins(0, 0, 0, 0)

    def show(self):
        if self.statecard:
            self.frontSide.hide()
            self.backSide.show()
        else:
            self.frontSide.show()
            self.backSide.hide()
        super().show()

    def setCard(self, card):
        self.card = card
        if self.card is not None:
            self.backSide.suit.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("cards/"+card_view[self.card.rank+self.card.mark]+".bmp")))
            self.statecard = self.card.isCardVisible


card_view = {"1Hearts":"1ch",
             "2Hearts":"2ch",
             "3Hearts":"3ch",
             "4Hearts":"4ch",
             "5Hearts":"5ch",
             "6Hearts":"6ch",
             "7Hearts":"7ch",
             "8Hearts":"8ch",
             "9Hearts":"9ch",
             "10Hearts":"10ch",
             "11Hearts":"11ch",
             "12Hearts":"12ch",
             "13Hearts":"13ch",
             "1Clubs":"1kr",
             "2Clubs":"2kr",
             "3Clubs":"3kr",
             "4Clubs":"4kr",
             "5Clubs":"5kr",
             "6Clubs":"6kr",
             "7Clubs":"7kr",
             "8Clubs":"8kr",
             "9Clubs":"9kr",
             "10Clubs":"10kr",
             "11Clubs":"11kr",
             "12Clubs":"12kr",
             "13Clubs":"13kr",
             "1Pikes":"1pi",
             "2Pikes":"2pi",
             "3Pikes":"3pi",
             "4Pikes":"4pi",
             "5Pikes":"5pi",
             "6Pikes":"6pi",
             "7Pikes":"7pi",
             "8Pikes":"8pi",
             "9Pikes":"9pi",
             "10Pikes":"10pi",
             "11Pikes":"11pi",
             "12Pikes":"12pi",
             "13Pikes":"13pi",
             "1Tiles":"1by",
             "2Tiles":"2by",
             "3Tiles":"3by",
             "4Tiles":"4by",
             "5Tiles":"5by",
             "6Tiles":"6by",
             "7Tiles":"7by",
             "8Tiles":"8by",
             "9Tiles":"9by",
             "10Tiles":"10by",
             "11Tiles":"11by",
             "12Tiles":"12by",
             "13Tiles":"13by",
             }

if __name__ == "__main__":
    app = QApplication(sys.argv)
    card = Card("6", "Tiles")
    window = Cards(card)
    window.statecard = True
    window.ShowCard()
    window.show()
    sys.exit(app.exec())






















