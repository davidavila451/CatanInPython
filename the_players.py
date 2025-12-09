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

    availableCities = 3

    cityData = {
        'Towns': [],
        'Cities': []
    }

    def __inti__(self):
        self.resources = Player.resources
        self.availableCities = Player.availableCities
        self.cityData = Player.cityData

    def printPlayer(self):
        for resource in self.resources:
            print(f'{resource}: {self.resources[resource]}')
