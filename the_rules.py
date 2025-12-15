import random
import re

RED = "\x1b[31m"
GREEN = "\x1b[32m"
BLUE = "\x1b[34m"
MAG = "\x1b[35m"
RESET = "\x1b[0m"

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
            "Connections": ["B3", "B4"]
        }
    },
    "D": {
        1: {
            "Status": '/',
            "Connections": ["B1", "C2"]
        },
        2: {
            "Status": '\\',
            "Connections": ["B2", "C3"]
        },
        3: {
            "Status": '/',
            "Connections": ["B3", "C4"]
        },
        4: {
            "Status": '\\',
            "Connections": ["B4", "C5"]
        }
    },
    "E": {
        1: {
            "Status": '-',
            "Connections": ["C1", "C2"]
        },
        2: {
            "Status": '-',
            "Connections": ["C3", "C4"]
        },
        3: {
            "Status": '-',
            "Connections": ["C5", "C6"]
        }
    },
    "F": {
        1: {
            "Status": '/',
            "Connections": ["C1", "D1"]
        },
        2: {
            "Status": '\\',
            "Connections": ["C2", "D2"]
        },
        3: {
            "Status": '/',
            "Connections": ["C3", "D3"]
        },
        4: {
            "Status": '\\',
            "Connections": ["C4", "D4"]
        },
        5: {
            "Status": '/',
            "Connections": ["C5", "D5"]
        },
        6: {
            "Status": '\\',
            "Connections": ["C6", "D6"]
        }
    },
    "G": {
        1: {
            "Status": '-',
            "Connections": ["D2", "D3"]
        },
        2: {
            "Status": '-',
            "Connections": ["D4", "D5"]
        }
    },
    "H": {
        1: {
            "Status": '\\',
            "Connections": ["D1", "E1"]
        },
        2: {
            "Status": '/',
            "Connections": ["D2", "E2"]
        },
        3: {
            "Status": '\\',
            "Connections": ["D3", "E3"]
        },
        4: {
            "Status": '/',
            "Connections": ["D4", "E4"]
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
            "Locations": ["9-CR", "7-BL", "12-TL"]
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

#Handles all game logic. (Rolling dice, purchasing and placing cities/roads/cards)
class GameLogic:
    def __init__(self, board):
        self.cityData = cityData
        self.roadData = roadData
        board.daBoard = updateCities(self.cityData, board.daBoard)
        updateRoads(self.roadData, board.daBoard)

    #Search for a city that contains the proper ID and position sequence if NA return null
    def buildTown(self, player, board, userInput):
        for row in self.cityData:
            for city in self.cityData[row]:
                for location in self.cityData[row][city]['Locations']:
                    if location == userInput:
                        if re.search(r'^\x1b\[3[1-5]mx\x1b\[0m$',self.cityData[row][city]['Status']):
                            print("A town already exist here!")
                            return -1
                        elif re.search(r'^\x1b\[3[1-5]mX\x1b\[0m$',self.cityData[row][city]['Status']):
                            print("A city already exist here!")
                            return -1
                        else:
                            self.cityData[row][city]['Status'] = f'{RED}x{RESET}'
                            board.daBoard = updateCities(self.cityData, board.daBoard)
                            for location in self.cityData[row][city]['Locations']:    
                                player.cityData['Towns'].append(location)
                            player.availableCities -= 1
                            player.currentPoints += 1
                            userInputConnection = coordsToCityPos(userInput, self.cityData)
                            cityVerification(player, userInputConnection)
                            print("Town Built!")
                            print(player.longestRoadData)
                            return 0
        print("Invalid Coordinates: "+userInput+". Please try again.")
        return -1

    def buildCity(self, player, board, userInput):
        if (player.resources['Ore'] < 3 and player.resources['Grain'] < 2):
            print(f"""
Insufficient Resources. Must have:
1/{player.resources['Ore']} Ore
1/{player.resources['Grain']} Grain
""")
            return -1
            
        for row in self.cityData:
            for city in self.cityData[row]:
                for location in self.cityData[row][city]['Locations']:
                    if location == userInput:
                        if re.search(r'^\x1b\[3[1-5]mx\x1b\[0m$',self.cityData[row][city]['Status']):
                            self.cityData[row][city]['Status'] = f'{RED}X{RESET}'
                            board.daBoard = updateCities(self.cityData, board.daBoard)
                            for location in self.cityData[row][city]['Locations']:    
                                player.cityData['Towns'].remove(location)
                                player.cityData['Cities'].append(location)
                            player.currentPoints += 1
                            print("City Built!")
                            return 0
                        elif re.search(r'^\x1b\[3[1-5]mX\x1b\[0m$',self.cityData[row][city]['Status']):
                            print("A city already exist here!")
                            return -1
                        else:
                            print("There is no town here!")
                            return -1
        print("Invalid Coordinates: "+userInput+". Please try again.")
        return -1

    def buildRoad(self, player, board, userInput, previousPoint):
        #Fetch the points
        previousPointConnection = coordsToCityPos(previousPoint, self.cityData)
        userInputConnection = coordsToCityPos(userInput, self.cityData)
        #Built the road
        for row in self.roadData:
            for road in self.roadData[row]:
                if (userInputConnection in roadData[row][road]["Connections"]) and (previousPointConnection in roadData[row][road]["Connections"]):
                    if re.search(r'^\x1b\[3[1-5]m[-\\/]\x1b\[0m$',self.roadData[row][road]['Status']):
                        print("A road already exist here!")
                        return -1
                    else:
                        self.roadData[row][road]['Status'] = f'{RED}{self.roadData[row][road]['Status']}{RESET}'
                        board.daBoard = updateRoads(self.roadData, board.daBoard)    
                        player.roadData.append([row,road])
                        player.availableRoads -= 1
                        roadVerification(player, userInputConnection, previousPointConnection, self.cityData)
                        print("Road Built!")
                        return 0
        print("Invalid Coordinates: "+userInput+". Please try again.")
        return -1

    def buildNewTown(self, player, board, userInput):
        if (player.resources['Brick'] < 1 and player.resources['Lumber'] < 1 and player.resources['Wool'] < 1 and player.resources['Grain'] < 1):
            print(f"""
Insufficient Resources. Must have:
1/{player.resources['Brick']} Brick
1/{player.resources['Lumber']} Lumber
1/{player.resources['Wool']} Wool
1/{player.resources['Grain']} Grain
""")
            return -1
        
        userInputConnection = coordsToCityPos(userInput, self.cityData)
        if userInputConnection != -1:
            for road in player.roadData:
                if userInputConnection in self.roadData[road[0]][road[1]]['Connections']:
                    GameLogic.buildTown(self, player, board, userInput)
                    return 0
        print("Invalid Coordinates: "+userInput+". Please try again")
        return -1
    
    def buildNewRoad(self, player, board, userInput):
        if (player.resources['Brick'] < 1 and player.resources['Lumber'] < 1):
            print(f"""
Insufficient Resources. Must have:
1/{player.resources['Brick']} Brick
1/{player.resources['Lumber']} Lumber
""")
            return -1

        userInputTokens = userInput.split("/")
        if(len(userInputTokens) != 2):
            print(f"Invalid range: {userInput}")
            return -1

        previousPointConnection = coordsToCityPos(userInputTokens[0], self.cityData)
        validationFlag = 0
        for entry in player.roadData:
            if previousPointConnection in roadData[entry[0]][entry[1]]['Connections']:
                validationFlag = 1

        if validationFlag != 1:
            print("No Connecting road")
            return -1

        result = GameLogic.buildRoad(self, player, board, userInputTokens[1], userInputTokens[0])
        if  result == 0:
            player.resources['Brick'] -= 1
            player.resources['Lumber'] -= 1

        return result
    
    #Roll the dice for the player, return the resources for that die results
    def rollDice(self, board, player):
        dieResult = random.randint(2,12) #Roll 2 dice
        print(f'Die Result: {dieResult}') #Debug checking
        if dieResult != 7:
            for tile in board.boardMap:
                if tile.dieNumber == dieResult and tile.gk == False:
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
        else:
            newUserInput = input("""
You rolled a 7. Where would you like to place Genghis Khan?
Enter the tile ID you would like to place him on
""")
            returnFlag = board.moveGK(newUserInput)
            while returnFlag != 0:
                newUserInput = input("""
Where would you like to place Genghis Khan?
Enter the tile ID you would like to place him on
""")
                returnFlag = board.moveGK(newUserInput)
        return 0

#Seperate Functions
#Return a list of available cities and their position on the board in respect to tile IDs
def mapCities(board):
    cityPositionList = []
    for Y in board:
        for index, X in enumerate(board[Y]):
            if X == '0' or re.search(r'^\x1b\[3[1-5]m[xX]\x1b\[0m$',X):
                cityPositionList.append([index,Y])
    print("Town/Cities mapped")
    return cityPositionList

def updateCities(data, board):
    cityPositionList = mapCities(board)
    i = 0
    for row in data:
        for city in data[row]:
            board[cityPositionList[i][1]][cityPositionList[i][0]] = data[row][city]['Status']
            i += 1
    print("Towns/Cities updated")
    return board

def mapRoads(board):
    roadPositionList = []
    i = 1
    for Y in board:
        for index, X in enumerate(board[Y]):
            if re.search(r'(-+)',X) or X == '/' or X == '\\' or re.search(r'^\x1b\[3[1-5]m[\\/-]\x1b\[0m$', X):
                roadPositionList.append([index, Y, i])
                i += 1
            if re.search(r'^\n',X):
                i = 1
        i = 1
    print("Roads mapped")
    return roadPositionList
    

def updateRoads(data, board):
    roadPositionList = mapRoads(board)
    for entry in roadPositionList:
        if re.search(r'^\x1b\[3[1-5]m[\\/]\x1b\[0m$', data[entry[1]][entry[2]]['Status']):
            board[entry[1]][entry[0]] = data[entry[1]][entry[2]]['Status']
        elif data[entry[1]][entry[2]]['Status'] != "/" and data[entry[1]][entry[2]]['Status'] != "\\":
            board[entry[1]][entry[0]] = data[entry[1]][entry[2]]['Status'] * 5
        else:
            board[entry[1]][entry[0]] = data[entry[1]][entry[2]]['Status']
    return board

def coordsToCityPos(userInput, data):
    for row in data:
        for city in data[row]:
            if userInput in data[row][city]["Locations"]:
                return f'{row}{city}'
    return -1

def roadVerification(player, endPoint, startPoint, cityData):
    #Verify city locations
    startPointTokens = list(startPoint)

    #If there is a city at the starting point begin a new longest road entry
    print(cityData[startPointTokens[0]][int(startPointTokens[1])])
    if(cityData[startPointTokens[0]][int(startPointTokens[1])]['Status'] != '0'):
        print("Creating new road")
        newEntry = {
            "Sequence": [startPoint, endPoint],
            "NoOfRoads": 1
        }
        player.longestRoadData.append(newEntry)
        return 0
    #If there is a city at the ending point find the entries with the starting point, normal entry
    for longRoadData in player.longestRoadData:
        print("Updating road")
        if startPoint in longRoadData['Sequence']:
            if (longRoadData['Sequence'][-1] == startPoint):
                print("Adding to existing road")
                longRoadData['Sequence'].append(endPoint)
                longRoadData['NoOfRoads'] += 1

                for longRoadData2 in player.longestRoadData:
                    if (longRoadData2['Sequence'][-1] == endPoint) and longRoadData2 != longRoadData:
                        print("Merging Roads")
                        index = len(longRoadData2['Sequence']) - 2
                        while index >= 0:
                            longRoadData['Sequence'].append(longRoadData2['Sequence'][index])
                            longRoadData['NoOfRoads']+=1
                            index -= 1
                        player.longestRoadData.remove(longRoadData2)
                return 0
            else:
                #Verify forks in road
                print("Splitting Road")
                index = 0
                newEntry = {
                    "Sequence": [],
                    "NoOfRoads": 0
                }
                while longRoadData['Sequence'][index] != startPoint:
                    newEntry['Sequence'].append(longRoadData['Sequence'][index])
                    newEntry['NoOfRoads'] += 1
                    index += 1

                newEntry['Sequence'].append(startPoint)
                newEntry['Sequence'].append(endPoint)
                newEntry['NoOfRoads'] += 1
                player.longestRoadData.append(newEntry)
                return 0

def cityVerification(player, startPoint):
    for longRoadData in player.longestRoadData:
        if startPoint in longRoadData['Sequence'] and (startPoint != longRoadData['Sequence'][-1] or startPoint != longRoadData['Sequence'][0]):
            print("Splitting road")
            newEntryA = {
                "Sequence": [],
                "NoOfRoads": 0
            }
            newEntryB = {
                "Sequence": [],
                "NoOfRoads": 0
            }
            
            index = 0
            sequencePoint = longRoadData['Sequence'][index]

            while sequencePoint != startPoint:
                newEntryA['Sequence'].append(longRoadData['Sequence'][index])
                newEntryA['NoOfRoads'] += 1
                index += 1
                sequencePoint = longRoadData['Sequence'][index]
            newEntryA['Sequence'].append(longRoadData['Sequence'][index])

            while index != len(longRoadData['Sequence']) - 1:
                newEntryB['Sequence'].append(longRoadData['Sequence'][index])
                newEntryB['NoOfRoads'] += 1
                index += 1
            newEntryB['Sequence'].append(longRoadData['Sequence'][index])

            player.longestRoadData.append(newEntryA)
            player.longestRoadData.append(newEntryB)
            player.longestRoadData.remove(longRoadData)
            return 0
    print()