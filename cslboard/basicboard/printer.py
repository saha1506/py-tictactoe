
class Printer:
    @classmethod
    def DarkSymbol(self, content: str):
        print('\x1b[2;37;40m' + content + '\x1b[0m', end='')
    @classmethod
    def DarkString(self, content: str):
        print('\x1b[2;37;40m' + content + '\x1b[0m')
    @classmethod
    def WhiteSymbol(self, content: str):
        print('\x1b[0;37;40m' + content + '\x1b[0m', end='')
    @classmethod
    def WhiteString(self, content: str):
        print('\x1b[0;37;40m' + content + '\x1b[0m')
    @classmethod
    def BlueSymbol(self, content: str):
        print('\x1b[1;34;40m' + content + '\x1b[0m', end='')
    @classmethod
    def RedSymbol(self, content: str):
        print('\x1b[1;31;40m' + content + '\x1b[0m', end='')
    @classmethod
    def RedString(self, content: str):
        print('\x1b[1;31;40m' + content + '\x1b[0m')

