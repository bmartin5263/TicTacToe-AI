class TicBoard():

    SPACE_NAMES = [
        'TL', 'TM', 'TR',
        'CL', 'CM', 'CR',
        'BL', 'BM', 'BR'
    ]

    SPACE_NAMES_REVERSED = [
        'LT', 'MT', 'RT',
        'LC', 'MC', 'RC',
        'LB', 'MB', 'RB'
    ]

    TRIADS = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    def __init__(self):
        self.spaces = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.free = 9
        self.canPlacePiece = True
        self.winnerID = -1

    def checkWin(self):
        for triad in TicBoard.TRIADS:
            for i in range(1, len(triad)):
                checkSymbol = self.spaces[triad[i]]
                if checkSymbol == ' ' or checkSymbol != self.spaces[triad[i-1]]:
                    break
            else:
                return True
        return False

    def draw(self):
        out = "\n\t   L   M   R\n"
        out += "\tT: {} | {} | {} \n".format(self.spaces[0], self.spaces[1], self.spaces[2])
        out += "\t  -----------\n"
        out += "\tC: {} | {} | {} \n".format(self.spaces[3], self.spaces[4], self.spaces[5])
        out += "\t  -----------\n"
        out += "\tB: {} | {} | {} \n".format(self.spaces[6], self.spaces[7], self.spaces[8])
        return out

    def place(self, player, space):
        self.spaces[space] = player['symbol']
        self.free -= 1
        if self.checkWin():
            self.winnerID = player['id']
            self.canPlacePiece = False
        elif self.free == 0:
            self.canPlacePiece = False

    def validSpace(self, playerInput):
        for i in range(9):
            if playerInput == TicBoard.SPACE_NAMES[i] or playerInput == TicBoard.SPACE_NAMES_REVERSED[i]:
                if self.spaces[i] == ' ':
                    return i
                else:
                    return -1
        return -1