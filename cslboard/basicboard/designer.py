from cslboard.basicboard import printer
from cslboard.basicboard import basicmodels

class Designer:

    def __init__(self, board: basicmodels.Board):
        self.board = board
        self.player_1 = None
        self.player_2 = None

    def boardsize(self):
        return self.board.size * 4 + self.board.size - 1 

    def __fieldname(self, field: basicmodels.Field):
        return chr(ord('@') + field.position.x + 1) + str(field.position.y + 1)

    def __print_cell(self, field: basicmodels.Field):
        if field.is_empty():
            printer.Printer.DarkSymbol(' {} '.format(self.__fieldname(field)))
        else:
            player = field.owner
            if self.player_1 == None: 
                self.player_1 = player
            elif self.player_2 == None:
                self.player_2 = player
            if self.player_1 == player:
                printer.Printer.RedSymbol(' {} '.format(player.player_name))
            else:
                printer.Printer.BlueSymbol(' {} '.format(player.player_name))

    def __draw_dash_raw(self):
            printer.Printer.DarkSymbol(' ')
            for i in range(self.board.size):
                printer.Printer.DarkSymbol('----')
                if i < self.board.size - 1:
                    printer.Printer.DarkSymbol('+')
            printer.Printer.DarkSymbol(' ')
            print() 

    def draw(self):
        def __print_empty_line():
            printer.Printer.DarkString(' ' * (self.boardsize() + 2))
        print()
        __print_empty_line()
        for raw in range(self.board.size):
            printer.Printer.DarkSymbol(' ')
            for column in range(self.board.size):
                self.__print_cell(self.board.fields[raw][column])
                if column != self.board.size - 1:
                    printer.Printer.DarkSymbol('|')
            printer.Printer.DarkSymbol(' ')
            print()
            if raw != self.board.size - 1:
                self.__draw_dash_raw()
        __print_empty_line()
        print()

