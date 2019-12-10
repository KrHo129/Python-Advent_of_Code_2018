# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:36:02 2018

@author: Blaž
"""


dataInitialState = ""
dataSpreadRules = []


class SpreadRule:
    def __init__(self, _rule, _willGrow):
        self.rule = _rule
        self.willGrow = _willGrow


''' Reading File
'''
fileInput = open ("Input Txts/Day12.txt", "r")
#fileInput = open ("Input Txts/test.txt", "r")

for line in fileInput:
    splitedLine = line.split(" ")
    if (splitedLine[0] == "initial"):
        dataInitialState = splitedLine[2].strip()
    elif len(splitedLine) == 3:
        pravilo = splitedLine[0].strip()
        
        boRastlina = None
        if (splitedLine[2].strip() == "#"):
            boRastlina = True
        elif (splitedLine[2].strip() == "."):
            boRastlina = False
        newRule = SpreadRule(pravilo, boRastlina)
        dataSpreadRules.append(newRule)
        
fileInput.close

def task01(initialState, rules, generationRepeatCount):
    oldResult = 0
    diferenceInResults = 0
    willGrowRulesArray = []
    wontGrowRulesArray = []
    
    for singleRule in rules:
        if singleRule.willGrow:
            willGrowRulesArray.append (singleRule.rule)
        else:
            wontGrowRulesArray.append(singleRule.rule)
    
    currentState = initialState
    
    currentState = "...." + currentState + "...."
    minusPositonAdded = 4
    breakPointCount = 0
    for i in range (repeatCount):
        newState = ".."
        for position in range (2, len(currentState) - 2):
            stringSection = currentState[position - 2 : position + 3]
            if (stringSection in willGrowRulesArray):
                newState += "#"
            else:
                newState += "."
        newState += ".."
        
        insertionNeeded = False
        for checkPos in range(4):
            if (newState[checkPos] == "#"):
                insertionNeeded = True
                
            if insertionNeeded:
                newState = "." + newState
                minusPositonAdded += 1
        
        for checkPos in range(-1, -5, -1):
            if (newState[checkPos] == "#"):
                newState += "."
        
        currentState = newState
        
        newResult = 0
        for pos in range (len(currentState)):
            if (currentState[pos] == "#"):
                newResult += pos - minusPositonAdded
        
        if (newResult - oldResult == diferenceInResults):
            breakPointCount = i
            break
        else:
            diferenceInResults = newResult - oldResult
            
        oldResult = newResult
        
    
    if (generationRepeatCount != 20):
        addToResult = (generationRepeatCount - breakPointCount - 1) * diferenceInResults
        newResult += addToResult
    
    return (newResult)




repeatCount = 20
print ("Result of taks 01 is : " + str(task01(dataInitialState, dataSpreadRules, repeatCount)))

repeatCount = 50 * 1000 * 1000 * 1000
print ("Result of taks 02 is : " + str(task01(dataInitialState, dataSpreadRules, repeatCount)))




