RED = "\x1b[31m"
GREEN = "\x1b[32m"
BLUE = "\x1b[34m"
MAG = "\x1b[35m"
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

    color = RED

    availableCities = 2
    availableRoads = 2

    currentPoints = 0

    cityData = {
        'Towns': [],
        'Cities': []
    }

    roadData = []

    def __inti__(self):
        self.resources = Player.resources
        self.availableCities = Player.availableCities
        self.cityData = Player.cityData

    def printPlayer(self):
        if(self.currentPoints > 9):
            pointsNumLen = 2
        else:
            pointsNumLen = 1

        print("|-------------------|-------------------|")
        print(f"| RESOURCES:        |POINTS: {self.currentPoints}{' '*(11-pointsNumLen)}|")
        for resource in self.resources:
            if(self.resources[resource] > 9):
                resourceNumLen = 2
            else:
                resourceNumLen = 1

            print(f'| {resource}: {self.resources[resource]}{' '*(16-(len(resource)+resourceNumLen))}| {' '*(19-pointsNumLen)}|')

        print("|-------------------|-------------------|")