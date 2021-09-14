# ------------------------------------------------
class A(object):
    def __init__(self,n=0):
        self.num = n
    def printA(self):
        print(self.num)
    def printC(self):
        print('A.printC()')
        

# ------------------------------------------------
class B(A):
    def __init__(self,n=0,m=0):
        A.__init__(self,n)
        self.mum = m
    
    def printA(self):
        print('B.printA()')

    def printB(self):
        print(self.mum,end=' ')
        A.printA(self)
        self.printA()
                
# ------------------------------------------------
class C(A):
    mum = 3    
    def printA(self):
        print('C.printA()')

    def printB(self):
        print(self.mum,end=' ')
        A.printA(self)
        self.printA()

# ------------------------------------------------
#b=B(3,4)
#b.num          # => 3
#b.mum          # => 4
#b.printB()     # => 4 3 \n B.printA()
#b.printA()     # => B.printA()
#A.printA(b)    # => 3
#b.printC()     # => A.printC()
#c=C(7)
#c.num          # => 7
#c.mum          # => 3
#c.printB()     # => 3 7 \n C.printA()
#c.printA()     # => C.printA()
#A.printA(c)    # => 7
#c.printC()     # => A.printC()
