# --------------------------------------
# The Anatomy of Recursive Functions 
# --------------------------------------
def isEven(n):
	if n == 1: return False
	return isOdd(n-1)

def isOdd(n):
	if n == 1: return True           
	return isEven(n-1)            

# --------------------------------------
'''
>>> isEven(8)
True
>>> isEven(81)
False
>>> isOdd(81)
True
>>> isOdd(8)
False
'''
# --------------------------------------
# Tree Recursion 
# --------------------------------------
def fib(n):
        if n == 1:
                return 0
        if n == 2:
                return 1
        return fib(n-2) + fib(n-1)
# --------------------------------------
'''
>>> fib(6)
5
'''
# --------------------------------------
# Memoization 
# --------------------------------------
def memo(f):
        """Return a memoized version of single-argument function f."""
        cache = {}
        def memoized(n):
                if n not in cache:
                        cache[n] = f(n)
                return cache[n]
        return memoized
# --------------------------------------
'''
>>> fib = memo(fib)
>>> fib(40)
63245986
'''
# --------------------------------------
# Recursive Lists 
# --------------------------------------
class Rlist(object):
        """A recursive list consisting of a first element and the rest."""
        class EmptyList(object):
                def __len__(self):
                        return 0

        empty = EmptyList()

        def __init__(self, first, rest=empty):
                self.first = first
                self.rest = rest
        def __repr__(self):
                args = repr(self.first)
                if self.rest is not Rlist.empty:
                        args += ', {0}'.format(repr(self.rest))
                return 'Rlist({0})'.format(args)
        def __len__(self):
                return 1 + len(self.rest)
        def __getitem__(self, i):
                if i == 0:
                        return self.first
                return self.rest[i-1]

# --------------------------------------
'''
>>> s = Rlist(1, Rlist(2, Rlist(3)))
>>> s.rest
Rlist(2, Rlist(3))
>>> len(s)
3
>>> s[1]
2
'''
# --------------------------------------
# Combining two lists 
# --------------------------------------
def extend_rlist(s1, s2):
        if s1 is Rlist.empty:
                return s2
        return Rlist(s1.first, extend_rlist(s1.rest, s2))
# --------------------------------------
'''
>>> s = Rlist(1, Rlist(2, Rlist(3)))
>>> extend_rlist(s.rest, s)
Rlist(2, Rlist(3, Rlist(1, Rlist(2, Rlist(3)))))
'''

# --------------------------------------
# Mapping a function over a list 
# --------------------------------------
def map_rlist(s, fn):
        if s is Rlist.empty:
                return s
        return Rlist(fn(s.first), map_rlist(s.rest, fn))
def square(x):
        return x*x
# --------------------------------------
'''
>>> s = Rlist(1, Rlist(2, Rlist(3)))
>>> map_rlist(s, square)
Rlist(1, Rlist(4, Rlist(9)))
'''

# --------------------------------------
# Filtering 
# --------------------------------------
def filter_rlist(s, fn):
        if s is Rlist.empty:
                return s
        rest = filter_rlist(s.rest, fn)
        if fn(s.first):
                return Rlist(s.first, rest)
        return rest
# --------------------------------------
'''
>>> s = Rlist(1, Rlist(2, Rlist(3)))
>>> filter_rlist(s, lambda x: x % 2 == 1)
Rlist(1, Rlist(3))
'''
# --------------------------------------
# Hierarchical Structures 
# --------------------------------------
def count_leaves(tree):
        if type(tree) != tuple:
                return 1
        return sum(map(count_leaves, tree))
# --------------------------------------
'''
>>> t = ((1, 2), 3, 4)
>>> count_leaves(t)
4
>>> big_tree = ((t, t), 5)
>>> big_tree
((((1, 2), 3, 4), ((1, 2), 3, 4)), 5)
>>> count_leaves(big_tree)
9
'''

# --------------------------------------
# Mapping and recursion together 
# --------------------------------------
def map_tree(tree, fn):
        if type(tree) != tuple:
                return fn(tree)
        return tuple(map_tree(branch, fn) for branch in tree)
# --------------------------------------
'''
>>> t = ((1, 2), 3, 4)
>>> big_tree = ((t, t), 5)
>>> map_tree(big_tree, square)
((((1, 4), 9, 16), ((1, 4), 9, 16)), 25)
'''

# --------------------------------------
# Mapping and recursion together 
# --------------------------------------
class Tree(object):
        def __init__(self, entry, left=None, right=None):
                self.entry = entry
                self.left = left
                self.right = right
	
        def __repr__(self):
                args = repr(self.entry)
                if self.left or self.right:
                        args += ', {0}, {1}'.format(repr(self.left), 				repr(self.right))
                return 'Tree({0})'.format(args)
def fib_tree(n):
        """Return a Tree that represents a recursive 	Fibonacci calculation."""
        if n == 1:
                return Tree(0)
        if n == 2:
                return Tree(1)
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.entry + right.entry, left, right)

# --------------------------------------
'''
>>> fib_tree(5)
Tree(3, Tree(1, Tree(0), Tree(1)), Tree(2, Tree(1), Tree(1, Tree(0), Tree(1))))
'''
