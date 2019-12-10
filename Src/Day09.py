# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 23:25:19 2018

@author: Blaž
"""

dataInput = []

''' Functions
'''
def isNumeric (s):
    try:
        int(s)
        return True
    except ValueError:
        return False


''' Reading File
'''
inputFile = open ("Input Txts/Day09.txt", "r")

txt = inputFile.read()
splitedTxt = txt.split(" ")

for word in splitedTxt:
    if (isNumeric(word)):
        dataInput.append(int(word))

inputFile.close()

''' Classes
'''
class Player:
    score = 0
    
    def __init__(self, _playerIndex):
        self.playerIndex = _playerIndex
    def increseScore(self, _scoreIncrese):
        self.score += _scoreIncrese

''' Task01
'''
def task01 (data, multiplyer):
    arrayList = []
    valuesArray = []
    valuesArray.append(0)
    
    numOfPlayers = data[0]
    lastMarble = data[1] * multiplyer
    arrayMaxLen = 100
    
    currentPos = 0
    playerOnHisTurn = 0
    players = {}
    currentList = 0
    
    for currentValue in range (1, lastMarble + 1):
        playerOnHisTurn += 1
        if (playerOnHisTurn > numOfPlayers):
            playerOnHisTurn -= numOfPlayers
            
        if (currentValue % 23 == 0):
            if (playerOnHisTurn not in players):
                newPlayer = Player(playerOnHisTurn)
                players[playerOnHisTurn] = newPlayer
            
            players[playerOnHisTurn].increseScore(currentValue)
            
            currentPos -= 7
            if (currentPos < 0):
                if (len(arrayList) == 0):
                    currentPos += len(valuesArray)
                else:
                    arrayList.insert(currentList, valuesArray)
                    currentList -= 1
                    currentList = arrayList.index(arrayList[currentList])
                    valuesArray = arrayList[currentList]
                    del arrayList[currentList]
                    currentPos = valuesArray.index(valuesArray[currentPos])
                    
            players[playerOnHisTurn].increseScore(valuesArray[currentPos])
            valuesArray.remove(valuesArray[currentPos])
            
            if (currentPos > len(valuesArray) - 1):
                currentPos = 0
                print ("ERROR")
                break
        else:
            currentPos += 2
            if currentPos > len(valuesArray):
                if len(arrayList) == 0:
                    while (currentPos > len(valuesArray)):
                        currentPos -= len(valuesArray)
                else:
                    currentPos = 1
                    if (currentList >= len(arrayList)):
#                        print(1)
                        arrayList.insert(currentList, valuesArray)
                        valuesArray = arrayList[0]
                        currentList = 0
                        del arrayList [currentList]
                    else:
#                        print(2)
                        arrayList.insert(currentList, valuesArray)
                        currentList += 1
                        valuesArray = arrayList[currentList]
                        del arrayList [currentList]
            
            valuesArray.insert(currentPos, currentValue)
            
        if (len(valuesArray) > arrayMaxLen and currentPos > arrayMaxLen + 50):
            storeArray = valuesArray[:arrayMaxLen]
            valuesArray = valuesArray[arrayMaxLen:]
            arrayList.insert(currentList, storeArray)
            currentList += 1
            currentPos -= arrayMaxLen
            
    winningScore = 0
    
    for playerIndex in players:
        if (players[playerIndex].score > winningScore):
            winningScore = players[playerIndex].score
    
    return (winningScore)


# drugi del rabi 20 sekund
print ("Result of taks 01 is : " + str(task01(dataInput, 1)))
print ("Result of taks 01 is : " + str(task01(dataInput, 100)))
