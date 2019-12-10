# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:50:03 2018

@author: Blaž
"""

dataInput = []

''' Read File
'''
myInputFile = open("Input Txts/Day13.txt", "r")
#myInputFile = open("Input Txts/test.txt", "r")


for line in myInputFile:
    lineStr = line.strip("\n")
    tempCharArray = []
    for char in lineStr:
        tempCharArray.append(char)
    dataInput.append(tempCharArray)
    
myInputFile.close()


class Vagon:
    def __init__(self, yPos, xPos, direction, trailUnderVagon):
        self.yPos = yPos
        self.xPos = xPos
        self.direction = direction
        # 0 = left; 1 = up; 2 = right; 3 = down
        self.nextDirection = 1
        # 1 = left; 2 = stright; 3 = right
        self.trailUnderVagon = trailUnderVagon
    
    def setGrid (self, grid):
        self.grid = grid
        
    def getPosition (self):
        y = self.yPos
        x = self.xPos
        pos = [y, x]
        return pos
    
    def changeDirectionOnIntersection (self):
        nextDir = self.nextDirection
        if (nextDir == 1):
            self.nextDirection = 2
            self.direction -= 1
            if self.direction < 0:
                self.direction += 4
        elif (nextDir == 2):
            self.nextDirection = 3
        elif (nextDir == 3):
            self.nextDirection = 1
            self.direction += 1
            if (self.direction > 3):
                self.direction -= 4
        
    def moveLeft (self):
        self.xPos -= 1
        self.trailUnderVagon = self.grid[self.yPos][self.xPos]
    def moveUp (self):
        self.yPos -= 1
        self.trailUnderVagon = self.grid[self.yPos][self.xPos]
    def moveRight (self):
        self.xPos += 1
        self.trailUnderVagon = self.grid[self.yPos][self.xPos]
    def moveDown (self):
        self.yPos += 1
        self.trailUnderVagon = self.grid[self.yPos][self.xPos]
        
    def moveVagon(self):
        currDir = self.direction
        currTrail = self.trailUnderVagon
        
        if (currTrail == "+"):
            self.changeDirectionOnIntersection()
        
        currDir = self.direction
        if currDir == 0:
            if currTrail == "-" or currTrail == "+":
                self.moveLeft()
            elif currTrail == "/":
                self.moveDown()
                self.direction = 3
            elif (currTrail == "\\") :
                self.moveUp()
                self.direction = 1
            else:
                print("Move Vagon ERROR " + str(currDir))
            
            
        elif currDir == 1:
            if currTrail == "|" or currTrail == "+":
                self.moveUp()
            elif currTrail == "/":
                self.moveRight()
                self.direction = 2
            elif (currTrail == "\\") :
                self.moveLeft()
                self.direction = 0
            else:
                print("Move Vagon ERROR " + str(currDir))
            
        elif currDir == 2:
            if currTrail == "-" or currTrail == "+":
                self.moveRight()
            elif currTrail == "/":
                self.moveUp()
                self.direction = 1
            elif (currTrail == "\\") :
                self.moveDown()
                self.direction = 3
            else:
                print("Move Vagon ERROR " + str(currDir))
                
        elif currDir == 3:
            if currTrail == "|" or currTrail == "+":
                self.moveDown()
            elif currTrail == "/":
                self.moveLeft()
                self.direction = 0
            elif (currTrail == "\\") :
                self.moveRight()
                self.direction = 2
            else:
                print("Move Vagon ERROR " + str(currDir))




def findVagons(data):
    vagonChars = ["<", ">", "v", "^"]
    allVagonsArray = []
    for y in range (len(data)):
        for x in range(len(data[y])):
            char = data[y][x]
            if char in vagonChars:
                smer = -1
                if char == "<":
                    smer = 0
                    data[y][x] = "-"
                elif char == "^":
                    smer = 1
                    data[y][x] = "|"
                elif char == ">":
                    smer = 2
                    data[y][x] = "-"
                elif char == "v":
                    smer = 3
                    data[y][x] = "|"
                
                if smer == -1:
                    print("Direction Error!")
                    return
                
                newVagon = Vagon(y, x, smer, data[y][x])
                allVagonsArray.append(newVagon)
           
    return allVagonsArray
                

def getVagonFromArray(_vagonPosition, _vagonArray):
    for v in _vagonArray:
        if (v.getPosition() == _vagonPosition):
            return (v)
    
    print("Cannot find proper vagon!")
    return None


''' Task 01
'''
def task01(data):
    
    allVagons = findVagons(data)

    for singleVagon in allVagons:
        singleVagon.setGrid(data)
    
    vagonPositions = []
    for vagon in allVagons:
        vagonPositions.append(vagon.getPosition())
    
    vagonPositions.sort()
    
    brePoint = 0
    chrashDetected = False
    crashPos = [-1, -1]
        
    failSaveBreakCounter = 10000
    while (not chrashDetected):
        newVagonPositions = []
        
        currentPositions = []
        for p in vagonPositions:
            currentPositions.append(p)
            
        for vagPos in vagonPositions:
            vag = getVagonFromArray(vagPos, allVagons)
            
            vag.moveVagon()
            newPos = vag.getPosition()
            
            currentPositions.remove(vagPos)
            
            
            if newPos in currentPositions:
                chrashDetected = True
                crashPos = newPos
                break
            
            currentPositions.append(newPos)
            newVagonPositions.append(newPos)
            
        vagonPositions = newVagonPositions
        vagonPositions.sort()


        brePoint += 1
        if (brePoint > failSaveBreakCounter):
            print("While loop breaked after: " + str(failSaveBreakCounter) +
                  " cycles - to avoide endless loop!")
            break
    
#    print (brePoint)
    result = str(crashPos[1]) + "," + str(crashPos[0])
    return result


''' Task 02
'''
def task02(data):
    allVagons = findVagons(data)
    
    for singleVagon in allVagons:
        singleVagon.setGrid(data)
    
    vagonPositions = []
    for vagon in allVagons:
        vagonPositions.append(vagon.getPosition())
    vagonPositions.sort()
    
    brePoint = 0
    lastPos = [None, None]
        
    failSaveBreakCounter = 2* 10**4
    while (True):
        newVagonPositions = []
        currentPositions = []
        crashPositions = []
        
        
        for p in vagonPositions:
            currentPositions.append(p)
        
        for vagPos in list(vagonPositions):
            if vagPos in crashPositions:
                continue
            vag = getVagonFromArray(vagPos, allVagons)
            
            vag.moveVagon()
            newPos = vag.getPosition()
            
            currentPositions.remove(vagPos)
            
            if newPos in currentPositions:
                crashPositions.append(newPos)
                
            currentPositions.append(newPos)
            newVagonPositions.append(newPos)
        
        for cPos in crashPositions:
            while (cPos in newVagonPositions):
                newVagonPositions.remove(cPos)
            for sinVag in allVagons:
                if sinVag.getPosition() == cPos:
                    allVagons.remove(sinVag)
            print(f"Crash at: {cPos}; Iritation: {brePoint}; " +
                      f"Vagons left: {len(allVagons)}")
        
        if len(newVagonPositions) == 1:
            lastPos = newVagonPositions[0]
            break
        elif len(newVagonPositions) < 1:
            print ("Something went wrong!")
            break
        
        vagonPositions = []
        vagonPositions = newVagonPositions
        vagonPositions.sort()
        
        brePoint += 1
        if (brePoint > failSaveBreakCounter):
            print("While loop breaked after: " + str(failSaveBreakCounter) +
                  " cycles - to avoide endless loop!")
            break
    
    
    result = str(lastPos[1]) + "," + str(lastPos[0])
    return result




from myClasses import KrHoClass as kc

print(f"\nResult of taks 01 is: {task01(kc().copyList(dataInput))}\n")
print(f"\nResult of taks 02 is: {task02(kc().copyList(dataInput))}")







