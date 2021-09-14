# ------------------------------------------------
'''
def f1(x):
    return x+y
def f2(y):
    return f1(3)+1
print(f2(3))
'''
# ------------------------------------------------
'''
def f2(y):
    def f1(x):
        return x+y
    return f1(3)+1
print(f2(3))
'''
# ------------------------------------------------
'''
x=100
def f1(y):
    return y+x
def f2(x):
    return x+f1(3)
print(f2(3))
print(f1(3))
'''
# ------------------------------------------------
'''
def f1(x):
    return f2(x,10)
#print(f1(20))  # => NameError: name 'f2' is not defined 
def f2(i,j):
    return i+j
print(f1(20))
'''
# ------------------------------------------------
'''
def f1(x):
    return f2(10)
def f2(y):
    return y+x
print(f1(20))   # => NameError: name 'x' is not defined
'''
# ------------------------------------------------
