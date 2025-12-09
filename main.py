import random
import re

RED = "\x1b[31m"
GREEN = "\x1b[32m"
BLUE = "\x1b[34m"
MAG = "\x1b[35m"
RESET = "\x1b[0m"

#Handles all game logic. (Rolling dice, purchasing and placing cities/roads/cards)
class GameLogic:
    roadData = {
        "A": {
            1: {
                "Status": '-',
                "Connections": ["A1", "A2"]
            }
        },
        "B": {
            1: {
                "Status": '/',
                "Connections": ["A1", "B2"]
            },
            2: {
                "Status": '\\',
                "Connections": ["A2", "B3"]
            }
        },
        "C": {
            1: {
                "Status": '-',
                "Connections": ["B1", "B2"]
            },
            2: {
                "Status": '-',
                "Locations": ["B3", "B4"]
            }
        },
        "D": {
            1: {
                "Status": '/',
                "Locations": ["B1", "C2"]
            },
            2: {
                "Status": '\\',
                "Locations": ["B2", "C3"]
            },
            3: {
                "Status": '/',
                "Locations": ["B3", "C4"]
            },
            4: {
                "Status": '\\',
                "Locations": ["B4", "C5"]
            }
        },
        "E": {
            1: {
                "Status": '-',
                "Locations": ["C1", "C2"]
            },
            2: {
                "Status": '-',
                "Locations": ["C3", "C4"]
            },
            3: {
                "Status": '-',
                "Locations": ["C5", "C6"]
            }
        },
        "F": {
            1: {
                "Status": '/',
                "Locations": ["C1", "D1"]
            },
            2: {
                "Status": '\\',
                "Locations": ["C2", "D2"]
            },
            3: {
                "Status": '/',
                "Locations": ["C3", "D3"]
            },
            4: {
                "Status": '\\',
                "Locations": ["C4", "D4"]
            },
            5: {
                "Status": '/',
                "Locations": ["C5", "D5"]
            },
            6: {
                "Status": '\\',
                "Locations": ["C6", "D6"]
            }
        },
        "G": {
            1: {
                "Status": '-',
                "Locations": ["D2", "D3"]
            },
            2: {
                "Status": '-',
                "Locations": ["D4", "D5"]
            }
        },
        "H": {
            1: {
                "Status": '\\',
                "Locations": ["D1", "E1"]
            },
            2: {
                "Status": '/',
                "Locations": ["D2", "E2"]
            },
            3: {
                "Status": '\\',
                "Locations": ["D3", "E3"]
            },
            4: {
                "Status": '/',
                "Locations": ["D4", "E4"]
            },
            5: {
                "Status": '\\',
                "Connections": ["D5", "E5"]
            },
            6: {
                "Status": '/',
                "Connections": ["D6", "E6"]
            }
        },
        "I": {
            1: {
                "Status": '-',
                "Connections": ["E1", "E2"]
            },
            2: {
                "Status": '-',
                "Connections": ["E3", "E4"]
            },
            3: {
                "Status": '-',
                "Connections": ["E5", "E6"]
            }
        },
        "J": {
            1: {
                "Status": '/',
                "Connections": ["E1", "F1"]
            },
            2: {
                "Status": '\\',
                "Connections": ["E2", "F2"]
            },
            3: {
                "Status": '/',
                "Connections": ["E3", "F3"]
            },
            4: {
                "Status": '\\',
                "Connections": ["E4", "F4"]
            },
            5: {
                "Status": '/',
                "Connections": ["E5", "F5"]
            },
            6: {
                "Status": '\\',
                "Connections": ["E6", "F6"]
            }
        },
        "K": {
            1: {
                "Status": '-',
                "Connections": ["F2", "F3"]
            },
            2: {
                "Status": '-',
                "Connections": ["F4", "F5"]
            }
        },
        "L": {
            1: {
                "Status": '\\',
                "Connections": ["F1", "G1"]
            },
            2: {
                "Status": '/',
                "Connections": ["F2", "G2"]
            },
            3: {
                "Status": '\\',
                "Connections": ["F3", "G3"]
            },
            4: {
                "Status": '/',
                "Connections": ["F4", "G4"]
            },
            5: {
                "Status": '\\',
                "Connections": ["F5", "G5"]
            },
            6: {
                "Status": '/',
                "Connections": ["F6", "G6"]
            }
        },
        "M": {
            1: {
                "Status": '-',
                "Connections": ["G1", "G2"]
            },
            2: {
                "Status": '-',
                "Connections": ["G3", "G4"]
            },
            3: {
                "Status": '-',
                "Connections": ["G5", "G6"]
            }
        },
        "N": {
            1: {
                "Status": '/',
                "Connections": ["G1", "H1"]
            },
            2: {
                "Status": '\\',
                "Connections": ["G2", "H2"]
            },
            3: {
                "Status": '/',
                "Connections": ["G3", "H3"]
            },
            4: {
                "Status": '\\',
                "Connections": ["G4", "H4"]
            },
            5: {
                "Status": '/',
                "Connections": ["G5", "H5"]
            },
            6: {
                "Status": '\\',
                "Connections": ["G6", "H6"]
            }
        },
        "O": {
            1: {
                "Status": '-',
                "Connections": ["H2", "H3"]
            },
            2: {
                "Status": '-',
                "Connections": ["H4", "H5"]
            }
        },
        "P": {
            1: {
                "Status": '\\',
                "Connections": ["H1", "I1"]
            },
            2: {
                "Status": '/',
                "Connections": ["H2", "I2"]
            },
            3: {
                "Status": '\\',
                "Connections": ["H3", "I3"]
            },
            4: {
                "Status": '/',
                "Connections": ["H4", "I4"]
            },
            5: {
                "Status": '\\',
                "Connections": ["H5", "I5"]
            },
            6: {
                "Status": '/',
                "Connections": ["H6", "I6"]
            }
        },
        "Q": {
            1: {
                "Status": '-',
                "Connections": ["I1", "I2"]
            },
            2: {
                "Status": '-',
                "Connections": ["I3", "I4"]
            },
            3: {
                "Status": '-',
                "Connections": ["I5", "I6"]
            }
        },
        "R": {
            1: {
                "Status": '\\',
                "Connections": ["I2", "J1"]
            },
            2: {
                "Status": '/',
                "Connections": ["I3", "J2"]
            },
            3: {
                "Status": '\\',
                "Connections": ["I4", "J3"]
            },
            4: {
                "Status": '/',
                "Connections": ["I5", "J4"]
            }
        },
        "S": {
            1: {
                "Status": '-',
                "Connections": ["J1", "J2"]
            },
            2: {
                "Status": '-',
                "Connections": ["J3", "J4"]
            }
        },
        "T": {
            1: {
                "Status": '\\',
                "Connections": ["J2", "K1"]
            },
            2: {
                "Status": '/',
                "Connections": ["J3", "K2"]
            }
        },
        "U": {
            1: {
                "Status": '-',
                "Connections": ["K1", "K2"]
            }
        }
    }
    cityData = {
        "A":{
            1: {
                "Status": "0",
                "Locations": ["0-TL"]
            },
            2: {
                "Status": "0",
                "Locations": ["0-TR"]
            }
        },
        "B":{
            1: {
                "Status": "0",
                "Locations": ["1-TL"]
            },
            2: {
                "Status": "0",
                "Locations": ["1-TR", "0-CL"]
            },
            3: {
                "Status": "0",
                "Locations": ["2-TL", "0-CR"]
            },
            4: {
                "Status": "0",
                "Locations": ["2-TR"]
            }
        },
        "C":{
            1: {
                "Status": "0",
                "Locations": ["3-TL"]
            },
            2: {
                "Status": "0",
                "Locations": ["3-TR", "1-CL"]
            },
            3: {
                "Status": "0",
                "Locations": ["4-TL", "1-CR", "0-BL"]
            },
            4: {
                "Status": "0",
                "Locations": ["4-TR", "2-CL", "0-BR"]
            },
            5: {
                "Status": "0",
                "Locations": ["5-TL", "2-CR"]
            },
            6: {
                "Status": "0",
                "Locations": ["5-TR"]
            }
        },
        "D":{
            1: {
                "Status": "0",
                "Locations": ["3-CL"]
            },
            2: {
                "Status": "0",
                "Locations": ["3-CR", "1-BL", "6-TL"]
            },
            3: {
                "Status": "0",
                "Locations": ["4-CL", "1-BR", "6-TR"]
            },
            4: {
                "Status": "0",
                "Locations": ["4-CR", "2-BL", "7-TL"]
            },
            5: {
                "Status": "0",
                "Locations": ["2-BR", "7-TR", "5-CL"]
            },
            6: {
                "Status": "0",
                "Locations": ["5-CR"]
            }
        },
        "E":{
            1: {
                "Status": "0",
                "Locations": ["3-BL", "8-TL"]
            },
            2: {
                "Status": "0",
                "Locations": ["3-BR", "8-TR", "6-CL"]
            },
            3: {
                "Status": "0",
                "Locations": ["6-CR", "4-BL", "9-TL"]
            },
            4: {
                "Status": "0",
                "Locations": ["4-BR", "9-TR", "7-CL"]
            },
            5: {
                "Status": "0",
                "Locations": ["7-CR", "5-BL", "10-TL"]
            },
            6: {
                "Status": "0",
                "Locations": ["5-BR", "10-TR"]
            }
        },
        "F":{
            1: {
                "Status": "0",
                "Locations": ["8-CL"]
            },
            2: {
                "Status": "0",
                "Locations": ["8-CR", "6-BL", "11-TL"]
            },
            3: {
                "Status": "0",
                "Locations": ["6-BR", "11-TR", "9-CL"]
            },
            4: {
                "Status": "0",
                "Locations": ["9-CR", "7-BL", "12-TR"]
            },
            5: {
                "Status": "0",
                "Locations": ["7-BR", "12-TR", "10-CL"]
            },
            6: {
                "Status": "0",
                "Locations": ["10-CR"]
            }
        },
        "G":{
            1: {
                "Status": "0",
                "Locations": ["8-BL", "13-TL"]
            },
            2: {
                "Status": "0",
                "Locations": ["8-BR", "13-TR", "11-CL"]
            },
            3: {
                "Status": "0",
                "Locations": ["11-CR", "9-BL", "14-TL"]
            },
            4: {
                "Status": "0",
                "Locations": ["9-BR", "14-TR", "12-CL"]
            },
            5: {
                "Status": "0",
                "Locations": ["12-CR", "10-BL", "15-TL"]
            },
            6: {
                "Status": "0",
                "Locations": ["10-BR", "15-TR"]
            }
        },
        "H":{
            1: {
                "Status": "0",
                "Locations": ["13-CL"]
            },
            2: {
                "Status": "0",
                "Locations": ["13-CR", "16-TL", "11-BL"]
            },
            3: {
                "Status": "0",
                "Locations": ["11-BR", "16-TR", "14-CL"]
            },
            4: {
                "Status": "0",
                "Locations": ["14-CR", "12-BL", "17-TL"]
            },
            5: {
                "Status": "0",
                "Locations": ["12-BR", "17-TR", "15-CL"]
            },
            6: {
                "Status": "0",
                "Locations": ["15-CR"]
            }
        },
        "I":{
            1: {
                "Status": "0",
                "Locations": ["13-BL"]
            },
            2: {
                "Status": "0",
                "Locations": ["13-BR", "16-CL"]
            },
            3: {
                "Status": "0",
                "Locations": ["16-CR", "14-BL", "18-TL"]
            },
            4: {
                "Status": "0",
                "Locations": ["14-BR", "18-TR", "17-CL"]
            },
            5: {
                "Status": "0",
                "Locations": ["17-CR", "15-BL"]
            },
            6: {
                "Status": "0",
                "Locations": ["15-BR"]
            }
        },
        "J":{
            1: {
                "Status": "0",
                "Locations": ["16-BL"]
            },
            2: {
                "Status": "0",
                "Locations": ["16-BR", "18-CL"]
            },
            3: {
                "Status": "0",
                "Locations": ["18-CR", "17-BL"]
            },
            4: {
                "Status": "0",
                "Locations": ["17-BR"]
            }
        },
        "K":{
            1: {
                "Status": "0",
                "Locations": ["18-BL"]
            },
            2: {
                "Status": "0",
                "Locations": ["18-BR"]
            }
        }
    }

    def __init__(self, board):
        self.cityData = GameLogic.cityData
        GameLogic.mapCities(self, board)
        GameLogic.mapRoads(self, board)

    #Return a list of available cities and their position on the board in respect to tile IDs
    def mapCities(self, board):
        cityPositionList = []
        i = 0
        for Y in board.daBoard:
            for index, X in enumerate(board.daBoard[Y]):
                if X == '0' or re.search('^\\x1b\[3[1-5]m[xX]\\x1b\[0m$',X):
                    cityPositionList.append([index,Y])
        for row in self.cityData:
            for city in self.cityData[row]:
                print(cityPositionList)
                print(i)
                print(self.cityData)
                board.daBoard[cityPositionList[i][1]][cityPositionList[i][0]] = self.cityData[row][city]['Status']
                i += 1
        print("Towns/Cities mapped") 
    def mapRoads(self, board):
        roadPositionList = []
        i = 1
        for Y in board.daBoard:
            for index, X in enumerate(board.daBoard[Y]):
                if re.search("(-+)",X) or X == '/' or X == '\\':
                    roadPositionList.append([index, Y, i])
                    i += 1
                if re.search("^\n",X):
                    i = 1
            i = 1
        for entry in roadPositionList:
            if self.roadData[entry[1]][entry[2]]['Status'] != "/" and self.roadData[entry[1]][entry[2]]['Status'] != "\\":
                board.daBoard[entry[1]][entry[0]] = self.roadData[entry[1]][entry[2]]['Status'] * 5
            else:
                board.daBoard[entry[1]][entry[0]] = self.roadData[entry[1]][entry[2]]['Status']

    #Search for a city that contains the proper ID and position sequence if NA return null
    def buildTown(self, player, board, userInput):
        for row in self.cityData:
            for city in self.cityData[row]:
                for location in self.cityData[row][city]['Locations']:
                    if location == userInput:
                        if re.search('^\\x1b\[3[1-5]mx\\x1b\[0m$',self.cityData[row][city]['Status']):
                            print("A town already exist here!")
                            return
                        elif re.search('^\\x1b\[3[1-5]mX\\x1b\[0m$',self.cityData[row][city]['Status']):
                            print("A city already exist here!")
                            return
                        else:
                            self.cityData[row][city]['Status'] = f'{RED}x{RESET}'
                            GameLogic.mapCities(self, board)
                            for location in self.cityData[row][city]['Locations']:    
                                player.cityData['Towns'].append(location)
                            player.availableCities -= 1
                            print("Town Built!")
                            return
        print("Invalid Coordinates: "+userInput+". Please try again.")
        return

    def buildCity(self, player, board, userInput):
            for row in self.cityData:
                for city in self.cityData[row]:
                    for location in self.cityData[row][city]['Locations']:
                        if location == userInput:
                            if re.search('^\\x1b\[3[1-5]mx\\x1b\[0m$',self.cityData[row][city]['Status']):
                                self.cityData[row][city]['Status'] = f'{RED}X{RESET}'
                                GameLogic.mapCities(self, board)
                                for location in self.cityData[row][city]['Locations']:    
                                    player.cityData['Towns'].remove(location)
                                    player.cityData['Cities'].append(location)
                                print("City Built!")
                                return
                            elif re.search('^\\x1b\[3[1-5]mX\\x1b\[0m$',self.cityData[row][city]['Status']):
                                print("A city already exist here!")
                                return
                            else:
                                print("There is no town here!")
                                return
            print("Invalid Coordinates: "+userInput+". Please try again.")
            return

    #Roll the dice for the player, return the resources for that die results
    def rollDice(self, board, player):
        dieResult = random.randint(2,12) #Roll 2 dice
        print(f'Die Result: {dieResult}') #Debug checking
        for tile in board.boardMap:
            if tile.dieNumber == dieResult:
                #Check to see if player has any towns or cities on this tile
                for ownedTown in player.cityData['Towns']:
                    townLocation = ownedTown.split("-")
                    townID = townLocation[0]
                    if townID == str(tile.id) and tile.id != 9:
                        player.resources[tile.resource] += 1 #Give players one resource for town
                for ownedCity in player.cityData['Cities']:
                    cityLocation = ownedCity.split("-")
                    cityID = cityLocation[0]
                    if cityID == str(tile.id) and tile.id != 9:
                        player.resources[tile.resource] += 2 #Give players two resource for city
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
              ' ' * 10, '\\', '#', '/', ' ' * 7, '\\', '#', '/', '\n',
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

#Start of main biz
board = Board()
player = Player()
userInput = ""

#Setup Loop
while(userInput != "quit" and player.availableCities != 0):
    board.printBoard()
    userInput = input(f"""
Select where you would like to build a city.
Enter the tile ID (top number) followed by position:
Ex. 4-TL would place a town on tile 4 in the top left.
                      
You have {str(player.availableCities)} left to place.
""")
    if(userInput != "quit"):
        board.gameLogic.buildTown(player, board, userInput)
#Main Game Loop
while(userInput != "quit"):
    board.printBoard()
    player.printPlayer()
    userInput = input("""
What would you like to do?
1. roll - Roll the dice and collect your resources
2. upgrade town - Upgrade a town you currently own to a city
3. quit - Exit the game
""")
    if(userInput == "roll"):
        board.gameLogic.rollDice(board, player)
    elif(userInput == 'upgrade town'):
        userInput = input("What town would you like to upgrade?")
        board.gameLogic.buildCity(player, board, userInput)
    else:
        print(f"Invalid input: {userInput}. Please try again.")

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