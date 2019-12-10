# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 23:18:53 2018

@author: Blaž
"""

puzzleInput = "607331"


''' Task 01
'''
def task01(pInput):
    puzzInput = int(pInput)
    results = [3,7]
    elfPos1 = 0
    elfPos2 = 1
    elfValue1 = results[0]
    elfValue2 = results[1]
    
    while (len(results) < puzzInput + 10):
        elfValueSum = elfValue1 + elfValue2
        sumStr = str(elfValueSum)
        for num in sumStr:
            results.append(int(num))
            
        
        elfPos1 += elfValue1 + 1
        while elfPos1 > len(results) - 1:
            elfPos1 -= len(results)
        elfValue1 = results[elfPos1]
        
        elfPos2 += elfValue2 + 1
        while (elfPos2 > len(results) - 1):
            elfPos2 -= len(results)
        elfValue2 = results[elfPos2]
        
#        print(f"p1 {elfPos1} ; v1 {elfValue1}; p2 {elfPos2} ; v2 {elfValue2}")
    
    lastNums = results[puzzInput:puzzInput+10]
    resultValue = ""
    for number in lastNums:
        resultValue += str(number)
    return resultValue


def task02(pInput):
    print("\nStarting task 2; This may take a few minutes!")
    results = [3,7]
    elfPos1 = 0
    elfPos2 = 1
    elfValue1 = results[0]
    elfValue2 = results[1]
    
    matchingValue = []
    for numm in pInput:
        matchingValue.append(int(numm))
    
    matchFound = False
    failSavePoint = 10**8
    irCount = 0
    result = None
    while not matchFound:
        elfValueSum = elfValue1 + elfValue2
        sumStr = str(elfValueSum)
        for num in sumStr:
            results.append(int(num))
            
        
        elfPos1 += elfValue1 + 1
        while elfPos1 > len(results) - 1:
            elfPos1 -= len(results)
        elfValue1 = results[elfPos1]
        
        elfPos2 += elfValue2 + 1
        while (elfPos2 > len(results) - 1):
            elfPos2 -= len(results)
        elfValue2 = results[elfPos2]
        
        # včasih doda 2 številki v array, 
        # zato je treba pregledovat tudi za eno mesto nazaj
        arrPart1 = []
        arrPart2 = []
        
        startPos = -1 * len(matchingValue) 
        arrPart1 = results[startPos :]
        
        startPos -= 1
        stopPos = -1
        arrPart2 = results[startPos : stopPos]
        
        
        if arrPart1 == matchingValue:
            result = len(results) - len(matchingValue)
            break
        elif arrPart2 == matchingValue:
            result = len(results) - len(matchingValue) - 1
            break
            
        if irCount >= failSavePoint:
            print(f"Iritation limit reached at: {irCount}")
            break
        irCount += 1
        if irCount % 1000000 == 0:
            print(f"Iritation counter: {irCount//1000000}*10^6")
        
    return result
    
    

print (f"\nResult of taks 01 is: {task01(puzzleInput)}")
print (f"\nResult of taks 02 is: {task02(puzzleInput)}\n")