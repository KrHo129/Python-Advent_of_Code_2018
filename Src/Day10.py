# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:38:34 2018

@author: Blaž
"""

import re # za napredni split
dataInput = []


class Data:
    def __init__(self, _xPos, _yPos, _xVel, _yVel):
        self.xPos = _xPos
        self.yPos = _yPos
        self.xVel = _xVel
        self.yVel = _yVel


def isNumeric(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

''' Reading File
'''
inputFile = open ("Input Txts/Day10.txt", "r")
#inputFile = open ("Input Txts/test.txt", "r")

for line in inputFile:
    numericData = []
    splitedLine = re.split("<|>|,", line)
    for word in splitedLine:
        word = word.strip()
        if (isNumeric(word)):
            numericData.append(int(word))
    xP, yP, xV, yV = numericData
    newData = Data(xP, yP, xV, yV)
    dataInput.append(newData)

inputFile.close()


def addVelocity(data):
    for d in data:
        d.xPos += d.xVel
        d.yPos += d.yVel
    
    return (data)

def reduceVelocity (data):
    for d in data:
        d.xPos -= d.xVel
        d.yPos -= d.yVel

def displayData(finalData):
    '''
    allValues = []
    for singleData in finalData:
        allValues.append(singleData.xPos)
        allValues.append(singleData.yPos)
    
    valueMin = (min(allValues)) 
    valueMax = (max(allValues)) 

    gridSize = (valueMax - valueMin) + 3
    for singleData in finalData:
        singleData.xPos = singleData.xPos - valueMin
        singleData.yPos = singleData.yPos - valueMin
    '''
    valsX = []
    valsY = []
    for sData in finalData:
        valsX.append(sData.xPos)
        valsY.append(sData.yPos)
    
    xMin = min(valsX)
    xMax = max(valsX)
    yMin = min(valsY)
    yMax = max(valsY)
    
    if (xMin < 0):
        for sData in finalData:
            sData.xPos += abs(xMin)
        xMax += abs(xMin)
        xMin += abs(xMin)
    else:
        for sData in finalData:
            sData.xPos -= xMin
        xMax -= xMin
        xMin -= xMin
    if (yMin < 0):
        for sData in finalData:
            sData.yPos += abs(yMin)
        yMax += abs(yMin)
        yMin += abs(yMin)
    else:
        for sData in finalData:
            sData.yPos -= yMin
        yMax -= yMin
        yMin -= yMin
        
    grid = [["." for x in range (xMax+1)] for y in range(yMax+1)]
    for singleData in finalData:
        grid[singleData.yPos][singleData.xPos] = "#"
    
    printGrid = ""
    for line in grid:
        for char in line:
            printGrid += char
        printGrid += "\n"
            
    print (printGrid)
    return


def task01(data, repeatCount):
    
    allValues = []
    for singleData in data:
        allValues.append(singleData.xPos)
        allValues.append(singleData.yPos)
    
    maxValue = max(allValues)
    
    changedData = data
    for i in range (repeatCount):
        changedData = addVelocity(changedData)
        newAllValues = []
        for singleData in changedData:
            newAllValues.append(singleData.xPos)
            newAllValues.append(singleData.yPos)
        
        newMaxValue = max(newAllValues)
        if (newMaxValue < maxValue):
            maxValue = newMaxValue
        else:
            reduceVelocity(changedData)
            displayData(changedData)
            return (i)

maxRepeatCount = 50000  # za vsak slučaj, da ne naredimo endless loop

print ("Result of taks 02 is : " + str(task01(dataInput, maxRepeatCount)))    
# 10418