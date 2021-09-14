from operator import add,mul
# -------------------------------------------------
# S#4
# -------------------------------------------------
'''
for n in range(5):
    print(n)
    n=n+2
    print('*',n)
'''
# -------------------------------------------------
'''
0
* 2
1
* 3
2
* 4
3
* 5
4
* 6
'''
# -------------------------------------------------
# S#9
# -------------------------------------------------
def square(x):
    return mul(x, x)
def square1(x):
    mul(x, x) # Watch out! This call doesn’t return a value.
def square2(x):
    res = mul(x, x)   
def square3(x):
    global res
    res = mul(x, x)   

def print_square(x):
    print(square(x))

# -------------------------------------------------
# S#10
# -------------------------------------------------
'''
print (1)
print (print(1), print(2))
'''
# -------------------------------------------------
# S#11
# -------------------------------------------------
def percent_difference(x, y):
    difference = abs(x-y)
    return 100 * difference / x

# >>> percent_difference(40, 50)
# 25.0
# -------------------------------------------------
# S#13
# -------------------------------------------------
def fib(n):
    """Compute the nth Fibonacci number."""
    pred, curr = 0, 1 # Fibonacci numbers
    for _ in range(n):
        pred, curr = curr, pred + curr # Re-bind pred and curr
    return pred

# -------------------------------------------------
# S#17
# -------------------------------------------------
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k+1
    return total
'''
>>> sum_naturals(100)
5050
'''
def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total
'''
>>> sum_cubes(100)
25502500
'''
def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / (k * (k + 2)), k + 4
    return total
'''
>>> pi_sum(100)
3.121594652591009
'''
# -------------------------------------------------
# S#19-21
# -------------------------------------------------
def summation(n, term, next):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), next(k)
    return total
# -------------------------------------------------
def cube(k):
    return pow(k, 3)
def successor(k):
    return k + 1
def sum_cubes(n):
    return summation(n, cube, successor)
#>>> sum_cubes(3)
#36
# -------------------------------------------------
def identity(k):
    return k
def sum_naturals(n):
    return summation(n, identity, successor)
# >>> sum_naturals(10)
# 55
# -------------------------------------------------
def pi_term(k):
    denominator = k * (k + 2)
    return 8 / denominator
def pi_next(k):
    return k + 4
def pi_sum(n):
    return summation(n, pi_term, pi_next)
# >>> pi_sum(1e6)
# 3.1415906535898936
# -------------------------------------------------
# S#23-24
# -------------------------------------------------
def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess
# -------------------------------------------------
def near(x, f, g):
    return approx_eq(f(x), g(x))

def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance
# -------------------------------------------------
# S#25 golden ratio
# -------------------------------------------------
def golden_update(guess):
    return 1/guess + 1

def golden_test(guess):
    return near(guess, square, successor)

# >>> iter_improve(golden_update, golden_test)
# 1.6180371352785146
# -------------------------------------------------
# S#29 x^2 = a
# -------------------------------------------------
def average(x, y):
    return (x + y)/2

def sqrt_update(guess, a):
    return average(guess, a/guess)

# -------------------------------------------------
def square_root(a):
    def update(guess):
        return average(guess, a/guess)
    def test(guess):
        return approx_eq(square(guess), a)
    return iter_improve(update, test)
# -------------------------------------------------
'''
>>> square_root(5)
2.2360688956433634
>>> square_root(25)
5.000000000053722
'''
