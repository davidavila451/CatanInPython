RESET = "\x1b[0m"

#Player class which will keep track of the players resources, points, and action cards
class Player:
    resources = {
        'Lumber': 0,
        'Wool': 0,
        'Grain': 0,
        'Brick': 0,
        'Ore': 0
    }

    resourceKeys = list(resources.keys())

    availableCities = 2
    availableRoads = 2

    ownedSeqRoads = 0
    longestRoadData = []
    armySize = 0
    heldCards = []
    specialtyCards = []

    currentPoints = 0

    cityData = {
        'Towns': [],
        'Cities': []
    }

    roadData = []

    def __inti__(self):
        self.resources = Player.resources
        self.COLOR = ""
        self.colorTitle = ""
        self.availableCities = Player.availableCities
        self.longestRoadData = Player.longestRoadData
        self.ownedRoads = Player.ownedRoads
        self.armySize = Player.armySize
        self.heldCards = Player.heldCards
        self.specialtyCards = Player.specialtyCards
        self.currentPoints = Player.currentPoints
        self.cityData = Player.cityData
        self.roadData = Player.roadData

    def printPlayer(self):
        if(self.currentPoints > 9):
            pointsNumLen = 2
        else:
            pointsNumLen = 1

        print(f"|-------------------|-------------------|-------------------|")
        print(f"| RESOURCES:        | POINTS: {self.currentPoints}{' '*(10-(2 if self.currentPoints>9 else 1))}| CARDS:            |")     
        print(f'| {Player.resourceKeys[0]}: {self.resources[Player.resourceKeys[0]]}{' '*(16-(len(Player.resourceKeys[0])+(2 if self.resources[Player.resourceKeys[0]]>9 else 1)))}| ARMY SIZE: {self.armySize}{' '*(7-(2 if self.armySize>9 else 1))}| {f'{self.heldCards[0].title}: {self.heldCards[0].qty}' if 0 <= 0 < len(self.heldCards) else ''}{' '*(16-(len(self.heldCards[0].title) + (2 if self.heldCards[0].qty>9 else 1))) if 0 <= 0 < len(self.heldCards) else ' '*(19-pointsNumLen)}|')
        print(f'| {Player.resourceKeys[1]}: {self.resources[Player.resourceKeys[1]]}{' '*(16-(len(Player.resourceKeys[1])+(2 if self.resources[Player.resourceKeys[1]]>9 else 1)))}| SPECIAL CARDS:{' '*(5-pointsNumLen)}| {f'{self.heldCards[1].title}: {self.heldCards[1].qty}' if 0 <= 1 < len(self.heldCards) else ''}{' '*(16-(len(self.heldCards[1].title) + (2 if self.heldCards[1].qty>9 else 1))) if 0 <= 1 < len(self.heldCards) else ' '*(19-pointsNumLen)}|')
        print(f'| {Player.resourceKeys[2]}: {self.resources[Player.resourceKeys[2]]}{' '*(16-(len(Player.resourceKeys[2])+(2 if self.resources[Player.resourceKeys[2]]>9 else 1)))}| {f'{self.specialtyCards[0]}' if 0 <= 0 < len(self.specialtyCards) else ''}{' '*(18-(len(self.specialtyCards[0]))) if 0 <= 0 < len(self.specialtyCards) else ' '*(19-pointsNumLen)}| {f'{self.heldCards[2].title}: {self.heldCards[2].qty}' if 0 <= 2 < len(self.heldCards) else ''}{' '*(16-(len(self.heldCards[2].title) + (2 if self.heldCards[2].qty>9 else 1))) if 0 <= 2 < len(self.heldCards) else ' '*(19-pointsNumLen)}|')
        print(f'| {Player.resourceKeys[3]}: {self.resources[Player.resourceKeys[3]]}{' '*(16-(len(Player.resourceKeys[3])+(2 if self.resources[Player.resourceKeys[3]]>9 else 1)))}| {' '*(19-pointsNumLen)}| {f'{self.heldCards[3].title}: {self.heldCards[3].qty}' if 0 <= 3 < len(self.heldCards) else ''}{' '*(16-(len(self.heldCards[3].title) + (2 if self.heldCards[3].qty>9 else 1))) if 0 <= 3 < len(self.heldCards) else ' '*(19-pointsNumLen)}|')
        print(f'| {Player.resourceKeys[4]}: {self.resources[Player.resourceKeys[4]]}{' '*(16-(len(Player.resourceKeys[4])+(2 if self.resources[Player.resourceKeys[4]]>9 else 1)))}| {' '*(19-pointsNumLen)}| {f'{self.heldCards[4].title}: {self.heldCards[4].qty}' if 0 <= 4 < len(self.heldCards) else ''}{' '*(16-(len(self.heldCards[4].title) + (2 if self.heldCards[4].qty>9 else 1))) if 0 <= 4 < len(self.heldCards) else ' '*(19-pointsNumLen)}|')
        print(f"|-------------------|-------------------|-------------------|")

    def removeCard(self, cardName):
        for card in self.heldCards:
            if card.title == cardName:
                if card.qty == 1:
                    self.heldCards.remove(card)
                else:
                    card.qty -= 1
        return
    
    def getResource(userInput):
        match userInput:
            case 'Lumber':
                self.resources['Lumber'] += 1
                return 0
            case 'Wool':
                self.resources['Wool'] += 1
                return 0
            case 'Grain':
                self.resources['Grain'] += 1
            case 'Brick':
                self.resources['Brick'] += 1
            case 'Ore':
                self.resources['Ore'] += 1
            case _:
                print(f"Invalid resource: {userInput}")
    
    def initialSetUp(self, table):
        #Build Town
        clearFlagA = -1
        while clearFlagA != 0:
            userInput = input(f"""
Select where you would like to build a city.
Enter the tile ID (top number) followed by position:
Ex. 4-TL would place a town on tile 4 in the (T)op (L)eft.
                            
You have {str(self.availableCities)} left to place.
""")
            if(userInput == "quit"):
                quit()
            cityChoice = scrubCityInput(userInput, table.gameLogic)
            if cityChoice == -1:
                clearFlagA = -1
            else:
                clearFlagA = table.gameLogic.buildTown(self, table, cityChoice)
                previousPoint = cityChoice
        
        clearFlagB = -1

        #Build Road
        while clearFlagB != 0:
            userInput = input(f"""
Select the point you would like to build your road to
from the town you just built.
Enter the tile ID (top number) followed by position:
Ex. 4-TR would place a road to tile (4) in the (T)op (R)ight.
                        
You have {str(self.availableRoads)} left to place.
""")
            if(userInput == "quit"):
                quit()
            
            cityChoice = scrubCityInput(userInput, table.gameLogic)
            if cityChoice == -1:
                clearFlagB = -1
            else:
                clearFlagB = table.gameLogic.buildRoad(self, table, cityChoice, previousPoint)

    def onTurn(self, table, cards, players):
        table.gameLogic.rollDice(table, self)
        returnFlag = -1
        while returnFlag == -1:
            self.printPlayer()
            userInput = input("""
What would you like to do?
1. Trade with another player
2. Upgrade a town you currently own to a city
3. Build a town
4. Build a road
5. Purchase a card
6. Play a card in your hand
9. Exit the game
""")
            match userInput:
                case '1':
                    userInput = input(f"""
Who would you like to trade with?
1. {players[1].COLOR}{players[1].colorTitle}{RESET}
2. {players[2].COLOR}{players[2].colorTitle}{RESET}
3. {players[3].COLOR}{players[3].colorTitle}{RESET}
""")
                    match userInput:
                        case "1":
                            returnFlag = players[1].initiateTrade()
                        case "2":
                            returnFlag = players[2].initiateTrade()
                        case "3":
                            returnFlag = players[3].initiateTrade()
                        case _:
                            returnFlag = -1
                case '2':
                    userInput = input("What town would you like to upgrade?\n")
                    cityChoice = scrubCityInput(userInput, table.gameLogic)
                    if cityChoice == -1:
                        returnFlag = -1
                    else:
                        returnFlag = table.gameLogic.buildCity(self, table, cityChoice)
                case '3':
                    userInput = input("Where would you like to build a new town?\n")
                    cityChoice = scrubCityInput(userInput, table.gameLogic)
                    if cityChoice == -1:
                        returnFlag = -1
                    else:
                        returnFlag = table.gameLogic.buildNewTown(self, table, cityChoice)
                case '4':
                    userInput = input("""
        Where would you like to build a new road?
        Enter the starting and ending points as shown
        Ex. 4-TL/4-TR would build a road from
        tile 4 Top Left to tile 4 Top Right
        """)
                    userInputTokens = userInput.split("/")
                    if(len(userInputTokens) != 2):
                        print(f"Invalid range: {userInput}")
                        returnFlag = -1
                    else:
                        cityChoiceA = scrubCityInput(userInputTokens[0], table.gameLogic)
                        cityChoiceB = scrubCityInput(userInputTokens[1], table.gameLogic)
                        if cityChoiceA == -1 or cityChoiceB == -1:
                            returnFlag = -1
                        else:
                            returnFlag = table.gameLogic.buildNewRoad(self, table, cityChoiceB, cityChoiceA)
                case '5':
                    returnFlag = cards.purchaseCard(self)
                case '6':
                    userInput = input("Which card would you like to play?\n")
                    returnFlag = cards.playCard(self, table, userInput)
                case '9':
                    print("Thank you for playing!")
                    quit()
                case 'quit':
                    print("Thank you for playing!")
                    quit()
                case _:
                    print(f"Invalid input: {userInput}. Please try again.\n")
                    returnFlag = -1
            cards.specialtyCardCheck(self, table)

def scrubCityInput(userInput, game):
    for row in game.cityData:
            for city in game.cityData[row]:
                if userInput in game.cityData[row][city]['Locations']:
                    return(f'{row}{city}')

    print("Invalid Coordinates: "+userInput+". Please try again.")
    return -1