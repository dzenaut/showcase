# Problem 9.12
# Solution by Razvan Panea
# Date: 17.05.2013

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

item1 = StorageItem("Book", 1)
s.store(item1)

item2 = StorageItem("Lamp", 1)
s.store(item2)

item3 = StorageItem("Couch", 3)
s.store(item3)

item4 = StorageItem("Table", 2)
s.store(item4)

item5 = StorageItem("Laptop", 20)
s.store(item5)

s.printItems()

if s.isFull():
    print("The storage is full!")
else:
    print("The storage is not full!")
