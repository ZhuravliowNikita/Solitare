from Card import Card

class CardinRow(Card):
    def __init__(self, card, leftcard=None, rightcard=None):
        super(CardinRow, self).__init__(card.rank, card.mark)
        self.leftcard = leftcard
        self.rightcard = rightcard

    def islocked(self):
        if self.leftcard == None and self.rightcard == None:
            return True
        return False
