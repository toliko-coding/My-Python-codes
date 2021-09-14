# ------------------------------------------------
# Conventional Interfaces
# ------------------------------------------------
# S1 - Sum of n elements of Fibonacci sequence
# ------------------------------------------------
def fib(k): 
    """Compute the kth Fibonacci number.""" 
    prev, curr = 1, 0 # curr is the first Fibonacci number. 
    for _ in range(k - 1): 
        prev, curr = curr, prev + curr
    return curr
# ------------------------------------------------
# fib(20) # => 4181
# ------------------------------------------------
def iseven(n): 
    return n % 2 == 0
# ------------------------------------------------
#nums = (5, 6, -7, -8, 9) 
#tuple(filter(iseven, nums)) # => (6, -8) 
#sum(map(abs, nums)) # => 35 
# ------------------------------------------------
def sum_even_fibs(n): 
    """Sum the even members of the first n Fibonacci numbers.""" 
    return sum(filter(iseven, map(fib, range(1, n+1)))) 
# ------------------------------------------------
#sum_even_fibs(20) # => 3382
# ------------------------------------------------

# ------------------------------------------------
# S2
# ------------------------------------------------
#tuple('Spaces between words'.split()) # => ('Spaces', 'between', 'words') 
# ------------------------------------------------
def first(s):
    """Return first letter of string"""
    return s[0]
# ------------------------------------------------
def iscap(s):
    """Return True if first letter is Capital Letter"""
    return len(s) > 0 and s[0].isupper() 
# ------------------------------------------------
def acronym(name): 
    """Return a tuple of the letters that form the acronym for name.""" 
    return tuple(map(first, filter(iscap, name.split()))) 
# ------------------------------------------------
#acronym('Sami shamoon Collage of Engineering Department of Software Engineering') #->('S', 'C', 'E', 'D', 'S', 'E')
# ------------------------------------------------

# ------------------------------------------------
# Generator expressions
# <map expression> for <name> in <sequence expression> if <filter expression> 
# ------------------------------------------------
def sum_even_fibs1(n): 
    return sum(fib(k) for k in range(1, n+1) if fib(k) % 2 == 0)
# ------------------------------------------------
def sum_even_fibs2(n): 
    return sum(fib(k) for k in range(1, n+1) if iseven(fib(k)))
# ------------------------------------------------
def acronym1(name): 
    return tuple(w[0] for w in name.split() if iscap(w))
# ------------------------------------------------
def acronym2(name): 
    return tuple(first(w) for w in name.split() if iscap(w))
# ------------------------------------------------
#sum_even_fibs1(20) # => 3382
#acronym1('Sami shamoon Collage of Engineering Department of Software Engineering') #->('S', 'C', 'E', 'D', 'S', 'E')
# ------------------------------------------------


# ------------------------------------------------
# Reduce
# ------------------------------------------------
from operator import mul 
from functools import reduce 
#reduce(mul, (1, 2, 3, 4, 5))
# ------------------------------------------------
def product_even_fibs(n): 
    """Return the product of the first n even Fibonacci numbers, except 0."""
    return reduce(mul, filter(iseven, map(fib, range(2, n+1))))
# ------------------------------------------------
#product_even_fibs(20) # => 123476336640
# ------------------------------------------------

def reduce_even_fibs(n,f): 
    return reduce(f, filter(iseven, map(fib, range(2, n+1))))
# ------------------------------------------------
#reduce_even_fibs(20,lambda x,y:x*y) #mul => 123476336640
#reduce_even_fibs(20,lambda x,y:x+y) #sum => 3382
# ------------------------------------------------

