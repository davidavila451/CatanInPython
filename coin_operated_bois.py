RED = "\x1b[31m"
GREEN = "\x1b[32m"
BLUE = "\x1b[34m"
MAG = "\x1b[35m"
RESET = "\x1b[0m"

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

    def __inti__(self):
        self.resources = Bot.resources
        self.color = RED
        self.availableCities = Bot.availableCities
        self.longestRoadData = Bot.longestRoadData
        self.ownedRoads = Bot.ownedRoads
        self.armySize = Bot.armySize
        self.heldCards = Bot.heldCards
        self.specialtyCards = Bot.specialtyCards
        self.currentPoints = Bot.currentPoints
        self.cityData = Bot.cityData
        self.roadData = Bot.roadData