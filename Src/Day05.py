# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:37:06 2018

@author: Blaž
"""


inputDataString = ""


''' Reading File
'''
fileSource = open ("Input Txts/Day05.txt", "r")

inputDataString = fileSource.read().strip()

fileSource.close()


''' Task 1
'''
def task01(dataString, getResultType):
    charIndex = 0
    
    while charIndex < len(dataString) - 1:
        char1 = dataString[charIndex]
        char2 = dataString[charIndex+1]
        
        if (char1.lower() == char2.lower() and char1 != char2):
            dataString = dataString[:charIndex] + dataString [charIndex + 2 :]
            if (charIndex > 0):
                charIndex -= 1
        else:
            charIndex += 1
        
    if (getResultType == "length"):
        result = len(dataString)    
    if (getResultType == "procesedDataArray"):
        result = dataString

    return result


''' Task2
'''
def task02 (dataString):
    allCharsInInputData = []
    
    minLength = -1
    
    for char in dataString:
        if (char.lower() not in allCharsInInputData):
            allCharsInInputData.append(char)
    dataString = task01(dataString, "procesedDataArray")
    
    for char in allCharsInInputData:
        tempDataStr = dataString.replace(char.lower(), "").replace(char.upper(), "")
        currentLength = task01(tempDataStr, "length")

        if (minLength == -1 or currentLength < minLength):
            minLength = currentLength
       
    result = minLength
    return (result)
    

print ("Result of taks 01 is : " + str(task01(inputDataString, "length")))
print ("Result of taks 02 is : " + str(task02(inputDataString)))