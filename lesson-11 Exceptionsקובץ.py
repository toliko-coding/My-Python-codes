# --------------------------------------
# Raising exceptions
# --------------------------------------
'''
>>> raise Exception('An error occurred')

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    raise Exception('An error occurred')
Exception: An error occurred
'''

# --------------------------------------
# Example
# --------------------------------------
'''
>>> try:
	x = 1/0
except ZeroDivisionError as e:
	print('handling a', type(e))
	x = 0	
('handling a', <type 'exceptions.ZeroDivisionError'>)
>>> x
0
'''
# --------------------------------------
# Example
# --------------------------------------
def invert(x):
    result = 1/x # Raises a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return result
def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)
# --------------------------------------
'''
>>> invert_safe(2)
Never printed if x is 0
0
>>> invert_safe(0)
'integer division or modulo by zero'
'''
# --------------------------------------
# Example: Newton’s method
# --------------------------------------
from math import sqrt
def approx_derivative(f, x, delta=1e-5):
    df = f(x + delta) - f(x)
    return df/delta
# --------------------------------------
def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)
    return update
# --------------------------------------
def find_root(f, initial_guess=10):
    def test(x):
        def approx_eq(x,y):
            return abs(x-y)< 1e-5
        return approx_eq(f(x), 0)
    return iter_improve(newton_update(f), test, initial_guess)
# --------------------------------------
def iter_improve(update, test, guess=1):
    print(guess)
    while not test(guess):
        guess = update(guess)
        print(guess)
    return guess
# --------------------------------------
def square_root(a):
    def square(x):
        return x*x
    return find_root(lambda x: square(x) - a)
# --------------------------------------
def func_root(a):
    return find_root(lambda x: 2*x*x + sqrt(x) - a)

'''
>>> square_root(16)
10
5.800002099877425
4.279312206273697
4.0091157184534305
4.000010374778599
4.000000000026422
4.000000000026422
>>> func_root(0)
10
4.940943260509369
2.3870712267378624
1.0761585432683334
0.37553813282078274
-0.010501189601387517
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    func_root(0)
  File "D:\BACKUP-DISK-D-19_8_2016\My\SCE\Principles of Programming Languages\2020-summer\Lec\Lec6\lesson-11.py", line 69, in func_root
    return find_root(lambda x: 2*x*x + sqrt(x) - a)
  File "D:\BACKUP-DISK-D-19_8_2016\My\SCE\Principles of Programming Languages\2020-summer\Lec\Lec6\lesson-11.py", line 62, in find_root
    return iter_improve(newton_update(f), test, initial_guess)
  File "D:\BACKUP-DISK-D-19_8_2016\My\SCE\Principles of Programming Languages\2020-summer\Lec\Lec6\lesson-11.py", line 72, in iter_improve
    while not test(guess):
  File "D:\BACKUP-DISK-D-19_8_2016\My\SCE\Principles of Programming Languages\2020-summer\Lec\Lec6\lesson-11.py", line 61, in test
    return approx_eq(f(x), 0)
  File "D:\BACKUP-DISK-D-19_8_2016\My\SCE\Principles of Programming Languages\2020-summer\Lec\Lec6\lesson-11.py", line 69, in <lambda>
    return find_root(lambda x: 2*x*x + sqrt(x) - a)
ValueError: math domain error
'''


'''
# --------------------------------------
class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess
# --------------------------------------
def iter_improve(update, test, guess=1):
    try:
        while not test(guess):
            guess = update(guess)
        return guess
    except ValueError:
        raise IterImproveError(guess)
# --------------------------------------
def find_root(f, initial_guess=10):
    def test(x):
        def approx_eq(x,y):
            return abs(x-y)< 1e-5        
        return approx_eq(f(x), 0)
    try:
        return iter_improve(newton_update(f), test, initial_guess)
    except IterImproveError as e:
        return e.last_guess
'''

# --------------------------------------
# Example
# --------------------------------------
def func(x):
    try:        
        y = 1/x
        print(x)
    except ZeroDivisionError as e:
        print(type(e))
    else:      
        print("Else")
    finally:  
        print("Finally")
    print("after try-except")
# --------------------------------------
'''
>>> func(0)
<class 'ZeroDivisionError'>
Finally
after try-except
>>> func(3)
3
Else
Finally
after try-except
>>> 
'''
