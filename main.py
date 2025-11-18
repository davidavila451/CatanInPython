import random

#Handles all game logic. (Rolling dice, purchasing and placing cities/roads/cards)
class GameLogic:
    def __init__(self, board):
        self.cityMap = GameLogic.mapCities(board)

    def mapCities(self, board):
        return 

    def buildCity(self, player):
        print("City Built")

    def rollDice(self, board, player):
        dieResult = random.randint(2,12) #Roll 2 dice
        print(f'Die Result: {dieResult}') #Debug checking
        for tile in board.boardMap:
            if tile.dieNumber == dieResult:
                player.resources[tile.resource] += 1 #Give players one resource for 
                continue


#Contains Resource Tile data. (ID, Die Number Medallion, Resource Produced, and Title)
class Tile:
    id = 0
    dieNumber = 0
    resource = ""
    title = ""

    def __init__(self, title, resource, id, dieNumber):
        self.resource = resource
        self.id = id
        self.dieNumber = dieNumber
        self.title = title

#Contains all visible data of the board. (The visible board, board generation, resources spread)
class Board:
    resourceMap = {
        'Lumber': 4,
        'Wool': 4,
        'Grain': 4,
        'Brick': 3,
        'Ore': 3
    }

    numbersMap = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

    boardMap = []

    daBoard = {
        'A': [' ' * 21, '0', '-' * 5, '0', ' ' * 10],
        'B': [
            ' ' * 20, '/', ' ' * 7, '\\', '\n',
            ' ' * 19, '/', '^', '\\'
            ],
        'C': [' ' * 12, '0', '-' * 5, '0', '+', '0', '-' * 5, '0', ' ' * 6],
        'D': [
            ' ' * 11, '/', ' ' * 7, '\\', '#', '/', ' ' * 7, '\\','\n',
            ' ' * 10, '/', '^', '\\', ' ' * 7, '/', '^', '\\'
            ],
        'E': [' ' * 3, '0', '-' * 5, '0', '+', '0', '-' * 5, '0', '+', '0', '-' * 5, '0', ' ' * 2],
        'F': [
            ' ' * 2, '/', ' ' * 7, '\\', '#', '/', ' ' * 7, '\\', '#', '/', ' ' * 7, '\\','\n',
            ' ', '/', '^', '\\', ' ' * 7, '/', '^', '\\', ' ' * 7, '/', '^', '\\'
            ],
        'G': ['0', '+', '0', '-' * 5, '0', '+', '0', '-' * 5, '0', '+', '0'],
        'H': [
            ' ', '\\', '#', '/', ' ' * 7, '\\', '#', '/', ' ' * 7, '\\', '#', '/','\n',
            ' ' * 2, '\\', ' ' * 7, '/', '^', '\\', ' ' * 7, '/', '^', '\\', ' ' * 7, '/'
            ],
        'I': [' ' * 3, '0', '-' * 5, '0', '+', '0', '-' * 5, '0', '+', '0', '-' * 5, '0', ' ' * 2],
        'J': [
            ' ' * 2, '/', ' ' * 7, '\\', '#', '/', ' ' * 7, '\\', '#', '/', ' ' * 7, '\\', '\n',
            ' ', '/', '^', '\\', ' ' * 7, '/', '^', '\\', ' ' * 7, '/', '^', '\\'
            ],
        'K': ['0', '+', '0', '-' * 5, '0', '+', '0', '-' * 5, '0', '+', '0'],
        'L': [
              ' ', '\\', '#', '/', ' ' * 7, '\\', '#', '/', ' ' * 7, '\\', '#', '/', '\n',
              ' ' * 2, '\\', ' ' * 7, '/', '^', '\\', ' ' * 7, '/', '^', '\\', ' ' * 7, '/'
              ],
        'M': [' ' * 3, '0', '-' * 5, '0', '+', '0', '-' * 5, '0', '+', '0', '-' * 5, '0', ' ' * 2],
        'N': [
              ' ' * 2, '/', ' ' * 7, '\\', '#', '/', ' ' * 7, '\\', '#', '/', ' ' * 7, '\\', '\n',
              ' ', '/', '^', '\\', ' ' * 7, '/', '^', '\\', ' ' * 7, '/', '^', '\\'
              ],
        'O': ['0', '+', '0', '-' * 5, '0', '+', '0', '-' * 5, '0', '+', '0'],
        'P': [
              ' ', '\\', '#', '/', ' ' * 7, '\\', '#', '/', ' ' * 7, '\\', '#', '/', '\n',
              ' ' * 2, '\\', ' ' * 7, '/', '^', '\\', ' ' * 7, '/', '^', '\\', ' ' * 7, '/'
              ],
        'Q': [' ' * 3, '0', '-' * 5, '0', '+', '0', '-' * 5, '0', '+', '0', '-' * 5, '0', ' ' * 2],
        'R': [
              ' ' * 10, '\\', '#', '/', ' ' * 7, '\\', '#', '/',' \n',
              ' ' * 11, '\\', ' ' * 7, '/', '^', '\\', ' ' * 7, '/'
              ],
        'S': [' ' * 12, '0', '-' * 5, '0', '+', '0', '-' * 5, '0'],
        'T': [
              ' ' * 19, '\\', '#', '/', '\n',
              ' ' * 20, '\\', ' ' * 7, '/'
              ],
        'U': [' ' * 21, '0', '-' * 5, '0', ' ' * 10]
    }

    def __init__(self):
        self.resourceMap = Board.resourceMap #Create a new resource map for tracking available resources for the board
        self.boardMap = Board.boardMap #Create new boardMap
        self.numbersMap = Board.numbersMap
        self.daBoard = Board.daBoard
        index = 0
        while index < 19: #For each tile on the board
            if(index == 9):
                self.boardMap.append(Tile('Desert', 'Desert', index, 7))
            else:
                resourceMapKeys = list(self.resourceMap.keys()) #Get a list of resources still available
                currentKey = random.choice(resourceMapKeys) #The current resource from the list of available resources
                currentDieNumber = random.choice(self.numbersMap)
                self.numbersMap.remove(currentDieNumber)
                Board.resourceCheck(self, currentKey) #Check to ensure the resource is still available
                match currentKey:
                    case 'Lumber':
                        self.boardMap.append(Tile('Forest', currentKey, index, currentDieNumber)) #Assign resource to current tile
                    case 'Wool':
                        self.boardMap.append(Tile('Pasture', currentKey, index, currentDieNumber))
                    case 'Grain':
                        self.boardMap.append(Tile('Fields', currentKey, index, currentDieNumber))
                    case 'Brick':
                        self.boardMap.append(Tile('Hills', currentKey, index, currentDieNumber))
                    case 'Ore':
                        self.boardMap.append(Tile('Mountains', currentKey, index, currentDieNumber))
            index += 1
        self.gameLogic = GameLogic(self)
        Board.populateBoard(self)
    
    def resourceCheck(self, resource):
        self.resourceMap[resource] = self.resourceMap[resource] - 1 #Remove one from available resources
        if(self.resourceMap[resource] == 0): #If the resource is empty remove it from the list
            del self.resourceMap[resource]

    def populateBoard(self):
        for resource in self.boardMap:
            flag1 = 0
            flag2 = 0
            flag3 = 0
            for Y in self.daBoard:
                for index, X in enumerate(self.daBoard[Y]):
                    if X == '^' and flag1 != 1:
                        self.daBoard[Y][index] = ' '*(4-(resource.id//10))+str(resource.id)+' '*4
                        flag1 = 1
                    if X == '+' and flag2 != 1:
                        self.daBoard[Y][index] = ' '*((11-len(resource.title))//2)+resource.title+' '*(((11-len(resource.title))//2)+((11-len(resource.title))%2))
                        flag2 = 1
                    if X == '#' and flag3 != 1:
                        self.daBoard[Y][index] = ' '*(4-(resource.dieNumber//10))+str(resource.dieNumber)+' '*4
                        flag3 = 1
                    if flag1 == 1 and flag2 == 1 and flag3 == 1:
                        break
                if flag1 == 1 and flag2 == 1 and flag3 == 1:
                    break

    def printBoard(self):
        for Y in self.daBoard:
            rowString = ''
            for X in self.daBoard[Y]:
                rowString += X
            print(f'{rowString}')

#Player class which will keep track of the players resources, points, and action cards
class Player:
    resources = {
        'Lumber': 0,
        'Wool': 0,
        'Grain': 0,
        'Brick': 0,
        'Ore': 0
    }

    availableCities = 3

    def __inti__(self):
        self.resources = Player.resources
        self.availableCities = Player.availableCities

    def printPlayer(self):
        for resource in self.resources:
            print(f'{resource}: {self.resources[resource]}')

#Start of main biz
board = Board()
player = Player()
userInput = ""

#Setup Loop
#while(userInput != "quit" or player.availableTowns != 0):
#    userInput = input("""
#                      Select where you would like to build a city.
#                      Enter the tile ID (top number) followed by position:
#                      Ex. 4-TL would place a town on tile 4 in the top left.
#                      """)
#    if(userInput != "quit"):
#        board.buildCity()
#Main Game Loop
while(userInput != "quit"):
    board.printBoard()
    player.printPlayer()
    userInput = input("What would you like to do? quit to exit\n")
    if(userInput == "roll dice"):
        board.gameLogic.rollDice(board, player)

print("Thank you for playing!")

#print(
#f"""   {board.boardMap[0].corner[0]}{board.boardMap[0].side[0]*5}{board.boardMap[0].corner[1]}   
#  {board.boardMap[0].side[5]}{' '*7}{board.boardMap[0].side[1]}  
# {board.boardMap[0].side[5]}{' '*9}{board.boardMap[0].side[1]} 
#{board.boardMap[0].corner[5]}{' '*((11-len(board.boardMap[0].title))//2)}{board.boardMap[0].title}{' '*(((11-len(board.boardMap[0].title))//2)+((11-len(board.boardMap[0].title))%2))}{board.boardMap[0].corner[2]}
# {board.boardMap[0].side[4]}{' '*(4-(board.boardMap[0].id//10))}{board.boardMap[0].id}{' '*4}{board.boardMap[0].side[2]} 
# {board.boardMap[0].side[4]}{' '*7}{board.boardMap[0].side[2]}  
#   {board.boardMap[0].corner[4]}{board.boardMap[0].side[3]*5}{board.boardMap[0].corner[3]}   
#""")
#print(board.boardMap[0].id)
#print(board.boardMap[0].resource)
#print(board.boardMap[6].id)
#print(board.boardMap[6].resource)