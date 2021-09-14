
from operator import getitem

def make_rat(n, d):
    return (n, d)
 
def numer(x):
    return getitem(x, 0)
def denom(x):
    return getitem(x, 1)
def make(x):
        try:
            result = numer(x)/denom(x)
        except ZeroDivisionError:
            return "Attempted to divide by zero"
        else:
            return result
def str_rat(x):
	"""Return a string n/d for numerator n and denominator d."""
	return '{0}/{1}={2}'.format(numer(x), denom(x),make(x))
def main():
    n=input("Enter numer number:")
    d=input("Enter denom number:")
    ns=0.0
    try:
        num=int(n)
        den=int(d)
        ns=make_rat(num,den)
    except ValueError:
        #Handle the exception
        print ('Try again and press numbers \n')
    else:
        print( str_rat(ns))
      
main()
