# ---------------------------- KOT ANATOLI ----- 324413756 ---------------------------

#TASK 4
'function that return the next item according to the jumps'
def next(k,jump):
    return k + jump

'function that return the value of functon f on k'

def term(f,k):
    return f(k)

'function that use both function above - return sum of all the values that returned from the '
'function f that gets arrgumet k with jumps of arrgumet jump '
def summation(f,k,jump,n):
    total = 0
    while k < n:
        total = total + 2* term(f,k)
        k = next(k,jump)

    return total

'''
function that return volume of function f between point a to b
 this function using Trapez method that divide the shape to n pices'''
def Trapez_rule(f,a,b,n):
    left = (b - a)
    jump = left / n
    left = left / (2*n)
    first = a + jump

    S = f(a) + f(b) + summation(f,first,jump,b)
    return S * left


print("----- TASK 4 Tests -----")
print(Trapez_rule(lambda x:x**2 , 0 , 10 ,10000))
print(Trapez_rule(lambda x:x**9 , 0 , 10 ,10000))




#Task 5
"""
functio that return True if the numebr n is a Prime number
"""
def myPrime(n):
    flag = True
    if n == 2 :
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                flag = False

            if flag == False:
                break

        return flag

'function that return True if the value n is in a Fibunachi sequence'
def isFib(n):
    flag = False
    i=0
    while(True):
       if fibNumber(i) > n or flag == True:
           break
       else:
           if fibNumber(i) == n:
                flag = True
           else:
               i = i + 1
    return flag

'function that return the value of Fibunachi number in place n'
def fibNumber(n):
    if n < 2:
        return 1;
    else:
        return fibNumber(n-1) + fibNumber(n-2)


'function that get list and a boolean function and return a new list of all the numbers in the list that are' \
'True according to the function'
def myFilter(L,func):
    list = []
    for item in L:
        if func(item) == True:
            list = list + [item]

    return list

print("----- TASK 5 Tests -----")

#myFilter
list = [2,4,5,6]
test = myFilter(list,myPrime)
print(test)


"""
function that get a List of numbers and a List of functions 
and return a new List of all the numbers that are True acoording to the Function List"""
def myFilterMulti(L,funcL):
    list = myFilter(L,funcL[0])
    for i in range(1,len(funcL)):
        list = myFilter(list,funcL[i])

    return list

#for myFilterMulti (isFib and myPrime) only
list = [2,4,5,6,7,13]
funcL = [myPrime,isFib]
print(myFilterMulti(list,funcL))

##for myFilterMulti with lambda
list = [2,4,5,13,41,55,89,107,144]
funcL = [myPrime,isFib,lambda x:x >= 9 and x < 100]
print(myFilterMulti(list,funcL))





#Task 6
'return square of the value'
def square(x):
    return x**2
'increace value by one'
def incr(x):
    return x + 1

"function that return funcion with enviroment , if you run the new function" \
"you get repet your new value n time acoorind to function f"
def repeated(f,n):
    def dis(x):
        for i in range(n):
            x = f(x)
        return x
    return dis


print("----- TASK 6 Tests -----")
z = repeated(incr,4)(2)
print(z)
z=repeated(square,2)(5)
print(z)


def compose(f,g):
    return lambda x : f(g(x))

def repeated2(f,n):

    if n > 1:
        return compose(repeated2(f,n-1),f)
    return f


z = repeated2(incr,4)(2)
print(z)
z=repeated2(square,2)(5)
print(z)
