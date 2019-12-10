# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:19:40 2018

@author: Blaž
"""

dataArray = []

''' Reading File
'''
inputFile = open ("Input Txts/Day07.txt", "r")

for line in inputFile:
    splitedData = line.strip().split(" ")
    charBefore, charAfter = splitedData[1], splitedData[7]
    beforeAndAfterCher = []
    beforeAndAfterCher.append(charBefore)
    beforeAndAfterCher.append(charAfter)
    dataArray.append(beforeAndAfterCher)

dataArray.sort()

inputFile.close()

''' Task1
'''
def task01 (data):
    
    requiresCharDict = {}
    allChars = []
    
    for inputCharArray in data:
        beforeChar = inputCharArray[0]
        afterChar = inputCharArray[1]
        
        if (beforeChar not in allChars):
            allChars.append(beforeChar)
        if (afterChar not in allChars):
            allChars.append(afterChar)
        
        if (afterChar not in requiresCharDict):
            tempArray = []
            tempArray.append(beforeChar)
            requiresCharDict[afterChar] = tempArray
        else:
            tempArray = requiresCharDict[afterChar]
            tempArray.append(beforeChar)
    
    allChars.sort()
    
    sequence = ""
    counter= 0
    while (len(allChars) > 0):
        ''' tale while je kr neki
            lahko bi reku samo od in range (0-26)
            ampak zdj je že tko
        '''
        counter += 1
        if (counter > 100):
            print("while has broken")
            break
        for char in allChars:
            if (char not in requiresCharDict):
                sequence += char
                allChars.remove(char)
                break
            else:
                isOk = True
                for neededChar in requiresCharDict[char]:
                    if (neededChar not in sequence):
                        isOk = False
                        break
                if (isOk):
                    sequence += char
                    allChars.remove(char)
                    break
            
    result = sequence
    return (result)

''' Classes
'''
class Letter:
    def __init__(self, _char, _timeNeeded):
        self.char = _char
        self.timeNeeded = _timeNeeded

class Worker:
    def __init__ (self, _isFree, _workingTime, _targetTime, _workingChar, _justFinished):
        self.isFree = _isFree
        self.workingTime = _workingTime
        self.targetTime = _targetTime
        self.workingChar = _workingChar
        self.justFinished = _justFinished


def task02(data):
    requiresCharDict = {}
    allChars = []
    
    for inputCharArray in data:
        beforeChar = inputCharArray[0]
        afterChar = inputCharArray[1]
        
        if (beforeChar not in allChars):
            allChars.append(beforeChar)
        if (afterChar not in allChars):
            allChars.append(afterChar)
        
        if (afterChar not in requiresCharDict):
            tempArray = []
            tempArray.append(beforeChar)
            requiresCharDict[afterChar] = tempArray
        else:
            tempArray = requiresCharDict[afterChar]
            tempArray.append(beforeChar)
    
    allChars.sort()
    
    
    letersClassDict = {}
    for i in range (len(allChars)):
        tempLetter = Letter(allChars[i], 60 + i + 1)
        letersClassDict[allChars[i]] = tempLetter
    
    workerArray = []
    for i in range (5):
        workerArray.append(Worker(True, 0, 0, "", False))
    
    
    sequence = ""
    possibleCharsArray = []
    counter= 0
    while (len(sequence) < 26):
        ''' tale while je kr neki
            lahko bi reku samo od in range (0-26)
         ampak zdj je že tko
        '''
        counter += 1
        if (counter > 10000):
            print("while has broken")
            print(sequence)
            print(possibleCharsArray)
            break
        
        for char in allChars:
            if (char not in requiresCharDict):
                possibleCharsArray.append(char)
                allChars.remove(char)
            else:
                isOk = True
                for neededChar in requiresCharDict[char]:
                    if (neededChar not in sequence):
                        isOk = False
                        break
                if (isOk):
                    possibleCharsArray.append(char)
                    allChars.remove(char)
        
        completedChars = []
        possibleCharsArray.sort()
        for worker in workerArray:
            if (worker.isFree and len(possibleCharsArray) > 0):
                tempChar = possibleCharsArray[0]
                worker.isFree = False
                worker.workingTime = 0
                worker.workingChar = tempChar
                worker.targetTime = letersClassDict[tempChar].timeNeeded
                possibleCharsArray.remove(tempChar)
                
            if (not worker.isFree):
                worker.workingTime += 1
                if (worker.workingTime >= worker.targetTime):
                    completedChars.append(worker.workingChar)
                    worker.isFree = True
                    
        completedChars.sort()
        for singleChar in completedChars:
            sequence += singleChar
        
    result = counter
    return (result)

print ("Result of taks 01 is : " + task01(dataArray))
print("Result of taks 02 is : " + str(task02(dataArray)))
