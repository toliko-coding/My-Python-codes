# --------------------------------------
# repr for build-in objects 
# --------------------------------------
'''
>>> x=5
>>> repr(x)
'5'
>>> eval(repr(x)) == x
True
>>> x=(1,2,3)
>>> y=repr(x)
>>> y
'(1, 2, 3)'
>>> type(x)
<class 'tuple'>
>>> type(y)
<class 'str'>
>>> eval(y)
(1, 2, 3)
>>> type(eval(y))
<class 'tuple'>
>>> eval(y)==x
True
>>> 12e12
12000000000000.0
>>> print(repr(12e12))

12000000000000.0
>>> repr(min)
'<built-in function min>'
>>> min
<built-in function min>

>>> "aaa"
'aaa'
>>> print(repr("aaa"))
'aaa'
>>> repr("aaa")
"'aaa'"
>>> aa=eval(repr("aaa"))
>>> aa
'aaa'
'''
# --------------------------------------
# for user-defined classes 
# --------------------------------------
'''
>>> class Account():
	def __init__(self):
		self.balance = 0
	def __repr__(self):
		return 'Account()'
>>> a = Account()
>>> repr(a)
'Account()'
>>> b=eval(repr(a))
>>> b
Account()
>>> b.balance
0
>>> a.__dict__
{'balance': 0}
>>> b.__dict__
{'balance': 0}

>>> id(a)
61636432
>>> id(b)
61635088
>>>
'''
# --------------------------------------
# str vs. repr 
# --------------------------------------
'''
>>> from datetime import date
>>> today = date(2011, 9, 12)
>>> repr(today)
'datetime.date(2011, 9, 12)'
>>> str(today)
'2011-09-12'
>>> 
'''
# --------------------------------------
# for Account object 
# --------------------------------------
'''
>>> a = Account()>>> class Account():
	def __init__(self):
	    self.balance = 0
	def __str__(self):
	    return 'bank account with balance = '+str(self.balance)
>>> a = Account()
>>> str(a)
'bank account with balance = 0'
>>> print(a)
bank account with balance = 0
>>> str(a)
'bank account with balance = 0'
>>> print(a)
bank account with balance = 0
'''
# --------------------------------------
# for Account object 
# --------------------------------------
'''
>>> class Account():
	def __init__(self):
	    self.balance = 0
	def __str__(self):
	    return 'bank account with balance = '+str(self.balance)
>>> a = Account()
>>> str(a)
'bank account with balance = 0'
>>> print(a)
bank account with balance = 0
'''

# --------------------------------------
# str or repr 
# --------------------------------------
'''
>>> class Account():
	def __init__(self):
	    self.balance = 0
	def __repr__(self):
	    return 'Account()'
	def __str__(self):
	    return 'bank account with balance = '+str(self.balance)
>>> a = Account()
>>> a
Account()
>>> print(a)
bank account with balance = 0
'''
'''
>>> class Account():
	def __init__(self):
	    self.balance = 0
	def __str__(self):
	    return 'bank account with balance = '+str(self.balance)
>>> a = Account()
>>> a
<__main__.Account object at 0x03AC7FB0>
>>> print(a)
bank account with balance = 0
>>>
'''
'''
>>> class Account():
	def __init__(self):
	    self.balance = 0
	def __repr__(self):
	    return 'Account()'
>>> a = Account()
>>> a
Account()
>>> print(a)
Account()
'''
'''
>>> class Account():
	def __init__(self):
	    self.balance = 0
>>> a = Account()
>>> a
<__main__.Account object at 0x03AC7A10>
>>> print(a)
<__main__.Account object at 0x03AC7A10>
'''
# --------------------------------------
# Polymorphic functions 
# --------------------------------------
'''
>>> today.__repr__()
'datetime.date(2011, 9, 12)'
>>> today.__str__()
'2011-09-12'
'''
# --------------------------------------
# Complex Numbers 
# --------------------------------------
def add_complex(z1, z2):
    return ComplexRI(z1.real+z2.real, z1.imag+z2.imag)

def mul_complex(z1, z2):
    return ComplexMA(z1.magnitude*z2.magnitude,z1.angle+z2.angle)

from math import atan2
class ComplexRI(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    def __repr__(self):
        return 'ComplexRI({0}, {1})'.format(self.real, self.imag)

from math import sin, cos
class ComplexMA(object):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.magnitude, self.angle)
'''
>>> from math import pi
>>> add_complex(ComplexRI(1, 2), ComplexMA(2, pi/2))
ComplexRI(1.0000000000000002, 4.0)
>>> mul_complex(ComplexRI(0, 1), ComplexRI(0, 1))
ComplexMA(1.0, 3.141592653589793)
'''
ComplexRI.__add__ = lambda self, other: add_complex(self,other)
ComplexMA.__add__ = lambda self, other: add_complex(self,other)
ComplexRI.__mul__ = lambda self, other: mul_complex(self,other)
ComplexMA.__mul__ = lambda self, other: mul_complex(self,other)
'''
>>> ComplexRI(1, 2) + ComplexMA(2, 0)
ComplexRI(3.0, 2.0)
>>> ComplexRI(0, 1) * ComplexRI(0, 1)
ComplexMA(1.0, 3.141592653589793)
'''
# --------------------------------------
# Generic Functions 
# --------------------------------------
from fractions import gcd
class Rational(object):
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g
    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)
def add_rational(x, y):
    nx, dx = x.numer, x.denom
    ny, dy = y.numer, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    return Rational(x.numer * y.numer, x.denom*y.denom)

def iscomplex(z):
    return type(z) in (ComplexRI, ComplexMA)
def isrational(z):
    return type(z) == Rational

def add_complex_and_rational(z, r):
    return ComplexRI(z.real + r.numer/r.denom, z.imag)

def add(z1, z2):
    """Add z1 and z2, which may be complex or rational."""
    if iscomplex(z1) and iscomplex(z2):
        return add_complex(z1, z2)
    elif iscomplex(z1) and isrational(z2):
        return add_complex_and_rational(z1, z2)
    elif isrational(z1) and iscomplex(z2):
        return add_complex_and_rational(z2, z1)
    else:
        return add_rational(z1, z2)

def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {ComplexRI: 'com',ComplexMA: 'com', Rational: 'rat'}
def add(z1, z2):
    types = (type_tag(z1), type_tag(z2))
    return add.implementations[types](z1, z2)

add.implementations = {}
add.implementations[('com', 'com')] = add_complex
add.implementations[('com', 'rat')] = add_complex_and_rational
add.implementations[('rat', 'com')] = lambda x, y: add_complex_and_rational(y, x)
add.implementations[('rat', 'rat')] = add_rational
'''
>>> add(ComplexRI(1.5, 0), Rational(3, 2))
ComplexRI(3.0, 0)
>>> add(Rational(5, 3), Rational(1, 2))
Rational(13, 6)
'''
# --------------------------------------
# Data-directed programming
# --------------------------------------
def apply(operator_name, x, y):
    tags = (type_tag(x), type_tag(y))
    key = (operator_name, tags)
    return apply.implementations[key](x, y)
def mul_complex_and_rational(z, r):
    return ComplexMA(z.magnitude * r.numer / r.denom, z.angle)
mul_rational_and_complex = lambda r, z: mul_complex_and_rational(z, r)
apply.implementations = {('mul', ('com', 'com')): mul_complex,
			('mul', ('com', 'rat')): mul_complex_and_rational,
			('mul', ('rat', 'com')): mul_rational_and_complex,
			('mul', ('rat', 'rat')): mul_rational}
adders = add.implementations.items()
apply.implementations.update({('add', tags):fn for (tags, fn) in adders})

'''
>>> apply('add', ComplexRI(1.5, 0), Rational(3, 2))
ComplexRI(3.0, 0)
>>> apply('mul', Rational(1, 2), ComplexMA(10, 1))
ComplexMA(5.0, 1)
'''
# --------------------------------------
# Coercion
# --------------------------------------
def rational_to_complex(x):
    return ComplexRI(x.numer/x.denom, 0)
coercions = {('rat', 'com'): rational_to_complex}

def coerce_apply(operator_name, x, y):
    tx, ty = type_tag(x), type_tag(y)
    if tx != ty:
        if (tx, ty) in coercions:
            tx, x = ty, coercions[(tx, ty)](x)
        elif (ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
        else:
            return 'No coercion possible.'
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)

coerce_apply.implementations = {('mul', 'com'):mul_complex,
				('mul', 'rat'): mul_rational,
				('add', 'com'): add_complex,
				('add', 'rat'): add_rational }
'''
>>> coerce_apply('add', ComplexRI(1.5, 0), Rational(3, 2))
ComplexRI(3.0, 0)
>>> coerce_apply('mul', Rational(1, 2), ComplexMA(10, 1))
ComplexMA(5.0, 1.0)
'''
