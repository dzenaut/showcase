class StorageItem():
    def __init__(self,name,size):
        '''name is a string, size is an integer'''
        self.name = name
        self.size = size

    def getName(self):
        return self.name

    def getSize(self):
        return self.size
'''
store = StorageItem("Dennis", 100)
print(store.getName())
print(store.getSize())
'''
