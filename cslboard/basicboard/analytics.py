from cslboard.basicboard.basicmodels import *
from cslboard.basicboard.mathmodels import *

class Analytics:
    def __init__(self, board: Board):
        self.board = board

    def find_math(self, length: int):
        return [Field(Vector2(1, 1), None), Field(Vector2(2, 1), None), Field(Vector2(3, 1), None)]