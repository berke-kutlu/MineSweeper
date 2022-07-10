# Piece Object With Attributes
class Piece(object):
    def __init__(self):
        self.mine = False
        self.clicked = False
        self.flagged = False
        self.mine_count = 0