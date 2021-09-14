# ------------------------------------------------
# class Fraction
# Attributes: numerator,denominator
# ------------------------------------------------
class Fraction(object):
# ------------- Constructor ----------------------
    def __init__(self,num=0,den=1):
        self.numerator = num
        self.denominator = den
# ------------- Print Fraction -------------------
    def printFraction(self):
        if self.denominator == 1:
            print(self.numerator)
        elif self.numerator > self.denominator:
            print('{0} {1}/{2}'.format(self.numerator//self.denominator,self.numerator%self.denominator,self.denominator))            
        else:
            print('{0}/{1}'.format(self.numerator,self.denominator))
# ------------- Real Number ----------------------
    def RealNum(self):
        if self.denominator == 1:
            return float(self.numerator)
        return self.numerator/self.denominator
# ------------- Fractions Reduction --------------
    def Reduction(self):
        den = self.denominator-1
        flag = False
        while den > 0 and flag == False:
            flag = (self.numerator%den == 0)and(self.denominator%den == 0)
            if flag == False:
                den -= 1
        if flag == True:
            self.numerator //= den
            self.denominator //= den
        return self

# ------------- Adding Fractions -----------------
    def __add__(self,other):
        self.numerator=self.numerator*other.denominator+other.numerator*self.denominator
        self.denominator*=other.denominator
        return self.Reduction()           

# ------------- Driver ---------------------------
def driver():
    num1 = Fraction(6,9)
    num2 = Fraction(1,4)
    num1.printFraction()                # => 6/9
    (num1.Reduction()).printFraction()  # => 2/3
    print(num1.RealNum())               # => 0.6666666666666666 
    print('----------')
    (num1+num2).printFraction()         # => 11/12
    print('----------')
    num3 = Fraction(1,6)                
    num4 = Fraction(1,3)
    (num3+num4).printFraction()         # => 1/2
    print('----------')
    num5 = Fraction(23,7)   
    num5.printFraction()                # => 3 2/7

driver()
