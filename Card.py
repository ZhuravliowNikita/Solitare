from copy import deepcopy
class Card:
    def __init__(self, rank, mark, isCardVisible=True):
        self.rank = rank
        self.mark = mark
        self.isCardVisible = isCardVisible

    def flip(self):
        self.isCardVisible = not self.isCardVisible

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if value in CardRank:
            self._rank = value


    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        if value in CardSuit:
            self._mark = value

    def __str__(self):
        return f"{self.rank} | {str(self.mark)}"
    def __del__(self):
        del(self._rank)
        del(self._mark)
        del(self.isCardVisible)


CardSuit = ["Clubs", "Hearts", "Pikes", "Tiles"]
CardRank = [str(i) for i in range(1,14,1)]