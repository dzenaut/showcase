class Number():
    def __init__(self, numstring, base):
        '''Makes an instance of the class Number, needs a number as an input an its associated base.'''
        #assigns key characteristics to attributes of the created instance. String and Int of numstring are needed, so that it is still possible to iterate over the digits of the Int (in form of a string)
        self.numstring = str(numstring)
        self.base = int(base)

        #makes a list of digits and replaces letters from hexadecimal by numbers
        self.digits = []
        for a in self.numstring:
            if a == 'A':
                a = 10
            elif a == 'B':
                a = 11
            elif a == 'C':
                a = 12
            elif a == 'D':
                a = 13
            elif a == 'E':
                a = 14
            elif a == 'F':
                a = 15
            else:
                pass
            self.digits.append(a)

        #makes a list with reversed order of the digits
        self.revdigits = self.reverseDigits()
        #assigns the decimal value to the attribute decimal
        self.decimal = self.convertToDec()

    #be able to extract key features of numbers without taking apart the interior of the object
    def getDecimal(self):
        return self.decimal

    def getNum(self):
        return self.numstring

    def getBase(self):
        return self.base

    def makeIntList(self):
        '''Converts the digits in the list of digits form strings into'''
        for a in range(len(self.digits)):
            self.digits[a] = int(self.digits[a])

    def reverseDigits(self):
        '''Enters digits in reverse order to reverse list'''
        self.revdigits = self.digits [::-1]

    def convertToDec(self):
        '''Convert the number to the respective decimal number'''
        #if the base is 10, the number is already in decimal
        if self.base == 10:
            return int(self.numstring)

        #list now has ints as components
        self.makeIntList()
        #update revdigits
        self.reverseDigits()

        #initialize variable for the result (decimal value)
        decimal = 0

        #calculate decimal
        for i in range(len(self.revdigits)):
            decimal += self.revdigits[i] * self.base**i

        return decimal

    def __str__(self):
        return 'Base: ' + str(self.base) + '\nValue: ' + self.numstring

def getNums(txtfile):
    '''makes a tuple of list of strings from a text file with numbers and their base.'''

    #open textfile as file and close it after code block below with statement
    with open(txtfile) as file:

        #.read() gets a string from the file. \n is deleted. split() creates a list from the string without \n
        numlist = file.read().replace('\n', '').split(', ')

    return numlist

#dictBaseNum and numInstances could be combined
def dictBaseNum(numlist, base):

    instances = []
    for i in range(len(numlist)):
        item = {}
        item[base] = numlist[i]
        instances.append(item)

    return instances

def numInstances(listdict):
    instancelist = []
    for dict in listdict:
        for key in dict:
            instancelist.append(Number(dict[key], key))
    return instancelist



ex1 = (dictBaseNum(getNums('num16.txt'), 16))
instance1 = numInstances(ex1)

for instance in instance1:
    decimal = instance.getDecimal()
    print(decimal)





