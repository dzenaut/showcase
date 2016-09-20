from p7_10 import StorageItem

class StorageFull(Exception):
    def __str__(self):
        return "The Storage is full."

class Storage():
    def __init__(self,capacity):
        self.capacity = capacity
        self.content = []

    def store(self, s):
        '''s is an instance of StorageItem'''
        self.content.append(s)

    def printItems(self):
        for item in self.content:
            print(item.getName())
            print(item.getSize())

    def isFull(self):
        total = 0
        for item in self.content:
            total += item.getSize()
        if total >= self.capacity:
            return True
        return False

class ProtectedStorage(Storage):
    def store(self,s):
        try:
            self.content.append(s)
            total = 0
            for item in self.content:
                total += item.getSize()
            if total > self.capacity:
                raise StorageFull()
        except StorageFull as e:
            del self.content[-1]
            print(e)
            quit()

s = ProtectedStorage(1)
i1 = StorageItem("Pen", 1)
i2 = StorageItem("Rubber", 2)
s.store(i1)
s.store(i2)


