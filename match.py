from ticboard import TicBoard
import random
import os
import copy

def clearShell():
    os.system('cls' if os.name == 'nt' else 'clear')

class Match():

    CENTER = 4
    CORNERS = (0,2,6,8)

    def __init__(self, players):
        self.players = players
        self.board = TicBoard()
        self.turn = None
        self.complete = False
        self.winner = -1

    def begin(self):
        # self.turn = random.randrange(0,2)
        self.turn = 0
        clearShell()
        print("Beginning Game, {} vs {}".format(self.players[0]['name'],self.players[1]['name']))
        print("First Turn will be {}".format(self.players[self.turn]['name']))
        str(input("Press Enter"))

    def end(self):
        clearShell()
        print(self.board.draw())
        if self.winner == -1:
            print("Draw!")
        else:
            print("{} Wins!".format(self.players[self.winner]['name']))
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
                break

            else:
                print(self.board.draw())
                print()
                if self.board.free == 9:
                    bestMove = (0,random.choice((Match.CENTER, random.choice(Match.CORNERS))))
                else:
                    bestMove = self.think(self.turn, self.board, 0)
                spaceNum = bestMove[1]
                break

        self.board.place(player['symbol'], spaceNum)

        victory = self.board.checkWin()
        if victory or self.board.free == 0:
            self.complete = True
            if victory:
                self.winner = self.turn

        self.turn = self.nextPlayer(self.turn)

    def nextPlayer(self, turn):
        if turn == 0:
            return 1
        else:
            return 0

    def think(self, player, board, depth):

        #Base Case

        victory = board.checkWin()
        if victory and (depth-1) % 2 != 0:
            return [-10+depth, None]
        elif victory and (depth-1) % 2 == 0:
            return [10-depth, None]
        elif board.free == 0:
            return [0, None]

        moves = []

        for i, space in enumerate(self.board.spaces):
            if space == ' ':
                move = [0, i]
                self.board.place(self.players[player]['symbol'], i)
                move[0] += self.think(self.nextPlayer(player), self.board, depth+1)[0]
                moves.append(move)
                self.board.place(' ', i)

        if depth % 2 == 0:
            if depth == 0:
                for move in moves:
                    print(move)
                str(input())
            return max(moves, key=lambda v: v[0])
        else:
            return min(moves, key=lambda v: v[0])