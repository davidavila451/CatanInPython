class Bot:
    resources = {
        'Lumber': 10,
        'Wool': 0,
        'Grain': 0,
        'Brick': 10,
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

    def __inti__(self, COLOR):
        self.resources = Bot.resources
        self.COLOR = COLOR
        self.availableCities = Bot.availableCities
        self.longestRoadData = Bot.longestRoadData
        self.ownedRoads = Bot.ownedRoads
        self.armySize = Bot.armySize
        self.heldCards = Bot.heldCards
        self.specialtyCards = Bot.specialtyCards
        self.currentPoints = Bot.currentPoints
        self.cityData = Bot.cityData
        self.roadData = Bot.roadData

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
            previousPoint = userInput
            clearFlagA = table.gameLogic.buildTown(self, table, userInput)
        
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
            clearFlagB = table.gameLogic.buildRoad(self, table, userInput, previousPoint)

    def onTurn(self, table, cards):
        returnFlag = 0
        if returnFlag == 0:
            self.printPlayer()
            userInput = input("""
What would you like to do?
2. Upgrade a town you currently own to a city
3. Build a town
4. Build a road
5. Purchase a card
6. Play a card in your hand
9. Exit the game
""")
            match userInput:
                case '2':
                    userInput = input("What town would you like to upgrade?\n")
                    returnFlag = table.gameLogic.buildCity(self, table, userInput)
                case '3':
                    userInput = input("Where would you like to build a new town?\n")
                    returnFlag = table.gameLogic.buildNewTown(self, table, userInput)
                case '4':
                    userInput = input("""
        Where would you like to build a new road?
        Enter the starting and ending points as shown
        Ex. 4-TL/4-TR would build a road from
        tile 4 Top Left to tile 4 Top Right
        """)
                    returnFlag = table.gameLogic.buildNewRoad(self, table, userInput)
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