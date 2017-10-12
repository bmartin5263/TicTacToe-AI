from match import Match
import sys

def getComputerName(players):
    names = ['SkyNet', 'Watson']
    for name in names:
        for player in players:
            if player['name'] == name:
                break
        else:
            return name

def getComputerSymbol(players):
    symbols = ['X', 'O']
    for symbol in symbols:
        for player in players:
            if player['symbol'] == symbol or player['symbol'] == symbol.lower():
                break
        else:
            return symbol

def nameLegal(name, players):
    for player in players:
        if player['name'] == name:
            return False
    return True

def symbolLegal(symbol, players):
    if len(symbol) < 1 or symbol == ' ':
        return False
    symbol = symbol[0]
    for player in players:
        if player['symbol'] == symbol:
            return False
    return True

def main():
    players = []
    numPlayers = 0
    if len(sys.argv) > 1:
        try:
            numPlayers = sys.argv[1]
        except ValueError:
            pass
    if numPlayers < 1:
        while True:
            playerInput = str(input("\n1 or 2 Players: "))
            try:
                numPlayers = int(playerInput)
            except ValueError:
                pass
            if 0 <= numPlayers <= 2:
                break

    if numPlayers == 0:
        for i in range(2):
            computerName = getComputerName(players)
            computerSymbol = getComputerSymbol(players)
            computer = {'id': i, 'name': computerName, 'symbol': computerSymbol, 'computer': True}
            players.append(computer)
    else:
        i = 0
        for i in range(numPlayers):
            player = {'id': i, 'name': '', 'symbol': '', 'computer': False}
            nameInput = str(input("Player {} Please Enter Your Name: ".format(i + 1))).title()
            while not nameLegal(nameInput, players):
                print("Name Already Used!")
                nameInput = str(input("Player {} Please Enter Your Name: ".format(i + 1))).title()
            player['name'] = nameInput
            symbolInput = str(input("Player {} Choose a Symbol: ".format(i + 1)))
            while not symbolLegal(symbolInput, players):
                print("Symbol Invalid!")
                symbolInput = str(input("Player {} Choose a Symbol: ".format(i + 1)))
            player['symbol'] = symbolInput[0]
            players.append(player)

        for i in range(i+1, 2):
            computerName = getComputerName(players)
            computerSymbol = getComputerSymbol(players)
            computer = {'id': i, 'name': computerName, 'symbol': computerSymbol, 'computer': True}
            players.append(computer)

    for i in range(3):
        m = Match(players)
        m.begin()
        while not m.complete:
            m.nextTurn()
        m.end()


if __name__ == '__main__':
    main()