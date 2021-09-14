# --------------------------------------
# Sequence abstraction
# --------------------------------------
t = (1,2,3,4)
'''
for _ in t:
    print(_)
len(t)
t[0]
'''
# --------------------------------------
s = "abcd"
'''
for _ in s:
    print(_)
len(s)
s[0]
'''
# --------------------------------------
#Recursive Implementation
# --------------------------------------
empty_rlist = None

def make_rlist(first, rest):
    """Make a recursive list from its first element and the rest"""
    return (first, rest)
# --------------------------------------
def first(s):
    """Return the first element of a recursive list s"""
    return s[0]
# --------------------------------------
def rest(s):
    """Return the rest of the elements of a recursive list s"""
    return s[1]

# --------------------------------------
# Manipulation of lists
# --------------------------------------
counts = make_rlist(1, make_rlist(2, make_rlist(3, make_rlist(4, empty_rlist))))
#first(counts)  #1
#rest(counts)   #(2, (3, (4, None)))

# --------------------------------------
def len_rlist(s):
    """Return the length of recursive list s."""
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length

# --------------------------------------
def getitem_rlist(s, i):
    """Return the element at index i of recursive list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

# --------------------------------------
# Manipulating a recursive list as a sequence
# --------------------------------------
#len_rlist(counts)          #4
#getitem_rlist(counts, 1)   #2

# --------------------------------------
# Tuples
# --------------------------------------
digits = (1, 8, 2, 8)
#len(digits)    #4
#digits[3]      #8

#(2, 7) + digits * 2
#(2, 7, 1, 8, 2, 8, 1, 8, 2, 8)

# --------------------------------------
# Mapping
# --------------------------------------
alternates = (-1, 2, -3, 4, -5)
#map(abs, alternates)
#<map object at 0x039B79F0>
#tuple(map(abs, alternates))
#(1, 2, 3, 4, 5)

# --------------------------------------
# Sequence Iteration with while
# --------------------------------------
def count(s, value):
    """Count the number of occurrences of value in sequence s."""
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total

#count(digits, 8)   #2

# --------------------------------------
# Sequence Iteration without index variable
# --------------------------------------
def count2(s, value):
    """Count the number of occurrences of value in sequence s."""
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total

#count2(digits, 8)   #2

# --------------------------------------
# Sequence unpacking
# --------------------------------------
'''
pairs = ((1, 2), (2, 2), (2, 3), (4, 4))
same_count = 0
for x, y in pairs:
    if x == y:
        same_count = same_count + 1
same_count  #2
'''

# --------------------------------------
# Ranges are sequences too!
# --------------------------------------
'''
range(1, 10) # Includes 1, but not 10
#range(1, 10)

tuple(range(5, 8))
#(5, 6, 7)

tuple(range(4))
#(0, 1, 2, 3)

len(range(20))
#20

(range(20))[6]
#6
'''
'''
total = 0
for k in range(5, 8):
    total = total + k
total   #18
'''

# --------------------------------------
# Membership
# --------------------------------------
'''
digits
#(1, 8, 2, 8)
2 in digits
#True
1828 not in digits
#True
digits.index(8)
#1
digits.index(0)
#ValueError
digits.count(8)
#2
digits.count(0)
#0
'''

# --------------------------------------
# Slicing
# --------------------------------------
'''
digits[0:2]
#(1, 8)
digits[1:]
#(8, 2, 8)
digits[1:]
#(8, 2, 8)
digits[0::2]
#(1, 2)
digits[::-1]
#(8, 2, 8, 1)
'''

# --------------------------------------
# Strings
# --------------------------------------
'''
>>> 'I am string!'
'I am string!' 
>>> "I’ve got an apostrophe"
'I’ve got an apostrophe' 
>>> '??'
'??'
'''
# --------------------------------------
# strings are sequences
# --------------------------------------
'''
>>> city = ‘Beer Sheva’
>>> len(city)
10
>>> city[3]
‘r’
'''
# --------------------------------------
# addition and multiplication
# --------------------------------------
'''
>>> "Beer Sheva" + " and "+ "Ashdod"
'Beer Sheva and Ashdod‘
>>> 'Bye ' * 2
'Bye Bye ‘
'''
# --------------------------------------
# Membership in strings
# --------------------------------------
'''
>>> ’here’ in "Where’s Waldo?"
True

>>> ’Mississippi’.count(’i’)
4
>>> ’Mississippi’.count(’issi’)
1
'''
# --------------------------------------
# Multiline Literals
# --------------------------------------
'''
"""The Zen of Python
claims, Readability counts.
Read more: import this."""
'The Zen of Python\nclaims, Readability counts.\nRead more: import this.'
'''
# --------------------------------------
# String Coercion
# --------------------------------------
'''
>>> str(2) + ’ is an element of ’ + str(digits)
’2 is an element of (1, 8, 2, 8)’
'''
# --------------------------------------
# String methods
# --------------------------------------
'''
>>> ’1234’.isnumeric()
True

>>> ’rOBERT dE nIRO’.swapcase()
’Robert De Niro’

>>> ’snakeyes’.upper().endswith(’YES’)
True
'''

# --------------------------------------
# Conventional Interfaces
# --------------------------------------

# --------------------------------------
# enumerate
# --------------------------------------
'''
range(1, 10) – iterable object containing 
(1, 2, 3, 4, 5, 6, 7, 8, 9)

>>> tuple(range(1, 10))
(1, 2, 3, 4, 5, 6, 7, 8, 9)

>>> sum(range(1, 10))
45

>>> r =  enumerate([1,2,3])

>>> r
<enumerate object at 0x00000205DB3091F8>

>>> tuple(r)
((0, 1), (1, 2), (2, 3))

>>> for i in r:
		print(i)
(0, 1)
(1, 2)
(2, 3)
'''
# --------------------------------------
# fib as a mapped function
# --------------------------------------
def fib(k):
    """Compute the kth Fibonacci number."""
    prev, curr = 1, 0 # curr is the first Fibonacci number.
    for _ in range(k - 1):
        prev, curr = curr, prev + curr
    return curr

# --------------------------------------
# mapping
# --------------------------------------
'''
>>> nums = (5, 6, -7, -8, 9)

>>> map(abs, nums) – iterable object containing   (5, 6, 7, 8, 9)

>>> tuple(map(fib, (1, 2, 3, 4)))
(0, 1, 1, 2)

>>> sum(map(fib, (1, 2, 3, 4)))
4
'''
# --------------------------------------
# filtering with iseven
# --------------------------------------
def iseven(n):
    return n % 2 == 0

# --------------------------------------
# filter
# --------------------------------------
'''
>>> nums = (5, 6, -7, -8, 9)

>>> tuple(filter(iseven, nums))
(6, -8)

>>> tuple(filter(lambda x: x % 2 == 0, nums))
(6, -8)

>>> sum(filter(lambda x: x % 2 == 0, nums))
-2
'''
# --------------------------------------
# Solution
# --------------------------------------
def sum_even_fibs(n):
    """Sum the first n even Fibonacci numbers."""
    return sum(filter(iseven, map(fib, range(1, n+1))))
#sum_even_fibs(20)      #3382


# --------------------------------------
# Words enumeration via split
# --------------------------------------
'''
tuple(’Spaces between words’.split())
(’Spaces’, ’between’, ’words’)
'''

# --------------------------------------
# map - retrieve first letters
# --------------------------------------
def first(s):
    return s[0]

'''
>>> tuple(map(first, ("Tel", "Aviv")))
('T', 'A')

>>> tuple(map(lambda x: x[0], "Tel Aviv".split()))
('T', 'A')
'''

# --------------------------------------
# filter - retrieve capitalized words
# --------------------------------------
def iscap(s):
    return len(s) > 0 and s[0].isupper()
#tuple(filter(iscap, "city of Tel Aviv".split()))  #('Tel', 'Aviv')

# --------------------------------------
# Solution
# --------------------------------------
def acronym(name):
    """Return a tuple of the letters that form the 	acronym for name."""
    return tuple(map(first, filter(iscap, name.split())))

#acronym('Shamoon College of Engineering')      #(’S’, ’C’, ’E’)


# --------------------------------------
# Generator expressions
# --------------------------------------
def acronym2(name):
    return tuple(w[0] for w in name.split() if iscap(w))
def sum_even_fibs2(n):
    return sum(fib(k) for k in range(1, n+1) if fib(k) % 2 == 0)

# --------------------------------------
# Reduce
# --------------------------------------

from operator import mul,add
from functools import reduce
#reduce(mul, (1, 2, 3, 4, 5))  #120

def product_even_fibs(n):
    """Return the product of the first n even
    Fibonacci numbers, except 0."""
    return reduce(mul, filter(iseven, map(fib,range(2, n+1))))

#product_even_fibs(20)   #123476336640

def abbreviation(expr):
    return reduce(add, map(first, filter(iscap, expr.split())))  
def abbreviation2(expr):
    return "".join(map(first, filter(iscap, expr.split())))

