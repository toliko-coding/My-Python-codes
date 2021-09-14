# ------------------------------------------------
# Dispatch sample
# ------------------------------------------------
def make_nums( x, y):
    count = 0
    def dispatch(op):
        nonlocal count
        val = 0
        def func1(var):
            nonlocal x, y
            if var=='x':
                x += val
                return x
            elif var=='y':
                y += val
                return y
            else:
                return 'Error'
        if op=='view':
            return (x,y,count)
        elif op=='add':
            count+=1
            return x+y
        elif op=='sub':
            count+=1
            return x-y
        elif op == 'inc':
            val = 1
            return func1
        elif op == 'dec':
            val = -1
            return func1
        else:
            return 'Incorrect parameter'
    return dispatch
# ------------------------------------------------
#n1=make_nums(31,4)
#n1('view')     # => (31, 4, 0)
#n1('add')      # => 35
#n1('view')     # => (31, 4, 1)
#n1('mul')      # => 'Incorrect parameter'
#n1('inc')('y') # => 5
#n1('dec')('x') # => 30
#n1('sub')      # => 25
#n1('view')     # => (30, 5, 2)
# ------------------------------------------------


# ------------------------------------------------
#    Sets
# ------------------------------------------------
#s1={1,2,3,4,5}
#s1 => {1, 2, 3, 4, 5}
#s2=set((1,2,3,4,5))
#s2 => {1, 2, 3, 4, 5}
#s3=set([1,2,3,4,5])
#s3 => {1, 2, 3, 4, 5}

# ------------------------------------------------
#    Dictionaries
# ------------------------------------------------
#numerals={'I':1.0,'V':5,'X':10}
#numerals           => {'I': 1.0, 'V': 5, 'X': 10}
#numerals['X']      => 10
#numerals['A']=40
#numerals           => {'I': 1.0, 'V': 5, 'X': 10, 'A': 40}
#numerals['I']=1.5
#numerals           => {'I': 1.5, 'V': 5, 'X': 10, 'A': 40}
#numerals.values()  => dict_values([1.5, 5, 10, 40])
#numerals.keys()    => dict_keys(['I', 'V', 'X', 'A'])
#sum(numerals.values()) => 56.5
#tuple(numerals.keys()) => ('I', 'V', 'X', 'A')
#dict([(3,9),(4,16),(5,25)])    => {3: 9, 4: 16, 5: 25}
#d1=dict([(3,9),(4,16),(5,25)])
#d1                             => {3: 9, 4: 16, 5: 25}
#d2=dict(((3,9),(4,16),(5,25)))
#d2                             => {3: 9, 4: 16, 5: 25}
#d3=dict([[3,9],[4,16],[5,25]])
#d3                             =>{3: 9, 4: 16, 5: 25}
#d4=dict(('ab','cd'))
#d4                             => {'a': 'b', 'c': 'd'}
#d1.get(3)                      => 9
#d1.get(3,40)                   => 9
#d1.get(30,40)                  => 40

# ------------------------------------------------
#    String methods
# ------------------------------------------------
#'The London is CapitaL of GREAT BRITIAN'.lower()
#'the london is capital of great britian'
#'12345'.isnumeric()            => True
#'1234.5'.isnumeric()           => False
#'12a'.isnumeric()              => False

# ------------------------------------------------
#    in or not in operators
# ------------------------------------------------
#a=(1,2,3,4,5)
#3 in a                         => True
#6 not in a                     => True
#6 in a                         => False
#'abc' in ['aaa','abc','bbb']   => True
#'aaa' in {'sss':2,'aaa':5}     => True

# ------------------------------------------------
#    min and max
# ------------------------------------------------
#min(1,2,3,4,5)             => 1
#min((1,2,3,4,5))           => 1
#min([1,2,3,4,5])           => 1
#min('1,2,3,4,5')           => ','
#min({1,2,3,4,5})           => 1
#min({'a':1,'b':5,'c':2})   => 'a'
#max(1,2,3,4,5)             => 5
#max((1,2,3,4,5))           => 5
#max([1,2,3,4,5])           => 5
#max('1,2,3,a,4,5')         => 'a'
#max({1,2,3,4,5})           => 5
#max({'a':1,'b':5,'c':2})   => 'c'

# ------------------------------------------------
#    reduce
# ------------------------------------------------
from functools import reduce
#reduce(lambda x,y: x+y,(1,2,3,4,5))    => 15
#reduce(lambda x,y: x+y,(1,2,3,4,5),10) => 25
#reduce( lambda x,y: x or y%2==0,(1,2,3,4,5),False) => True
#reduce( lambda x,y: x or y%2==0,(1,7,3,9,5),False) => False
# reduce(lambda x,y: x+(y,),(1,2,3,4,5),()) => (1, 2, 3, 4, 5)

# ---------------------- S1 ----------------------
def func1():
    def func11():
        return 5
    def func12():
        return -5
    return (func11, func12)
# ------------------------------------------------
f1=func1()
#f1[1]() => -5
#f1[0]() => 5

# ---------------------- S2 ----------------------
def func2():
    def func21():
        return 5
    def func22():
        return -5
    return [func21, func22]
# ------------------------------------------------
f2=func2()
#f2[1]() => -5
#f2[0]() => 5



# ---------------------- S3 ----------------------
def func4():
    def dispatch(op):
        def func41():
            return 5
        def func42():
            return -5
        if op==1:
            return func41
        elif op==2:
            return func42
    return dispatch
# ------------------------------------------------
f4=func4()
#f4(1)() => -5
#f4(2)() => 5


# ---------------------- S4 ----------------------
def func5(*s):
    list1 = list(s)
    for w in list1:
        print(w,end=', ')
# ------------------------------------------------
#func5('aaa','bbb','ccc') # => aaa, bbb, ccc,

