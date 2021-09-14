# ------------------------------------------------
#               Class Object
# ------------------------------------------------
'''
from datetime import date
today = date(2013, 11, 9)
str(date(2013, 11, 11) - today) # => '2 days, 0:00:00'
today.month                     # => 11
today.strftime("%y-%m-%d %H:%M")# => '13-11-09 00:00'
'''

# ------------------------------------------------
#               Ordered Sequences - List    
# ------------------------------------------------
'''
s = ['ab', 2, [3, 4]]
s[0]        # =>'ab'
s[0][0]     # => 'a'
s[2][1]     # => 4
s[-1]       # => [3, 4]
s[0][2]='d' # => 'str' object does not support item assignment

s = [7, 8, 9, 10, 11]
s[:]        # => [7, 8, 9, 10, 11]
s[2:]       # => [9, 10, 11]
s[:2]       # => [7, 8]
s[::2]      # => [7, 9, 11]
s[1:4:1]    # => [8, 9, 10]
s[1:4:2]    # => [8, 10]

s+='a'      # => [7, 8, 9, 10, 11, 'a']
s.extend([1, 2])    # => [7, 8, 9, 10, 11, 'a', 1, 2]
s.insert(0, 5)      # => [5, 7, 8, 9, 10, 11, 'a', 1, 2]
del s[2:-2]         # => [5, 7, 1, 2]
s.append(-5)        # => [5, 7, 1, 2, -5]
list('abcd')        # => ['a', 'b', 'c', 'd']
list(range(5))      # => [0, 1, 2, 3, 4]
'''
# ------------------------------------------------
#               Ordered Sequences - Tuple
# ------------------------------------------------
'''
tuple([1, 2, 3])    # => (1, 2, 3)
list((1,2,3))       # => [1, 2, 3]
tuple(range(10))    # => (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
t=(1,2,3,4,5)
t[2]                # => 3
t[:-2]              # => (1, 2, 3)
t[3]=5              # => 'tuple' object does not support item assignment
'''
# ------------------------------------------------
#               Unordered Types - Set
# ------------------------------------------------
'''
s={1,2,3,4,5}
5 in s              # => True
8 in s              # => False
s = set(list(range(10)))
s                   # => {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
s[0]                # => 'set' object does not support indexing
len(s)              # => 10
s.add(4)
len(s)              # => 10
s.pop()             # => 0
s                   # => {1, 2, 3, 4, 5, 6, 7, 8, 9}
s.remove(5)
s                   # => {1, 2, 3, 4, 6, 7, 8, 9}
'''

# ------------------------------------------------
#               Unordered Types - Dictionary
# ------------------------------------------------
'''
s = { 'x' : 2, 'y' : [1,2], (3,4) : 5}
s[(3,4)]            # => 5
s['x'] = s['y']
s                   # => {'y': [1, 2], 'x': [1, 2], (3, 4): 5}
s['x'][0] = 7
s                   # => {'y': [7, 2], 'x': [7, 2], (3, 4): 5}
len(s)              # => 3
'x' in s            # => True
'''

# ------------------------------------------------
#           ADT rlist(tuple) - recursive list
# ------------------------------------------------
'''
empty_rlist = None
# ------------------------------------------------
def make_rlist(first,rest):
# Make a recursive list from its first element and the rest.
    return (first,rest)
# ------------------------------------------------
def first(s):
#Return the first element of a recursive list s.
    return s[0]
# ------------------------------------------------
def rest(s):
#Return the rest of the elements of a recursive list s.
    return s[1]
# ------------------------------------------------
def len_rlist(s):
# Return the length of recursive list s.
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length
       
# ------------------------------------------------
counts=make_rlist(1,make_rlist(2,make_rlist(3,make_rlist(4,None))))
print(len_rlist(counts))
'''

# ------------------------------------------------
#           ADT rlist(dispatch) - recursive list
# ------------------------------------------------
'''
empty_rlist = None
# ------------------------------------------------
def make_rlist(first,rest):
    def dispatch(x):
        if x==0:
            return first
        elif x==1:
            return rest
    return dispatch
# ------------------------------------------------
def getitem_pair(s,i):
    return s(i)
# ------------------------------------------------
def first(s):
    return getitem_pair(s,0)
# ------------------------------------------------
def rest(s):
    return getitem_pair(s,1)
# ------------------------------------------------
def len_rlist(s):
# Return the length of recursive list s.
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length
       
# ------------------------------------------------
counts=make_rlist(1,make_rlist(2,make_rlist(3,make_rlist(4,None))))
print(len_rlist(counts))
'''
