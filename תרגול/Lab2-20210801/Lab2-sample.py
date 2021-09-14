# ---------------------------------------------
# Sample 1 - math using
'''
import math
print(math.sqrt(25))
'''
# ---------------------------------------------
# Sample 2 - function math using
'''
from math import sqrt
print(sqrt(25))
'''
# ---------------------------------------------
# Sample 3 - Math+String format
'''
import math
n=4
print('sqrt of {0:^10d}  = {1:.2f}'.format(n,math.sqrt(n)))
print('sqrt of',n,'=',math.sqrt(n))
'''
# ---------------------------------------------
# Sample 4 - String format
'''
a,b,c=4,23.4567,'adersgdrg'
print('First: {0:^10d}, Second: {1:>10.2f}, Next: {2:30s} END'.format(a,b,c))
'''
# ---------------------------------------------
# Sample 5 - Function Sample

# First...
# Second...
# 1
# 6
'''
def f2():
    return 1

def f3(a,b):
    return a+b

print('First...')

def f1():
    print('Second...')

f1()
print(f2())
print(f3(2,4))
'''
# ---------------------------------------------
# Sample 5 - Function sample
'''
def f1(x,y):
    return x+y
#print(f1(2,3.3))
#print(f1(2,f1(5,7)))
#print(f1(float(input('Enter num1: ')),float(input('Enter num2: '))))
#print(f1(4,f1(float(input('Enter num1: ')),float(input('Enter num2: ')))))
'''
# ---------------------------------------------
# Sample 6 - Function sample from Presentetion
'''
def power2(x):
    return x*x
def func1(x):
    return power2(x)*3

print(func1(5))
#print(power2(3))
'''
# ---------------------------------------------
# Sample 7 - Function sample from Presentetion
'''
def func1(x):
    def power2(x):
        return x*x
    return power2(x)*3
print(func1(5))
#print(power2(3))
'''
# ---------------------------------------------
# Sample 8 - Function sample 
'''
def f2():
    print('start f2')
    f3()
    print('end f2')

def f3():
    print('start f3')
    print('end f3')

def f1():
    print('start f1')
    f2()
    print('end f1')
f1()
f2()
'''
# ---------------------------------------------
# Sample 9 - Function sample 
'''
def f1():
    print('start f1')
    def f2():
        print('start f2')
        def f3():
            print('start f3')
            print('end f3')
        f3()
        print('end f2')
    f2()
    print('end f1')
f1()
#f2()
'''
# ---------------------------------------------
