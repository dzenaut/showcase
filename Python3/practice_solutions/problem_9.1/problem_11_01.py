# Problem 11.1
# Solution by Razvan Panea
# Date: 17.05.2013

import random

class NotEnoughCapacity(Exception):

    def __str__(self):
        return "The storage is full! There is not enough space to store the provided item!"            

class StorageItem:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []

    def store(self, s):
        totalSize = 0
        for item in self.content:
            totalSize += item.getSize()
        if totalSize + s.getSize() > self.capacity:
            raise NotEnoughCapacity()
        else:
            self.content.append(s)  

    def printItems(self):
        for i in range(len(self.content)):
            print("Item " + str(i+1) + ":")
            print("  Name: " + self.content[i].getName())
            print("  Size: " + str(self.content[i].getSize()))
            print("")

    def isFull(self):
        totalSize = 0
        for item in self.content:
            totalSize += item.getSize()
        if totalSize >= self.capacity:
            return True
        else:
            return False

s = Storage(10)

while True:
    size = random.randint(0, 5)
    item = StorageItem("Item", size)
    try:
        s.store(item)
        print("Item of size " + str(size) + " was added!")
    except NotEnoughCapacity:
        print("There is not enough space! Items cannot be added anymore!")
        break
