RED = "\x1b[31m"
GREEN = "\x1b[32m"
BLUE = "\x1b[34m"
MAG = "\x1b[35m"
RESET = "\x1b[0m"

#Player class which will keep track of the players resources, points, and action cards
class Player:
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

    def __inti__(self):
        self.resources = Player.resources
        self.color = RED
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