import the_table
import the_players
import card_magic

#Start of main biz
table = the_table.Board()
cards = card_magic.Deck()
player = the_players.Player()
userInput = ""

#Setup Loop
while(userInput != "quit" and (player.availableCities > 0 or player.availableRoads > 0)):
    #Build town
    if(player.availableCities > 0):
        table.printBoard()
        clearFlagA = -1
        while clearFlagA != 0:
            userInput = input(f"""
Select where you would like to build a city.
Enter the tile ID (top number) followed by position:
Ex. 4-TL would place a town on tile 4 in the (T)op (L)eft.
                        
You have {str(player.availableCities)} left to place.
""")
            if(userInput == "quit"):
                quit()
            previousPoint = userInput
            clearFlagA = table.gameLogic.buildTown(player, table, userInput)

    #Build road
    if(player.availableRoads > 0):
        table.printBoard()
        clearFlagB = -1
        while clearFlagB != 0:
            userInput = input(f"""
Select the point you would like to build your road to
from the town you just built.
Enter the tile ID (top number) followed by position:
Ex. 4-TR would place a road to tile (4) in the (T)op (R)ight.
                    
You have {str(player.availableRoads)} left to place.
""")
            if(userInput == "quit"):
                quit()
            clearFlagB = table.gameLogic.buildRoad(player, table, userInput, previousPoint)

#Main Game Loop
returnFlag = 0
while(userInput != 5 or userInput != "quit" ):
    if returnFlag == 0:
        table.printBoard()
    player.printPlayer()
    userInput = input("""
What would you like to do?
1. Roll the dice and collect your resources
2. Upgrade a town you currently own to a city
3. Build a town
4. Build a road
5. Purchase a card
6. Play a card in your hand
9. Exit the game
""")
    match userInput:
        case '1':
            returnFlag = table.gameLogic.rollDice(table, player)
        case '2':
            userInput = input("What town would you like to upgrade?\n")
            returnFlag = table.gameLogic.buildCity(player, table, userInput)
        case '3':
            userInput = input("Where would you like to build a new town?\n")
            returnFlag = table.gameLogic.buildNewTown(player, table, userInput)
        case '4':
            userInput = input("""
Where would you like to build a new road?
Enter the starting and ending points as shown
Ex. 4-TL/4-TR would build a road from
tile 4 Top Left to tile 4 Top Right
""")
            returnFlag = table.gameLogic.buildNewRoad(player, table, userInput)
        case '5':
            returnFlag = cards.purchaseCard(player)
        case '6':
            userInput = input("Which card would you like to play?\n")
            returnFlag = cards.playCard(player, table, userInput)
        case '9':
            print("Thank you for playing!")
            quit()
        case 'quit':
            print("Thank you for playing!")
            quit()
        case _:
            print(f"Invalid input: {userInput}. Please try again.\n")
            returnFlag = -1
    cards.specialtyCardCheck(player, table)