# Problem 9.11
# Solution by Razvan Panea
# Date: 17.05.2013

class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.content = []

    def store(self, s):
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

