# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:08:49 2018

@author: Blaž
"""

inputDataIntArray = []

"""
    Reading input file
"""
inputFile = open ("Input Txts/Day01.txt", "r")

for line in inputFile:
    inputDataIntArray.append (line)

inputFile.close()

"""
    Task 1
"""
result1 = 0
for number in inputDataIntArray:
    result1 += int(number)

print ("Result 01 is: " + str(result1))

"""
    Task 2
"""
result2 = 0
currentFreq = 0
loopCounter = 0
matchFound = False
previousFreq = set()

while not matchFound:
    loopCounter += 1
    
    for number in inputDataIntArray:
        currentFreq += int(number)
        
        if (currentFreq in previousFreq):
            matchFound = True
            result2 = currentFreq
            break
        else:
            previousFreq.add(currentFreq)

print ("Result 02 is: " + str(result2))
print ("Required " + str(loopCounter) + " loops.")
