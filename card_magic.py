import random

allCards = [
    {
        "title": "Knight",
        "qty": 14
    },
    {
        "title": "Victory Point",
        "qty": 5
    },
    {
        "title": "Progress",
        "qty": 6
    }
]

victoryPointCards = [
    "University",
    "Library",
    "Market",
    "Great Hall",
    "Chapel"
]

progressCards = [
    {
        #Build 2 free roads
        "title": "Road Building",
        "qty": 2,
        "desc": "Build 2 free roads"
    },
    {
        #Take any 2 resources from the bank
        "title": "Year of Plenty",
        "qty": 2,
        "desc": "Take any 2 resources from the bank"
    },
    {
        #Name a resource, all players give you theirs
        "title": "Monopoly",
        "qty": 2,
        "desc": "Name a resource, all players give you theirs"
    }
]

specialtyCards = [
    {
        "title": "Longest Road",
        "player": None
    },
    {
        "title": "Largest Army",
        "player": None
    }
]

numbers = [0, 1, 2]
cardWeights = [0.56, 0.2, 0.24]

class Card:
    def __init__(self, cardTitle):
        self.title = cardTitle
        self.qty = 1
        self.status = 1

#Helps with conditional logic of different cards in the game.
class Deck:
    def __init__(self):
        self.allCards = allCards
        self.victoryPointCards = victoryPointCards
        self.progressCards = progressCards
        self.specialtyCards = specialtyCards
        self.shuffledDeck = random.choices(numbers, weights=cardWeights, k=25)

    def purchaseCard(self, player):
        if len(self.shuffledDeck) == 0:
            print("There are no more cards to purchase")
            return -1
        
        if (player.resources['Wool'] < 1) and (player.resources['Grain'] < 1) and (player.resources['Ore'] < 1):
            print(f"""
Insuffecient resources:
1/{player.resources['Wool']} Wool
1/{player.resources['Grain']} Grain
1/{player.resources['Ore']} Ore
""")
            return -1
        
        chosenNumber = self.shuffledDeck.pop(0)
        print("Card Purchased")
        player.resources['Wool'] -= 1
        player.resources['Grain'] -= 1
        player.resources['Ore'] -= 1
        print(f"You draw a {self.allCards[chosenNumber]["title"]} card.")
        match self.allCards[chosenNumber]["title"]:
            case "Knight":
                cardFlag = 0
                for card in player.heldCards:
                    if card.title == self.allCards[chosenNumber]["title"]:
                        card.qty += 1
                        cardFlag = 1
                if cardFlag == 0:
                    player.heldCards.append(Card(self.allCards[chosenNumber]["title"]))
                self.allCards[chosenNumber]['qty'] -= 1
                    
            case "Victory Point":
                Deck.drawVPCard(self)
                self.allCards[chosenNumber]['qty'] -= 1
                player.currentPoints += 1
            case "Progress":
                progressCard = Deck.drawProgressCard(self)
                cardFlag = 0
                for card in player.heldCards:
                    if card.title == progressCard:
                        card.qty += 1
                        cardFlag = 1
                if cardFlag == 0:
                    player.heldCards.append(Card(progressCard))
                self.allCards[chosenNumber]['qty'] -= 1

        return 0
    
    def drawVPCard(self):
        if(len(self.victoryPointCards)-1 == 0):
            vpCardInd = 0
        else:
            vpCardInd = random.randint(0,len(self.victoryPointCards)-1)
        vpCard = self.victoryPointCards.pop(vpCardInd)
        print(f"Congratulations, you construct a {vpCard}.\nYou gain one victory point.")
        
        return
    
    def drawProgressCard(self):
        if(len(self.progressCards)-1 == 0):
            progCardInd = 0
        else:
            progCardInd = random.randint(0,len(self.progressCards)-1)
        progCard = self.progressCards[progCardInd]['title']
        print(f"{progCard}. {self.progressCards[progCardInd]['desc']}")
        self.progressCards[progCardInd]['qty'] -= 1
        if self.progressCards[progCardInd]['qty'] == 0:
            self.progressCards.pop(progCardInd)

        return progCard
    
    def playCard(self, player, table, userInput):
        if len(player.heldCards) == 0:
            print("You have no cards to play!")
            return -1
        match userInput:
            case 'Knight':
                newUserInput = input("You play a knight card. Where would you like to place Gengis Khan?\n")
                returnFlag = table.moveGK(newUserInput)
                while returnFlag != 0:
                    newUserInput = input("Where would you like to place Gengis Khan?\n")
                    returnFlag = table.moveGK(newUserInput)
                player.armySize += 1
                for card in player.heldCards:
                    if card.title == 'Knight':
                        if card.qty > 1:
                            card.qty -= 1
                        else:
                            player.heldCards.remove(card)
                        

            case 'Year of Plenty':
                newUserInput = input("You play Year of Plenty. What is the first resource you would like?\n")
                returnFlag = player.getResource(newUserInput)
                while returnFlag != 0:
                    newUserInput = input("What is the first resource you would like?\n")
                    returnFlag = player.getResource(newUserInput)

                newUserInput = input("What is the second resource you would like?\n")
                returnFlag = player.getResource(newUserInput)
                while returnFlag != 0:
                    newUserInput = input("What is the second resource you would like?\n")
                    returnFlag = player.getResource(newUserInput)
            case 'Monopoly':
                newUserInput = input("You play Monopoly. What resource would you like to request?\n")
            case 'Road Building':
                newUserInput = input("You play Road Building. What are the coordinates for your first road?\n")
                player.resources['Brick'] += 2
                player.resources['Lumber'] += 2
                returnFlag = table.gameLogic.buildNewRoad(player, table, newUserInput)
                while returnFlag != 0:
                    newUserInput = input("What are the coordinates for your first road?\n")
                    returnFlag = table.gameLogic.buildNewRoad(player, table, newUserInput)

                table.printBoard()
                newUserInput = input("What are the coordinates for your second road?\n")
                returnFlag = table.gameLogic.buildNewRoad(player, table, newUserInput)
                while returnFlag != 0:
                    newUserInput = input("What are the coordinates for your second road?\n")
                    returnFlag = table.gameLogic.buildNewRoad(player, table, newUserInput)
                player.removeCard('Road Building')

            case _:
                print(f"You don't have a card called {userInput}.\n")
                return -1
        return 0
    
    def specialtyCardCheck(self, player, table):
        #Check for longest road
        for longRoadData in player.longestRoadData:
            if longRoadData['NoOfRoads'] > 5:
                player.specialtyCards.append(self.specialtyCards[0]['title'])
                player.currentPoints += 2
                self.specialtyCards[0]['player'] = "Player1"
                break
        #Check for largest army
        if player.armySize >= 3:
            player.specialtyCards.append(self.specialtyCards[1]['title'])
            player.currentPoints += 2
            self.specialtyCards[1]['player'] = "Player1"
        print("Special requirements checked!")
        return 0