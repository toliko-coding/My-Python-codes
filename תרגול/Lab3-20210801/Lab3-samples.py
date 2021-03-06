'''Recursive functions''' 
# ------------------------------------------------
# Sample 1
# ------------------------------------------------
# f1() => Non Stop Recurcive Function

def f1():
    """Non stop function""" 
    print('start f1 !')
    f1()
    print('end f1 !')
#f1()

# ------------------------------------------------
# Sample 2
# ------------------------------------------------
# f2(3) => 
# start f2 !
# start f2 !
# start f2 !
# end f2 !
# end f2 !
# end f2 !

def f2(x):
    '''Recursive functions'''
    if x > 0:
        print('start f2 !')
        f2(x-1)
        print('end f2 !')
#f2(3)
        
# ------------------------------------------------
# Sample 5
# ------------------------------------------------
# f5(7) => 7 6 5 4 3 2 1 1 2 3 4 5 6 7

def f5(x):
    if x > 0:
        print(x, end=' ')
        f5(x-1)
        print(x, end=' ')
#f5(7)
        
# ------------------------------------------------
# Sample 6
# ------------------------------------------------
# f6(7) => 7 6 5 4 3 2 1 2 3 4 5 6 7

def f6(x):
    if x == 1:
        print(x, end=' ')
    else:
        print(x, end=' ')
        f6(x-1)
        print(x, end=' ')
#f6(7)
        
# ------------------------------------------------
# Sample 7
# ------------------------------------------------
# f7(7) => 1 2 3 4 5 6 7 6 5 4 3 2 1

def f7(x,y=1):
    if x == y:
        print(y, end=' ')
    else:
        print(y, end=' ')
        f7(x,y+1)
        print(y, end=' ')
#f7(7)

# ------------------------------------------------
# Sample 8
# ------------------------------------------------
#print(f8(6)) => 720
#print(f8(0)) => 1
#print(f8(11)) => 39916800

def f8(x):
    if x == 0:
        return 1
    return x*f8(x-1)
#print(f8(6))
#print(f8(0))
#print(f8(11))

# ------------------------------------------------
# Sample 9 - If the amount of 1-bit odd number
# ------------------------------------------------
#print(f9(15)) => (1111b)-1 
#print(f9(131)) => (10000011)-0

def f9(x):
    if x == 0:
        return 1
    return (x%2)^f9(x//2)
#print(f9(15))
#print(f9(131))

# ------------------------------------------------
# Computing Exponent
# ------------------------------------------------
#exp(2,3)   => 8
#exp(3,2)   => 9

def exp(x, n):
    """
    Computes the result of x raised to the power of n.
        >>> exp(2,3)
        8
        >>> exp(3,2)
        9
    """
    if n == 0:
        return 1
    return x * exp(x, n-1)
# ------------------------------------------------
'''
exp(2, 4)
+-- 2 * exp(2, 3)
|       +-- 2 * exp(2, 2)
|       |       +-- 2 * exp(2, 1)
|       |       |       +-- 2 * exp(2, 0)
|       |       |       |       +-- 1
|       |       |       +-- 2 * 1
|       |       |       +-- 2
|       |       +-- 2 * 2
|       |       +-- 4
|       +-- 2 * 4
|       +-- 8
+-- 2 * 8
+-- 16
'''
# ------------------------------------------------
# Computing Exponent(fast)
# ------------------------------------------------
#fast_exp(2,10)     => 1024
def fast_exp(x, n):
    if n == 0:
        return 1
    if n%2 == 0:
        return fast_exp(x*x, n//2)
    return x * fast_exp(x, n-1)
# ------------------------------------------------
'''
fast_exp(2, 10)
+-- fast_exp(4, 5) # 4 = 2 * 2
|   +-- 4 * fast_exp(4, 4)
|   |       +-- fast_exp(16, 2) # 16 = 4 * 4
|   |       |   +-- fast_exp(256, 1) # 256 = 16 * 16
|   |       |   |   +-- 256 * fast_exp(256, 0)
|   |       |   |             +-- 1
|   |       |   |   +-- 256 * 1
|   |       |   |   +-- 256
|   |       |   +-- 256
|   |       +-- 256
|   +-- 4 * 256
|   +-- 1024
+-- 1024
1024
'''
