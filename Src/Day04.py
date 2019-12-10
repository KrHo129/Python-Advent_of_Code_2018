# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:58:41 2018

@author: Blaž
"""

unsplitInputDataArray = []
sortedInputData = []
guardSleepingTimeDict = {}

"""
    Reading input file
"""
inputFile = open ("Input Txts/Day04.txt", "r")

for line in inputFile:
    unsplitInputDataArray.append(line)

inputFile.close()

"""
    Classes
"""
class DataLine:
    def __init__ (self, _date, _time, _guardID, _isAsleep, _newShift):
        self.date = _date
        self.time = _time
        self.guardID = _guardID
        self.isAsleep = _isAsleep
        self.newShift = _newShift
      
"""
    Functions
"""
def organizeData():
    unsplitInputDataArray.sort()
    for data in unsplitInputDataArray:
        seperatedTimeAndInfo = data.replace("[", "").strip().split("]")
        dateWithTime = seperatedTimeAndInfo[0].replace(" ", ",").split(",")
        dateOnly = dateWithTime[0]
        timeOnly = str(dateWithTime[1]).replace(":", "")
        infoOnly = seperatedTimeAndInfo[1].strip()
        
        splitedInfo = []
        splitedInfo.clear()
        splitedInfo = infoOnly.split(" ")
        #infoType [awaknes, guardId]
        if (splitedInfo[0] == "Guard"):
            infoType = "guardID"
            tempGuardID = splitedInfo[1].replace ("#", "")
            tempNewShift = True
        elif (splitedInfo[0] == "falls" or splitedInfo[0] == "wakes"):
            infoType = "awaknes"
            tempNewShift = False
        else:
            infoType = "Error"
            
        if (infoType == "Error"):
            print("Something went wrong while organising data")
            return
        
        if (infoType != "awaknes" or splitedInfo[0] == "wakes"):
            guardAwake = False
        elif (splitedInfo[0] == "falls"):
            guardAwake = True
        
        tempDataLine = DataLine(dateOnly, int(timeOnly), tempGuardID,
                                guardAwake, tempNewShift)
        sortedInputData.append(tempDataLine)


def createSleepingDictionary():
    
    tempSleepingData = ["null" for x in range(60)]
    prevID = 0
    
    for data in sortedInputData:
        if (prevID == 0):
            prevID = data.guardID
        if (data.isAsleep and data.time < 100):
            tempSleepingData[data.time] = "sleeps"
        elif (not data.isAsleep and data.time < 100 and not data.newShift):
            tempSleepingData[data.time] = "wakesUp"
        
        if (not data.guardID in guardSleepingTimeDict):
            guardSleepingTimeDict[data.guardID] = [0 for x in range(60)]
        
        if (data.newShift):
            guardSleeps = False
            for minute in range (60):
                if (tempSleepingData[minute] == "sleeps"):
                    guardSleeps = True
                elif (tempSleepingData[minute] == "wakesUp"):
                    guardSleeps = False
                    
                if (guardSleeps):
                    guardSleepingTimeDict[prevID][minute] += 1
            
            tempSleepingData = ["null" for x in range(60)]
            prevID = data.guardID
    
    # še za zadnjega, ker se podatki ne končajo z novo izmeno in zato
    # v loopu ne preverimo zadnje izmene
    guardSleeps = False
    for minute in range (60):
        if (tempSleepingData[minute] == "sleeps"):
            guardSleeps = True
        elif (tempSleepingData[minute] == "wakesUp"):
            guardSleeps = False
            
        if (guardSleeps):
            guardSleepingTimeDict[prevID][minute] += 1

"""
    Task 01
"""
organizeData()
createSleepingDictionary()

guardIdWithMostSleepTime = maxTotalSleepingTime = 0

for dictIndex in guardSleepingTimeDict:
    sleepCounterArray = guardSleepingTimeDict[dictIndex]
    guardTotalSleepingTime = 0
    
    for minute in range (60):
        guardTotalSleepingTime += sleepCounterArray[minute]
    
    if (guardTotalSleepingTime > maxTotalSleepingTime):
        maxTotalSleepingTime = guardTotalSleepingTime
        guardIdWithMostSleepTime = dictIndex
        
sleepCounterArray = guardSleepingTimeDict[guardIdWithMostSleepTime]
minuteWithMaxSleepCounter = -1
maxCounter = 0

for minute in range (60):
    minuteSleepCounter = sleepCounterArray[minute]
    if (minuteSleepCounter > maxCounter):
        maxCounter = minuteSleepCounter
        minuteWithMaxSleepCounter = minute

result01 = int(guardIdWithMostSleepTime) * minuteWithMaxSleepCounter
print ("Result of taks 01 is : " + str(result01))


"""
    Task 02
"""
##done in Task 01
#organizeData()
#createSleepingDictionary()

minuteWithMaxSleepCounter = -1
maxSleepCounter = resultGuardID = 0

for dictIndex in guardSleepingTimeDict:
    sleepCounterArray = guardSleepingTimeDict[dictIndex]
    
    for minute in range (60):
        if (sleepCounterArray[minute] > maxSleepCounter):
            maxSleepCounter = sleepCounterArray[minute]
            minuteWithMaxSleepCounter = minute
            resultGuardID = dictIndex

result02 = int(resultGuardID) * minuteWithMaxSleepCounter
print ("Result of taks 02 is : " + str(result02))












