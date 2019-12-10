# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 22:57:07 2018

@author: Blaž
"""
import sys
sys.setrecursionlimit(10**4)


dataArray = []

''' Reading File
'''
inputFile = open ("Input Txts/Day08.txt", "r")

dataArray = inputFile.read().split(" ")

inputFile.close()

class ChildInfo:
    def __init__(self, _childCount, _metaDataCount, _depth, pos):
        self.childCount = _childCount
        self.metaDataCount = _metaDataCount
        self.depth = _depth
        self.pos = pos


class Node:
    def __init__ (self, _childCount, _metaDataCount, _position, _parent):
        self.position = _position
        self.childCount = _childCount
        self.metaDataCount = _metaDataCount
        self.parent = _parent
        self.children = []
        self.metaData = []
        self.value = None
        self.metaDataPos = None
        self.spaceOcupied = 0

    def calculateNodeValue (self, node):
        for child in node.children:
            if (child.value == None):
                node.calculateNodeValue(child)
                return
        value = 0
        for data in node.metaData:
            if (node.childCount > 0):
                if (data == 0 or data > node.childCount):
                    continue
                else:
                    value += node.children[data - 1].value
            else:
                value = sum(node.metaData)
        node.value = value
        if (node.parent != None):
            node.calculateNodeValue(node.parent)
        else:
            return 
        
    def getMetaData (self, node):
        startPos = node.metaDataPos
        stopPos = node.metaDataPos + node.metaDataCount
        for i in range (startPos, stopPos):
            node.metaData.append(int(dataArray[i]))
                
        for child in node.children:
            node.getMetaData(child)

    def getMetaDataPosition (self, node):
        if (node.metaDataPos == None and node.childCount == 0):
            node.metaDataPos = node.position + 2
            node.spaceOcupied = 2 + node.metaDataCount
            node.getMetaDataPosition(node.parent)
        elif (node.metaDataPos == None and node.childCount > 0):
            addToPos = 0
            for child in node.children:
                if (child.metaDataPos == None):
                    node.getMetaDataPosition(child)
                    return
                else:
                    addToPos += child.spaceOcupied
            node.metaDataPos = node.position + addToPos + 2
            node.spaceOcupied = addToPos + node.metaDataCount + 2
            if (node.parent != None):
                node.getMetaDataPosition(node.parent)
            
i = 0
depth = 0
apendex = []
childsArray = []
metadata = []

while i < len(dataArray) -1:
    a = int(dataArray[i])
    b = int(dataArray [i+1])
    
    depth += 1
    c = ChildInfo(a, b, depth, i)
    apendex.append(c)
    childsArray.append(c)
    if (a == 0):
        target = i + 2 + b
        i += 2
        while (i < target):
            metadata.append(int(dataArray[i]))
            i += 1
        depth -=1
        apendex.remove(apendex[len(apendex) - 1])
        
        while True:
            if (len(apendex) < 1):
                break
            
            d = apendex[len(apendex) -1]
            d.childCount -= 1
            if (d.childCount < 1):
                t = i + d.metaDataCount
                while (i < t):
                    metadata.append(int(dataArray[i]))
                    i += 1
                apendex.remove(d)
                if (len(apendex) < 1):
                    break
                d = apendex[len(apendex) -1]
                    
            else:
                break
    else:
        i += 2
        
maxDepth = 0
for child in childsArray:
    if (child.depth > maxDepth):
        maxDepth = child.depth

tree = None

def createTree (node, j):
    if (node.childCount > len(node.children)):
        p = node
        j += 1
        arrayPos = childsArray[j].pos
        chCount = int(dataArray[arrayPos])
        mDataCount = int(dataArray[arrayPos + 1])
        ch = Node(chCount, mDataCount, arrayPos, p)
        node.children.append(ch)
        createTree(ch, j)
    else:
        n = node.parent
        if (n == None):
            global tree
            tree = node
            return node     # NE DELA!!!
        createTree(n, j)


n = Node(int(dataArray[0]), int(dataArray[1]), 0, None)

createTree(n, 0)
       

tree.getMetaDataPosition(tree)
tree.getMetaData(tree)
tree.calculateNodeValue(tree)




print ("Result of taks 01 is : " + str(sum(metadata)))
print ("Result of taks 02 is : " + str(tree.value))




