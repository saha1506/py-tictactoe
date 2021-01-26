from cslboard.basicboard import mathmodels
from cslboard.basicboard import designer
from cslboard.basicboard import basicmodels
from cslboard.basicboard import analytics


class PlayBoard:
    def __init__(self, size: int):
        self.size = size
        self.board = basicmodels.Board(size)
        self.designer = designer.Designer(self.board)
        self.analytics = analytics.Analytics(self.board)
        self.players = []

    def set_field(self, x: int, y: int, player: basicmodels.Player):
        self.board.fields[x][y].chowner(player)

    def draw(self):
        self.designer.draw()

    def add_player(self, player: basicmodels.Player):
        self.players.append(player)

    def is_winner(self, player: basicmodels.Player):
        match = self.analytics.find_math(3)
        return len(match) >= 3