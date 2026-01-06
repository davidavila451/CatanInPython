import random
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

    playerAffinity = 5

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
        self.resources = Bot.resources
        self.COLOR = ""
        self.colorTitle = ""
        self.playerAffinity = Bot.playerAffinity
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
        townChoiceIndex = random.randint(0,len(table.gameLogic.availableCityPlots)-1)
        townChoice = table.gameLogic.availableCityPlots[townChoiceIndex]
        table.gameLogic.buildTown(self, table, townChoice)
        print("Built Town")

        #Build Road
        listOfAvailRoads = []
        for index in table.gameLogic.availableRoads:
            if townChoice in table.gameLogic.roadData[index[0]][int(index[1])]['Connections']:
                listOfAvailRoads.append(index)

        roadChoiceIndex = random.randint(0, len(listOfAvailRoads)-1)
        roadChoice = listOfAvailRoads[roadChoiceIndex]
        print(roadChoice)
        for connection in table.gameLogic.roadData[roadChoice[0]][int(roadChoice[1])]['Connections']:
            if connection != townChoice:
                newPoint = connection
        table.gameLogic.buildRoad(self, table, newPoint, townChoice)
        print("Built Road")

    def onTurn(self, table, cards, players):
        table.gameLogic.rollDice(table, self)

        numbers=[1,2,3,4]
        weights=[0.25,0.25,0.25,0.25]
        decision = random.choices(numbers, weights=weights, k=1)

        match decision:
            case 1:
                #Build road
                print()
            case 2:
                #Purchase Card
                print()
            case 3:
                #build town
                print()
            case 4:
                #Initiate Trade
                print()

        print("Turn Ended")

    def initiateTrade(self):
        if self.playerAffinity >= 5:
            print('"What are you looking for?"')
            userInput = input("""
1. Lumber
2. Wool
3. Grain
5. Brick
4. Ore
5. Nevermind
""")
            clearFlag = -1
            while clearFlag != 0:
                match userInput:
                    case "1":
                        print()
        else:
            print('"I do not wish to trade with the likes of you!"')
            return -1
        print()