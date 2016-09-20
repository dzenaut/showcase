# Problem 9.10
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

item = StorageItem("Book", 20)
print("The name of the item is: " + item.getName())
print("The size of the item is: " + str(item.getSize()))
