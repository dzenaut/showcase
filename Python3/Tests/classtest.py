class Number():
    def __init__(self,number):
        self.number=number
    def increase(self,by):
        self.number += by
        return self.number
    def decrease(self,by):
        self.number -= by
        return self.number
