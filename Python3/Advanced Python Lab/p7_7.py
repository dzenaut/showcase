class A(Exception):
    def __str__(self):
        return "there was a problem"

class B(Exception):
    def __str__(self):
        return "there was a problem"

class Q:
    def __init__(self,p):
        self.p = p
    def f(self, x):
        if x > self.p:
            return x
        else:
            raise A()

def f(q,x,y):
    try:
        print(q.f(x))
    except A:
        try:
            print(q.f(y))
        except A:
            raise B()

q = Q(4)

try:
    f(q,5,6)
except A:
    print("A")
except B:
    print("B")

try:
    f(q,2,3)
except A:
    print("A")
except B:
    print("B")
