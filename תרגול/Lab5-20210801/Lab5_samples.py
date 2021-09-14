# --------------------- S1 -----------------------
#def f1(x): return x**2
#print('Function f(11)-',f1(11))

# --------------------- S2 -----------------------
#g=lambda x: x**2
#print('Lambda x: x**2(8)-',g(8))

# --------------------- S3 -----------------------
#print('Lambda  x,y,z: (x+z)/y( 4,2,3)-',(lambda  x,y,z: (x+z)/y)( 4,2,3))

# --------------------- S4 -----------------------
#def make_incrementor (n): return lambda x: x + n
#f = make_incrementor(2)
#g = make_incrementor(6)
#print(f(42), g(42))

# --------------------- S5 -----------------------
#print(make_incrementor(22)(33)) 
#print(make_incrementor(2)(42),make_incrementor(6)(42))

# --------------------- S6 -----------------------
#print((lambda x,y: x and y)(7%2==1,8>0))
#print((lambda x,y: x%2==1 and y>0)(7,8))
#var=lambda x,y: x%2==1 and y>0
#print(var(7,8))

# --------------------- S7 -----------------------
#print('Lambda+If-',(lambda a,b: a+b if a>b  else a-b)(-10,5))

# ---------------------------------------------
# Sample 10 - List 

myList=[1,2,4,9]
'''
print(myList)
for x in myList:
    print(x,end=', ')
print()
for x in range(4):
    print(myList[x],end=', ')
print()
for x in range(3,-1,-1):
    print(myList[x],end=', ')
print()
'''
# ---------------------------------------------


# --------------------- S8 ----------------------
# Accept other functions as arguments
def summation(low,high,function,next):
    total=0
    while low<=high:
        total+=function(low)
        low=next(low)
    return total

def nextTwo(k):
    return k+2

#print(summation(0,5,lambda x: x**2,lambda x:x+1))
#print(summation(0,5,lambda x: x**2,nextTwo))

# --------------------- S9 ----------------------
# Return functions as values
def make_adder(n):
    """return a function that takes argument  k
    and returns  k+n"""
    def adder(k):
        return k+n
    return adder
three=make_adder(3)
#print(three(4)) #=>7 

# --------------------- S10 ----------------------
# Return functions as values
def power1(n):
    def calculate(x):
        return x**n
    return calculate
def power2(n):
    return lambda x:x**n
f=power1(3)
#print(f(2), f(3), f(4))
#print(power1(3)(5))
f=power2(3)
#print(f(2), f(3), f(4))
#print(power2(3)(5))

