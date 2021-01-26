from cslboard.basicboard.simpleboard import PlayBoard
from cslboard.basicboard.basicmodels import Player

board = PlayBoard(4)
player_1 = Player("AL")
player_2 = Player("TV")
board.add_player(player_1)
board.add_player(player_2)

board.set_field(1, 2, player_1)
board.set_field(1, 3, player_1)
board.set_field(1, 1, player_1)
board.set_field(0, 1, player_2)
board.set_field(3, 3, player_2)
board.set_field(2, 2, player_2)

board.draw()

is_winner = board.is_winner(player_1)
print(str(is_winner))