from ticboard import TicBoard
import random
import os

def clearShell():
    os.system('cls' if os.name == 'nt' else 'clear')

class Match():

    def __init__(self, players):
        self.players = players
        self.board = TicBoard()
        self.turn = None
        self.complete = False

    def begin(self):
        self.turn = random.randrange(0,2)
        clearShell()
        print("Beginning Game, {} vs {}".format(self.players[0]['name'],self.players[1]['name']))
        #print(self.board.draw())
        print("First Turn will be {}".format(self.players[self.turn]['name']))
        str(input("Press Enter"))

    def end(self):
        clearShell()
        print(self.board.draw())
        if self.board.winnerID == -1:
            print("Draw!")
        else:
            print("{} Wins!".format(self.players[self.board.winnerID]['name']))
        str(input("Press Enter"))

    def nextTurn(self):
        player = self.players[self.turn]
        while True:
            if not player['computer']:
                clearShell()
                print(self.board.draw())
                print()
                playerInput = str(input("{} select a space: ".format(player['name'])))
                spaceNum = self.board.validSpace(playerInput.upper())
                while spaceNum == -1:
                    clearShell()
                    print(self.board.draw())
                    print("{} is not a valid space!".format(playerInput))
                    playerInput = str(input("{} select a space: ".format(player['name'])))
                    spaceNum = self.board.validSpace(playerInput.upper())
                self.board.place(player, spaceNum)
                self.complete = not self.board.canPlacePiece
                break
        self.nextPlayer()

    def nextPlayer(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0