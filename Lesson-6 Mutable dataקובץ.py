# --------------------------------------
# Tuples vs. Lists
# --------------------------------------
'''
>>> x = (1,2)
>>> y = x
>>> y is x
True
>>> y = y + (3,4)
>>> y
(1, 2, 3, 4)
>>> x
(1, 2)
>>> x = (1 ,2)
>>> y = x
>>> y is x
True
>>> y[0] = 0 #TypeError: 'tuple' object does not support item assignment
'''
'''
>>> x = [1,2]
>>> y = x
>>> y is x
True
>>> y = y + [3,4]
>>> y
[1, 2, 3, 4]
>>> x
[1, 2]
>>> x = [1,2]
>>> y = x
>>> y is x
True
>>> y[0] = 0
>>> y
[0, 2]
>>> x
[0, 2]
'''
# --------------------------------------
# Creating account with a balance.
# make_account
# --------------------------------------
'''
def make_account(balance):
    """Return a withdraw function that draws     
    down balance with each call."""
    def withdraw(amount):
        if amount > balance:
            return 'Insufficient funds'
        return balance - amount
    return withdraw
#withdraw = make_account(100)
'''
'''
>>> withdraw = make_account(100)
>>> withdraw(20)
80
>>> withdraw(20)
80
>>> withdraw(20)
80
'''
# --------------------------------------
'''
def make_account(balance):
    """Return a withdraw function that draws down 	balance with each call."""
    def withdraw(amount):
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw
'''
'''
>>> withdraw = make_account(100)
>>> withdraw(20)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    withdraw(20)
  File "D:\BACKUP-DISK-D-19_8_2016\My\SCE\Principles of Programming Languages\2020-summer\Lec\Lec3\Lesson-6.py", line 59, in withdraw
    if amount > balance:
UnboundLocalError: local variable 'balance' referenced before assignment
>>> 
'''
# --------------------------------------
'''
def make_account(balance):
    """Return a withdraw function that draws down 	balance with each call."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw
'''
'''
>>> withdraw = make_account(100)
>>> withdraw(20)
80
>>> withdraw(20)
60
'''
# --------------------------------------
# playing cards
# --------------------------------------
#chinese_suits = ['coin', 'string', 'myriad']
#suits = chinese_suits

#suits.pop() #'myriad'

#suits.remove('string')

#suits.append('cup')

#suits.append('cup')

#suits.extend(['sword', 'club'])

#suits  #['coin', 'cup', 'sword', 'club']

#suits[2] = 'spade'

#suits  #['coin', 'cup', 'spade', 'club']

#suits[0:2] = ['heart', 'diamond']

#suits #['heart', 'diamond', 'spade', 'club']

#suits.reverse()
#suits  #['club', 'spade', 'diamond', 'heart']

#suits.sort()
#suits  #['club', 'diamond', 'heart', 'spade']

# --------------------------------------
# Sharing and Identity
# --------------------------------------
#chinese_suits #['heart', 'diamond', 'spade', 'club']

#nest = list(suits)
#nest[0] = suits
#nest   #[['heart', 'diamond', 'spade', 'club'], 'diamond', 'spade', 'club']

#suits.insert(2, 'Joker')
#nest   #[['heart', 'diamond', 'Joker', 'spade', 'club'], 'diamond', 'spade', 'club']

#nest[0].pop(2)     #'Joker'
#suits              #['heart', 'diamond', 'spade', 'club']

#suits is nest[0]   #True
#suits is ['heart', 'diamond', 'spade', 'club']     #False
#suits == ['heart', 'diamond', 'spade', 'club']     #True

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
# make_mutable_rlist
# --------------------------------------
'''
def make_mutable_rlist():
    """Return a functional implementation of a mutable recursive list."""
    contents = empty_rlist
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_rlist(contents)
        elif message == 'getitem':
            return getitem_rlist(contents, value)
        elif message == 'push_first':
            contents = make_rlist(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return str(contents)
    return dispatch

def to_mutable_rlist(source):
    """Return a functional list with the same contents as source."""
    s = make_mutable_rlist()
    for element in reversed(source):
        s('push_first', element)
    return s
suits = ['heart', 'diamond', 'spade', 'club']
'''
'''
>>> s = to_mutable_rlist(suits)
>>> s
<function make_mutable_rlist.<locals>.dispatch at 0x037FE2B0>
>>> type(s)
<class 'function'>
>>> s('str')
"('heart', ('diamond', ('spade', ('club', None))))"
>>> s('pop_first')
'heart'
>>> s('str')
"('diamond', ('spade', ('club', None)))"
'''
# --------------------------------------
# Dictionaries
# --------------------------------------
#numerals = {'I': 1.0, 'V': 5, 'X': 10}
#numerals['X']  #10
#numerals['I']=1
#numerals['L']=50
#numerals
#{'I': 1, 'V': 5, 'X': 10, 'L': 50}
#sum(numerals.values())     #66
#dict([(3, 9), (4, 16), (5, 25)])
#{3: 9, 4: 16, 5: 25}
#numerals.get('A', 0)   #0
#numerals.get('V', 0)   #5
#{x: x*x for x in range(3,6)}
#{3: 9, 4: 16, 5: 25}

# --------------------------------------
# Dictionaries
# --------------------------------------
'''
def make_dict():
    """Return a functional implementation of a dictionary."""
    records = []
    def getitem(key):
        for k, v in records:
            if k == key:
                return v
    def setitem(key, value):
        for item in records:
            if item[0] == key:
                item[1] = value
                return
        records.append([key, value])
    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
        elif message == 'keys':
            return tuple(k for k, _ in records)
        elif message == 'values':
            return tuple(v for _, v in records)
    return dispatch
'''
# --------------------------------------
# Manipulating dictionary
# --------------------------------------
'''
>>> d = make_dict()
>>> d
<function make_dict.<locals>.dispatch at 0x0360E460>
>>> d('setitem', 3, 9)
>>> d('setitem', 4, 16)
>>> d('getitem', 3)
9
>>> d('getitem', 4)
16
>>> d('keys')
(3, 4)
>>> d('values')
(9, 16)
'''
# --------------------------------------
# Usage Nonlocal statement implementation
# --------------------------------------
'''
def make_account(balance):
    """Return a withdraw function that draws down
    balance with each call."""
    bal = {'balance':balance}
    def withdraw(amount):
	    if amount > bal['balance']:
		    return 'Insufficient funds'
	    bal['balance'] = bal['balance'] - amount 
	    return bal['balance']
    return withdraw
'''
# --------------------------------------
#m=make_account(100)
#m(10)  #90

# --------------------------------------
# Dispatch dictionary instead of dispatch func
# --------------------------------------
'''
def make_mutable_rlist():
    """Return a functional implementation of a mutable recursive list."""
    contents = empty_rlist
    def length():
        return len_rlist(contents)
    def get_item(ind):
        return getitem_rlist(contents, ind)
    def push_first(value):
        nonlocal contents
        contents = make_rlist(value, contents)
    def pop_first():
        nonlocal contents
        f = first(contents)
        contents = rest(contents)
        return f
    def strl():
        return str(contents)

    return {'length':length, 'get_item':get_item, 'push_first':push_first, 'pop_first': pop_first, 'str':strl}
'''
# --------------------------------------
# Manipulating Dispatch dictionary
# --------------------------------------
'''
>>> m = make_mutable_rlist()
>>> m['str']()
'None'
>>> m['push_first'](5)
>>> m['push_first'](3)
>>> m['str']()
'(3, (5, None))'
'''
