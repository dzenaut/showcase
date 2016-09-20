class A:
    def f(self, x):
        print(x)

class B(A):
    def f(self,x):
        print(x+1)
    def g(self, x):
        print(x)

a = A()
b = B()
a.f(1)
b.f(1)
b.g(1)

#Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class
super(B,b).f(1)

'''
1
2
1
1
'''
