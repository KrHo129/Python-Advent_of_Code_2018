# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 00:36:43 2018

@author: Blaž
"""

import sys

inputValue = 4172


def getCellFuelLevel(xPos, yPos, serialNumber):
    rackID = xPos + 10

    tempInt = ((yPos * rackID) + serialNumber) * rackID

    if (tempInt >= 100):
        tempStr = str(tempInt)
        hund = int(tempStr[-3])
    else:
        hund = 0
    
    cellsFuelLevel = hund - 5
    
    return (cellsFuelLevel)


def createEmptyGrid(gridSize):
    eGrid = [[None for x in range(gridSize)] for y in range (gridSize)]
    
    return(eGrid)

#a = []
def calculateSquereFuelLevel(xPos, yPos, squereSize, gridData):
    squereValues = []
    for xx in range(xPos, xPos + squereSize):
        for yy in range (yPos, yPos + squereSize):
#            try:
#                apendex = gridData[xx][yy]
#            except IndexError:
#                print(xx)
#                print(yy)
#                print(squereSize)
#                return
            
            squereValues.append(gridData[xx][yy])
#    print(squereValues)
#    print(len(squereValues))
#    global a
#    a= squereValues
    return sum(squereValues)


def task01(serialNum, gridSize):
    
    grid = createEmptyGrid(gridSize + 1)
    
    for x in range (1, gridSize + 1):
        for y in range (1, gridSize + 1):
            grid[x][y] = getCellFuelLevel(x, y, serialNum)
    
    
    maxSquereValue = -1 * sys.maxsize
    xResult = yResult = 0
    for x in range (1, gridSize - 2):
        for y in range (1, gridSize - 2):
            squereFuel = calculateSquereFuelLevel(x, y, 3, grid)
            if (squereFuel > maxSquereValue):
                maxSquereValue = squereFuel
                xResult = x
                yResult = y
    
    xyPos = [xResult, yResult, maxSquereValue]
    return xyPos



def task02_1(serialNum, gridSize):
    grid = createEmptyGrid(gridSize + 1)
    
    for x in range (1, gridSize + 1):
        for y in range (1, gridSize + 1):
            grid[x][y] = getCellFuelLevel(x, y, serialNum)
    
    maxSquereValue = -1 * sys.maxsize
    xResult = yResult = 0
    sizeResult = 0
    for i in range (1, gridSize + 1):
        print(i)
        for x in range (1, gridSize - i + 2):
            for y in range (1, gridSize - i + 2):
#                break
                squereFuel = calculateSquereFuelLevel(x, y, i, grid)
                if (squereFuel > maxSquereValue):
                    maxSquereValue = squereFuel
                    xResult = x
                    yResult = y
                    sizeResult = i
#        break
    result = [xResult, yResult, sizeResult]
    return result


def task02_2(serialNum, gridSize):
    grid = createEmptyGrid(gridSize + 1)
    
    for x in range (1, gridSize + 1):
        for y in range (1, gridSize + 1):
            grid[x][y] = getCellFuelLevel(x, y, serialNum)
    
    
    
    '''
    maxSquereValue = -1 * sys.maxsize
    xResult = yResult = -1
    sizeResult = 0
    xLast = yLast = 300
    for i in range (300, 0, -1):
        print(i)
        xLast = xResult + i + 1
        yLast = yResult + i + 1
        if (xResult <= 0):
            xResult = 1
        if (yResult <= 0):
            yResult = 1
        for x in range (xResult, xLast - i + 1):
            for y in range (yResult, yLast - i + 1):
#                break
                squereFuel = calculateSquereFuelLevel(x, y, i, grid)
                if (squereFuel > maxSquereValue):
                    maxSquereValue = squereFuel
                    xResult = x
                    yResult = y
                    sizeResult = i
                    
#        break
                    
    '''
    '''
    
#    print(grid[300][300])
    
    maxSquereValue = -1 * sys.maxsize
    xResult = yResult = 0
    sizeResult = 0
    
    xStart = yStart = 1
    xStop = yStop = gridSize
    for sqSize in range (gridSize, 0, -1):
#        print(sqSize)
        tempMaxValue = -1 * sys.maxsize
#        print (maxSquereValue)
#        if (sqSize == 280):
#            print(str(xStart) + "  " + str(xStop + 2 - sqSize))
#            print(str(yStart ) + "  " + str(yStop + 2 - sqSize))
        xTempStart = xStart
        xTempStop = xStop
        yTempStart = yStart
        yTempStop = yStop
#            return
        for x in range (xTempStart, xTempStop + 2 - sqSize):
            for y in range (yTempStart, yTempStop + 2 - sqSize):
#                print (str(xStart) + " " + str(xStop))
                    
                squereFuel = calculateSquereFuelLevel(x, y, sqSize, grid)

                if (sqSize == 50):
                    asa = []
                    asa.append(x)
                    asa.append(y)
                    print(asa)
                    print(squereFuel)

                if (squereFuel > tempMaxValue):
                    tempMaxValue = squereFuel
                    xStart = x
                    yStart = y
                    xStop = x + sqSize - 1
                    yStop = y + sqSize - 1
                    
                    if (squereFuel > maxSquereValue):
                        maxSquereValue = squereFuel
                        xResult = x
                        yResult = y
                        sizeResult = sqSize
    
    print(maxSquereValue)
    result = [xResult, yResult, sizeResult]
    print(calculateSquereFuelLevel(90, 269, 16, grid))
    return result



#result1 = task01(inputValue, 300)
#xRes, yRes = result1[0], result1[1]
#print("Result of taks 02 is : " + str(xRes) + "," + str(yRes))


'''


def task02_3(serialNum, gridSize):
    grid = createEmptyGrid(gridSize + 1)
    
    for x in range (1, gridSize + 1):
        for y in range (1, gridSize + 1):
            grid[x][y] = getCellFuelLevel(x, y, serialNum)
    
    maxSquereValue = -1 * sys.maxsize
#    xResult = yResult = 0
#    sizeResult = 0
    result = []
    
    '''
    spremeni tempX nazaj na 1 ko končaš
    '''
    tempX = 85
    
    for x in range (tempX, gridSize + 1):
        for y in range (1, gridSize + 1):
            if (x - 1 <= 300 - y):
                print("\nx: " + str (x) + " |  y: " + str(y))
                print(result)
            if (x > y):
                tempStartPos = x
            else:
                tempStartPos = y
            for i in range (1, gridSize - tempStartPos + 1):
                squereFuel = calculateSquereFuelLevel(x, y, i, grid)
                if (squereFuel > maxSquereValue):
                    maxSquereValue = squereFuel
#                    xResult = x
#                    yResult = y
#                    sizeResult = i
                    result = []
                    result = [x, y, i, maxSquereValue]
#        break
    return result




# [236, 151, 15, 127]
# 45, 93, 9, 44
# x = 85

t2 = task02_3(inputValue, 300)























    
    