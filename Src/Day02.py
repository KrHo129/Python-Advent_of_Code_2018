# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 13:04:18 2018

@author: Blaž
"""

inputDataStrArray = []

"""
    Reading input file
"""
inputFile = open ("Input Txts/Day02.txt", "r")

for line in inputFile:
    inputDataStrArray.append (line.strip())

inputFile.close()

"""
    Task 1
"""
hasDuplicate = hasTriplicate = False
numberOfDuplicates = numberOfTriplicates = 0

def CountChars(sourceString, checkChar):
    charCount = 0
    for singleChar in sourceString:
        if (checkChar == singleChar):
            charCount += 1
    return charCount

for sequence in inputDataStrArray:
    tempSequence = sequence
    while (len(tempSequence) > 1):
        checkingChar = tempSequence[0]
        numerOfCheckingCharsInString = CountChars (tempSequence, checkingChar)
        if (numerOfCheckingCharsInString == 2):
            hasDuplicate = True
        elif (numerOfCheckingCharsInString) == 3:
            hasTriplicate = True
        tempSequence = tempSequence.replace(checkingChar, "")
        
    if hasDuplicate:
        numberOfDuplicates += 1
        hasDuplicate = False
        
    if hasTriplicate:
        numberOfTriplicates +=1
        hasTriplicate = False
    
result01 = numberOfDuplicates * numberOfTriplicates
print ("Result of task 01 is: " + str(result01))

"""
    Task 2
"""
result02 = ""
matchFound = False

def CompareStrings(str1, str2):
    missMatchCount = 0
    for x in range (len(str1)):
        if (str1[x] != str2[x]):
            missMatchCount += 1
    if (missMatchCount < 2):
        return True
    else:
        return False

for i in range(len(inputDataStrArray)-1):
    string1 = inputDataStrArray[i]
    for j in range (i+1, len(inputDataStrArray)):
        string2 = inputDataStrArray[j]
        if (CompareStrings(string1, string2)):
            matchStr1 = string1
            matchStr2 = string2
            matchFound = True
            break
    if matchFound:
        break

for i in range (len(matchStr1)):
    if (matchStr1[i] != matchStr2[i]):
        result02 = matchStr1[:i] + matchStr1[i+1:]
        break

print("Result of task 02 is: " + result02)