# -------------------------------------------------
# S#4-8
# -------------------------------------------------
from datetime import date
'''
>>> today = date(2021, 7, 19)
>>> today
datetime.date(2021, 7, 19)
>>> type(today)
<class 'datetime.date'>
>>> str(date(2020, 7, 19) - today)
'-365 days, 0:00:00'
>>> date(2020, 7, 19) - today
datetime.timedelta(days=-365)
>>> today.year
2021
>>> today.strftime('%A, %B %d')
'Monday, July 19'
>>> type(today)
<class 'datetime.date'>
>>> type(date.strftime)
<class 'method_descriptor'>
>>> type(date)
<class 'type'>
>>> type(type)
<class 'type'>
'''
# -------------------------------------------------
# S#14-15
# -------------------------------------------------
def make_rat(n, d):
    pass
def numer(x):
    pass
def denom(x):
    pass
# -------------------------------------------------
def add_rat(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return make_rat(nx * dy + ny * dx, dx * dy)
def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))
def eq_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)
# -------------------------------------------------

# -------------------------------------------------
# S#15
# -------------------------------------------------
def make_rat(n, d):
    return (n, d)

def numer(x):
    return getitem(x, 0)

def denom(x):
    return getitem(x, 1)
# -------------------------------------------------
# S#17-18
# -------------------------------------------------
'''
>>> (1, 2, 3)
(1, 2, 3)
>>> pair = (1, 2)
>>> pair
(1, 2)
>>> x, y = pair
>>> x
1
>>> y
2
>>> pair[0]
1
>>> from operator import getitem
>>> getitem(pair, 0)
1
>>> pair[1]
2
'''
# -------------------------------------------------
# S#19
# -------------------------------------------------
from operator import getitem
def make_rat(n, d):
    return (n, d)

def numer(x):
    return getitem(x, 0)

def denom(x):
    return getitem(x, 1)

# -------------------------------------------------
# S#20
# -------------------------------------------------
def str_rat(x):
    """Return a string ’n/d’ for numerator n and denominator d."""
    return '{0}/{1}'.format(numer(x), denom(x))

# -------------------------------------------------
# S#21
# -------------------------------------------------
'''
>>> half = make_rat(1, 2)
>>> str_rat(half)
'1/2'
>>> third = make_rat(1, 3)
>>> str_rat(mul_rat(half, third))
'1/6'
>>> str_rat(add_rat(third, third))
'6/9'
'''
# -------------------------------------------------
# S#22
# -------------------------------------------------
from math import gcd
def make_rat(n, d):
    g = gcd(n, d)
    return (n//g, d//g)
'''
>>> half = make_rat(1, 2)
>>> str_rat(half)
'1/2'
>>> third = make_rat(1, 3)
>>> str_rat(mul_rat(half, third))
'1/6'
>>> str_rat(add_rat(third, third))
'2/3'
'''

# -------------------------------------------------
# S#29-31
# -------------------------------------------------
def make_pair(x, y):
    """Return a function that behaves like a pair."""
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
    return dispatch
# -------------------------------------------------
def getitem_pair(p, i):
    """Return the element at index i of pair p."""
    return p(i)
# -------------------------------------------------
'''
>>> p = make_pair(1, 2)
>>> getitem_pair(p, 0)
1
>>> getitem_pair(p, 1)
2
'''
# -------------------------------------------------
from math import gcd
def make_rat(n, d):
    g = gcd(n, d)
    return make_pair(n//g, d//g)

def numer(x):
    return getitem_pair(x, 0)

def denom(x):
    return getitem_pair(x, 1)
# -------------------------------------------------
'''
>>> half = make_rat(1, 2)
>>> half
<function make_pair.<locals>.dispatch at 0x03BEC2B0>
>>> str_rat(half)
'1/2'
>>> third = make_rat(1, 3)
>>> str_rat(mul_rat(half, third))
'1/6'
>>> str_rat(add_rat(third, third))
'2/3'
'''
