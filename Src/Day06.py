# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:37:39 2018

@author: Blaž
"""

rawDataInputArray = []
#procesedInputDataArray = []

''' Reading Input File
'''
inputFile = open ("Input Txts/Day06.txt", "r")

for line in inputFile:
    rawDataInputArray.append(line.strip())

inputFile.close()

''' Functions
'''
def organiseData(data):
    procesedInputDataArray = []
    
    for line in data:
        coordinatesOnly = line.split(",")
        x = int(coordinatesOnly[0].strip())
        y = int(coordinatesOnly[1].strip())
        xyCoor = []
        xyCoor.append(x)
        xyCoor.append(y)
        procesedInputDataArray.append(xyCoor)
    
    procesedInputDataArray.sort()
    
    return (procesedInputDataArray)

def create2DGrid(procData):
    xMax = yMax = 0
    
    for coor in procData:
        if (coor[0] > xMax):
            xMax = coor[0]
        if (coor[1] > yMax):
            yMax = coor[1]
    
    gridValues = [["0" for y in range (yMax + 1)] for x in range (xMax + 1)]
    
    coordinatesDict = {}
    for i in range(1, len(procData) + 1):
        coordinatesDict[i] = procData[i - 1]
        
    for y in range (yMax):
        for x in range (xMax):
            minDistance = xMax + yMax
            minDistStr = ""
            distance = 0
            for i in range(1, len(procData) + 1):
                
                xDist = abs(coordinatesDict[i][0] - x)
                yDist = abs(coordinatesDict[i][1] - y)
                distance = xDist + yDist
                if (minDistance > distance):
                    minDistance = distance
                    minDistStr = str(i)
                elif (minDistance == distance):
                    minDistStr += ", " + str(i)
            gridValues[x][y] = minDistStr
    
    return (gridValues)



def createBorderValuesList(gridValues):
    borderValues = []
    
    xSize = len(gridValues)
    ySize = len(gridValues[0]) 
    
    for x in range (xSize):
        value = gridValues[x][0]
        if (value not in borderValues):
            borderValues.append(value)
            
        value = gridValues[x][ySize - 1]
        if (value not in borderValues):
            borderValues.append(value)
       
    for y in range (ySize):
        value = gridValues[0][y]
        if (value not in borderValues):
            borderValues.append(value)
            
        value = gridValues[xSize - 1][y]
        if (value not in borderValues):
            borderValues.append(value)

    return (borderValues)


def is_intiger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def countAreasInRange(procData, _range):
     
    xMax = yMax = 0
     
    for coor in procData:
        if (coor[0] > xMax):
            xMax = coor[0]
        if (coor[1] > yMax):
            yMax = coor[1]
        
    totalDistance = 0
    regionsCount = 0
    
    coordinatesDict = {}
    for i in range(1, len(procData) + 1):
        coordinatesDict[i] = procData[i - 1]
        
    for x in range (xMax):
        for y in range (yMax):
            totalDistance = 0
            for i in range(1, len(procData) + 1):
                xDist = abs(coordinatesDict[i][0] - x)
                yDist = abs(coordinatesDict[i][1] - y)
                totalDistance += xDist + yDist
                if (totalDistance > _range):
                    break
                
            if (totalDistance < _range):
                regionsCount += 1
        
    return (regionsCount)
    
''' Task 01
'''
def task1(rawData):
    procData = organiseData(rawData)
    gridValues = create2DGrid(procData)
    borderValues = createBorderValuesList(gridValues)
    
    valueCountDict = {}
    maxValueCount = 0
    valueWithMaxCount = ""
    
    for lineArray in gridValues:
        for value in lineArray:
            if (is_intiger(value) and value not in borderValues):
                if (value not in valueCountDict):
                    valueCountDict[value] = 1
                else:
                    valueCountDict[value] += 1
    
    for dictIndex in valueCountDict:
        valueCount = valueCountDict[dictIndex]
        if (valueCount > maxValueCount):
            maxValueCount = valueCount
            valueWithMaxCount = dictIndex
    
    result = maxValueCount
#    print (valueWithMaxCount)
    return result
    
    
''' Task 02
'''
def task2 (rawData):
    procData = organiseData(rawData)
    _range = 10000
    result = countAreasInRange(procData, _range)
    
    return result
    


print("Result of taks 01 is : " + str(task1(rawDataInputArray)))
print("Result of taks 02 is : " + str(task2(rawDataInputArray)))
    