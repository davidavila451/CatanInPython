import random
import the_table
import the_players
import card_magic
import coin_operated_bois

RED = "\x1b[31m"
GREEN = "\x1b[32m"
BLUE = "\x1b[34m"
MAG = "\x1b[35m"

#Start of main biz
table = the_table.Board()
cards = card_magic.Deck()
player = the_players.Player()
bot1 = coin_operated_bois.Bot()
bot2 = coin_operated_bois.Bot()
bot3 = coin_operated_bois.Bot()
userInput = ""
players = [player, bot1, bot2, bot3]
playerTurnOrder = []
availColors = [RED, GREEN, BLUE, MAG]
clearFlag = -1

#Determine Player Order
while len(playerTurnOrder) < 4:
    playerTurn = random.randint(0,len(players)-1)
    playerTurnOrder.append(players[playerTurn])
    players.remove(players[playerTurn])

#Pre Setup Loop
while(clearFlag != 0):
    userInput = input("""
Select a player color:
1. RED
2. GREEN
3. BLUE
4. MAGENTA
""")
    match(userInput):
        case "1":
            player.COLOR = RED
            availColors.remove(RED)
            clearFlag = 0
        case "2":
            player.COLOR = GREEN
            availColors.remove(GREEN)
            clearFlag = 0
        case "3":
            player.COLOR = BLUE
            availColors.remove(BLUE)
            clearFlag = 0
        case "4":
            player.COLOR = MAG
            availColors.remove(MAG)
            clearFlag = 0
        case _:
            print(f"Invalid selection: {userInput}")
            clearFlag = -1

bot1.COLOR = availColors[0]
bot2.COLOR = availColors[1]
bot3.COLOR = availColors[2]

#Setup Loop
turnCounter = 0
while(turnCounter != 2):
    for player in playerTurnOrder:
        table.printBoard()
        player.initialSetUp(table)
        

#Main Game Loop
while(True):
    table.printBoard()
    player.onTurn(table, cards)
    