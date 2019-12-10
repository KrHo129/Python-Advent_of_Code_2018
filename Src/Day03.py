# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:47:50 2018

@author: Blaž
"""

class SingleFabric:
    def __init__(self, awayFromLeft, awayFromTop, width, height):
        self.awayFromLeft = awayFromLeft
        self.awayFromTop = awayFromTop
        self.width = width
        self.height = height
        
inputDataDict = {}

"""
    Reading input file
"""
inputFile = open ("Input Txts/Day03.txt", "r")

for line in inputFile:
    tempSplitArray = (line.replace("#", "").replace("@", ",").replace(":", ",")
                                   .replace("x", ",").split(","))
    
    lineIndex = int(tempSplitArray[0].strip())
    tempFromLeft = int(tempSplitArray[1].strip())
    tempFromRight = int(tempSplitArray[2].strip())
    tempWidth = int(tempSplitArray[3].strip())
    tempHeight = int(tempSplitArray[4].strip())
    
    inputDataDict[lineIndex] = SingleFabric(tempFromLeft, tempFromRight,
                     tempWidth, tempHeight)
    
inputFile.close()

"""
    Task 1
"""
maxWidth = maxHeiht = 0

for index in inputDataDict:
    fabric = inputDataDict[index]
    currentWidth = fabric.awayFromLeft + fabric.width
    currentHeigt = fabric.awayFromTop + fabric.height
    
    if (currentWidth > maxWidth):
        maxWidth = currentWidth
    if (currentHeigt > maxHeiht):
        maxHeiht = currentHeigt

fabricMatrix = [[0 for x in range(1, maxWidth + 1)] for y in range(1, maxHeiht + 1)]
# fabricMatrix[y][x]

for index in inputDataDict:
    fabric = inputDataDict[index]
    for x in range(fabric.awayFromLeft, fabric.awayFromLeft + fabric.width):
        for y in range (fabric.awayFromTop, fabric.awayFromTop + fabric.height):
            fabricMatrix[y][x] += 1

overlapCounter = 0

for y in fabricMatrix:
    for x in y:
        if (x > 1):
            overlapCounter += 1

result01 = overlapCounter
print ("Result of task 1 is: " + str(result01))


"""
    Task 2
    // potrebuje Task 1!!
"""
overlapDetected = False
result02 = 0

for index in inputDataDict:
    fabric = inputDataDict[index]
    overlapDetected = False
    for x in range(fabric.awayFromLeft, fabric.awayFromLeft + fabric.width):
        for y in range (fabric.awayFromTop, fabric.awayFromTop + fabric.height):
            if (fabricMatrix[y][x] > 1):
                overlapDetected = True;
    if (not overlapDetected):
        result02 = index
        break
            
print("Result of task 2 is: " + str(result02))