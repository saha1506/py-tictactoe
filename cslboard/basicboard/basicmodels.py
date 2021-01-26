from cslboard.basicboard import mathmodels


class Board:
    def __init__(self, size: int):
        self.size = size
        self.fields = [[Field.empty(mathmodels.Vector2(j, i)) for j in range(size)] for i in range(size)]

class Player:
    def __init__(self, name: str):
        self.player_name = str(name)
    
    def __str__(self):
        return self.player_name

class Field:
    def __init__(self, position: mathmodels.Vector2, owner: Player):
        self.position = position
        self.owner = owner
    @classmethod
    def empty(cls, position: mathmodels.Vector2):
        return Field(position, None)
    def chowner(self, owner: Player):
        self.owner = owner
    def is_empty(self):
        return self.owner == None

    