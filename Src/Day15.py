# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 20:24:51 2018

@author: Blaž
"""

#from myClasses import KrHoClass as kc
import copy


def readFile(path):
    dataInput = []

    fileTxt = open (path, "r")
    
    for line in fileTxt:
        line = line.strip()
        lineArray = []
        for char in line:
            lineArray.append(char)
        dataInput.append(lineArray)
        
    fileTxt.close()
    
    return dataInput


def getAllCavernPositions(_originalGrid):
    allCavernPoss = []
    for y in range(len(_originalGrid)):
        for x in range(len(_originalGrid[y])):
            if (_originalGrid[y][x] != "#"):
                cavrnPos = [y, x]
                allCavernPoss.append(cavrnPos)
    return allCavernPoss

#def getDistanceBetweenTwoPoints (_point1, _point2):
#    yDist = abs(_point2[0] - _point1[0])
#    xDist = abs(_point2[1] - _point1[1])
#    
#    distance = yDist + xDist
#    
#    return distance


def getAdjacentPositions (_currPosition):
    adjacentPoss = []
    
    yCurr = _currPosition[0]
    xCurr = _currPosition[1]
    
    newPos = [yCurr + 1, xCurr]
    adjacentPoss.append(newPos)
    newPos = [yCurr - 1, xCurr]
    adjacentPoss.append(newPos)
    newPos = [yCurr, xCurr + 1]
    adjacentPoss.append(newPos)
    newPos = [yCurr, xCurr - 1]
    adjacentPoss.append(newPos)
    
    adjacentPoss.sort()

    return adjacentPoss

def isValidMove(_pos, _cavernPoss, _elfPoss, _goblinPoss):
    if (_pos in _cavernPoss and _pos not in _elfPoss and _pos not in _goblinPoss):
        return True
    else:
        return False


class PathWay:
    def __init__(self, _currPos, _startPos, _prevPos = None):
        self.currPos = _currPos
        self.startPos = _startPos
        self.prevPos = _prevPos
        
    def getStartPos(self):
        return self.startPos
    
    def getCurrPos(self):
        return self.currPos
    
    def getPrevPos (self):
        return self.prevPos

        
class Goblin:
    def __init__(self, _yPos, _xPos):
        self.yPos = _yPos
        self.xPos = _xPos
        self.health = 200
        self.attack = 3
        self.unitType = "G"
    
    def getUnitType (self):
        return self.unitType
    
    def getPosition(self):
        pos = [self.yPos, self.xPos]
        return pos
    
    def reduceHealth (self, _attValue):
        self.health -= _attValue
        return self.health
    
    def moveUnit(self, _cavernPoss, _elfPoss, _goblinPoss):
        startPos = self.getPosition()

        startAdjacentPos = getAdjacentPositions(startPos)
        
        adjacentPaths = []
        
        for pos in startAdjacentPos:
            if isValidMove(pos, _cavernPoss, _elfPoss, _goblinPoss):
                newPath = PathWay(pos, [pos])
                adjacentPaths.append(newPath)
        
        checkedPositions = []
        checkedPositions.append(startPos)
        
        targetPath = []
        
        while (len(adjacentPaths) > 0 and len(targetPath) <= 0):
            newPaths = []
            for p in adjacentPaths:
                
                pos = p.getCurrPos()

                if pos in _elfPoss:
                    targetPath.append(p)
                    
                elif (pos in checkedPositions):
                    for newP in newPaths:
                        if newP.getPrevPos() == pos:
                            for stPos in p.startPos:
                                if stPos not in newP.startPos:
                                    newP.startPos.append(stPos)
                            
                elif (isValidMove(pos, _cavernPoss, _elfPoss, _goblinPoss)):
                    adjPoss = getAdjacentPositions(pos)
                    for adjPos in adjPoss:
                        newPaths.append(PathWay(adjPos, p.getStartPos(), pos))
                    checkedPositions.append(pos)
            
            adjacentPaths = []
            adjacentPaths = copy.deepcopy(newPaths)
#        return targetPath
        if len(targetPath <= 0):
            return
        
        
        
        
        
        
    
    
    
    
    
        

class Elf:
    def __init__(self, _yPos, _xPos):
        self.yPos = _yPos
        self.xPos = _xPos
        self.health = 200
        self.attack = 3
        self.unitType = "E"
    
    def getUnitType (self):
        return self.unitType
    
    def getPosition(self):
        pos = [self.yPos, self.xPos]
        return pos
    
    def reduceHealth (self, _attValue):
        self.health -= _attValue
        return self.health
    
        
def getPersonList(_originalGrid):
    personList = [] 
    for y in range(len(_originalGrid)):
        for x in range(len(_originalGrid[y])):
            if _originalGrid[y][x] == "G":
                newGoblin = Goblin(y, x)
                personList.append(newGoblin)
            elif _originalGrid[y][x] == "E":
                newElf = Elf(y, x)
                personList.append(newElf)
    
    return (personList)
    

def getAllGoblinPositions (_personList):
    goblinPoss = []
    
    for pers in _personList:
        if pers.getUnitType() == "G":
            gPos = pers.getPosition()
            goblinPoss.append(gPos)
    
    return goblinPoss

def getAllElfPositions (_personList):
    elfPoss = []
    
    for pers in _personList:
        if pers.getUnitType() == "E":
            gPos = pers.getPosition()
            elfPoss.append(gPos)
    
    return elfPoss

b = []
 
def task01(txtPath):
    originalGrid = readFile(txtPath)
    cavernPositions = getAllCavernPositions(originalGrid)
    
    personList = getPersonList(originalGrid)
    
    elfPositions = getAllElfPositions(personList)
    goblinPositions = getAllGoblinPositions(personList)
    
    allUnitPositions = elfPositions + goblinPositions
    allUnitPositions.sort()
    
    
    
#    gg = Goblin(1, 4)
#    print (gg.findPathToClosestEnemyUnit(cavernPositions, elfPositions, allUnitPositions))
    
    a = Goblin(6,9)
    global b
    b = a.moveUnit(cavernPositions, elfPositions, goblinPositions)
    
#    for asd in b:
#        print(asd.pathList)
    
    
    return


dataInputPath = "Input Txts/Day15.txt"
testPath = "Input Txts/test.txt"
print (task01(dataInputPath))



