# ------ Anatoli Kot - 324413756 ---- HM - 4 -------

from functools import reduce
from operator import *

# ---------------------  Task 1 -------------------------
'''Date class that hold given date'''
class Date():

    #monthList = {1:"January" , 2:"February" , 3:"March", 4:"April" , 5 :"May" , 6:"June" , 7:"July" , 8:"August" , 9:"September" , 10:"October" , 11:"November" , 12:"December"}
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        self.monthList = {1:"January" , 2:"February" , 3:"March", 4:"April" , 5 :"May" , 6:"June" , 7:"July" , 8:"August" , 9:"September" , 10:"October" , 11:"November" , 12:"December"}


    def __str__(self):

        return "{}th of {} , {}".format(self.day , self.monthList[self.month] , self.year)

    def __repr__(self):
        return "Date({},{},{})".format(self.year,self.month , self.day)


'''Time class that hold time -> hour:minute '''
class Time():
    def __init__(self , hour , minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return "{0:02d}:{1:02d}".format(self.hour, self.minute)

    def __repr__(self):
        return "Time({}.{})".format(self.hour,self.minute)


    '''Method that check if self is bigger then other'''
    def isBigger(self,other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute >= other.minute:
                return True
            else:
                return False

        else:
            return False


    '''Method that check if self is smaller then other'''
    def isSmaller(self,other):
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute <= other.minute:
                return True
            else:
                return False

        else:
            return False



'''Calendar Class that contain task by day and time '''
class CalendarEntry():
    todoList = {}
    '''key = start time hour , value = [start,end,name]'''

    tasks = {}


    '''this list will hold the order of the task by hour'''
    order = []

    def __init__(self , year , month , day):
        self.date = Date(year,month,day)

    def __str__(self):
        print("Todo list for : ",end='')
        print(self.date)
        print("order : ")
        print(self.order)
        print("print : : ")

        j=1
        for i in self.order:
            #print(self.todoList[tuple(i)])
            print("{} . {} - {} - {}".format(j , self.todoList[tuple(i)][0]  , self.todoList[tuple(i)][1]  , self.todoList[tuple(i)][2]  ))
            j += 1

        return ""



    def __repr__(self):
        return "CalendarEntry({},{}.{})".format(self.date.year , self.date.month, self.date.day)

    '''function that check the task if True add task to the list of tasks'''
    def addTask(self,taskName , start,end):
        def checkTime(newstart,newendt):
            flag = True
            for task in self.todoList.values():
                # print(task)
                # Note : task[0] = currentStart , 1 : **end
                #               >                                 <  (start in midle)
                if newstart.isBigger(task[0]) and newstart.isSmaller(task[1]):
                    flag = False
                #             >                              <       (in midle)
                if newendt.isBigger(task[0]) and newendt.isSmaller(task[1]):
                    flag = False
                #                                                     (over other task)
                if newstart.isSmaller(task[0]) and newendt.isBigger(task[1]):
                    flag = False




            return flag

        if checkTime(start,end):

            self.todoList[(start.hour , start.minute)] = [start,end,taskName]
            self.order.append([start.hour , start.minute])
            self.order.sort()

            self.tasks[(str(start) , str(end))] = taskName

            print("Task added successfully.. ")

        else:
            print("Sorry , this time : {} - {} is already taken by another task".format(start,end))




print("#--------------------  Task 1 --------------------------#")

today = Date(2021,8,15)
# print(repr(today))
# print(today.year)
print(today)
todo = CalendarEntry(1994,8,15)
t = Time(10,0)
print(str(t))
#                             #t = Time(10,0)
todo.addTask("PPL Lecture", t, Time(13,0))
todo.addTask("PPL homework'#'1", Time(14,0), Time(16,0))
todo.addTask("PPL homework'#'2", Time(14,0), Time(16,0))
todo.addTask("PPL homework'#'3", Time(9,0), Time(10,30))
todo.addTask("PPL homework'#'4", Time(14,30), Time(16,30))
todo.addTask("PPL homework'#'5", Time(8,30), Time(23,30))
todo.addTask("PPL homework'#'6", Time(13,30), Time(15,30))

#
#
#
#
#
#
print("todo.tasks : ")
print(todo.tasks)
print(todo)
# todo = CalendarEntry(1994,12,28)
# todo.addTask("test1",Time(20,00) , Time(23,00))
# todo.addTask("tes2",Time(23,30) , Time(2,00))
# todo.addTask("test3",Time(22,45) , Time(1,45)) #x
# todo.addTask("test4",Time(14,45) , Time(2,20)) #x
# todo.addTask("test5",Time(19,30) , Time(20,00)) #x


# print(todo)
# print(todo.tasks)

# time1 = Time(22,1)
# time2 = Time(21,59)
#
# print(time1.isSmaller(time2))








# --------------------  Task 2 --------------------------  *****NOT COMPLETED - need to def checkTask line : 266



'''function that create class value by dict'''
def make_class(attrs, base=None):
    #print("make_class atrrs : " , attrs)
    """Return a new class (a dispatch dictionary) with given class attributes"""
    #print(attrs)
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value): attrs[name] = value

    # Return a new initialized objec'aaa': 5.5t instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        # print("Creating new")
        # print("args : " , args)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):       attrs[name] = value



        # instance dictionary
        obj = { 'get': get, 'set': set }

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = { 'get': get, 'set': set, 'new': new }
    return cls

'''function that create date class type'''
def make_date_class():
    monthList = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                 9: "September", 10: "October", 11: "November", 12: "December"}

    def __init__(self,year,month,day):
        self['set']("year",year)
        self['set']("month",month)
        self['set']("day",day)

    def str(self):
        return "{}th of {} , {} ".format(  self['get']('month') , monthList[ self['get']('month') ]    , self['get']('year')    )

    return make_class(locals())


'''function that create time class type'''
def make_time_class():

    def __init__(self,hour,minute):
        self['set']("hour",hour)
        self['set']("minute",minute)

    def __str__(self):
        return "{0:02d}:{1:02d}".format(  self['get']('hour')   , self['get']('minute')   )
        #print("here")

    def isBigger(self,other):
        return True


    return make_class(locals())


'''function that create calentry class type'''
def make_calentry_class():
    tasks = {}
   #Date = make_date_class()
    def __init__(self,year,month,day):
        self['set']("year" , year)
        self['set']("month" , month)
        self['set']("day" , day)

    def addTask(self , name , stime,etime):
        def checkTask():
            return True

        if checkTask():
            self['get']('tasks')[(stime['get']("__str__")(),etime['get']("__str__")())] = name
            print("Task {} added to the list".format(name))
        else:
            print("There is already task in this time : {}-{}".format(stime["get"]("__str__")() ,etime["get"]("__str__")() ))

    return make_class(locals())




print("#--------------------  Task 2 --------------------------#")
Date = make_date_class()
today = Date['new'](2021,8,15)
print(today['get']('year'))
print(today['get']('str')())
#
CalendarEntry = make_calentry_class()
todo = CalendarEntry['new'](2021,8,15)
#
Time = make_time_class()
t = Time['new'](10,0)
print(t['get']("__str__")())
t['set']('fun',lambda :print("function"))
t['get']('fun')()
#
#
todo['get']('addTask')('PPL lecture',t,Time['new'](13,0))
todo['get']('addTask')("PPL Homewwork#4", Time['new'](14,0), Time['new'](16,0))
#
print( todo['get']('tasks') )


# t1 = ("10:00" , "12:00")
# t2 = ("13:00" , "15:00")
# t3 = ("10:00" , "10:05")
#
# print(t1 > t3)





#--------------------  Task 3 --------------------------




class Shekel():

    def __init__(self,shekel=1):
        self.shekel = float(shekel)

    def amount(self):
        return self.shekel

    def __repr__(self):
        return "Shekel({})".format(self.shekel)

    def __str__(self):
        return "{}nis".format(self.shekel)

    def __add__(self, other):
        return add_ShekelsAndOther(self,other)



class Dollar():
    def __init__(self,dollar=1):
        self.dollar = float(dollar)

    def amount(self):
        return self.dollar * rates[('dollar', 'nis')]


    def __repr__(self):
        return "Dollar({})".format(self.dollar)

    def __str__(self):
        return "{}$".format(self.dollar)

    def __add__(self, other):
        return add_ShekelsAndOther(self,other)


class Euro():
    def __init__(self,euro=1):
        self.euro = float(euro)

    def amount(self):
        return self.euro * rates[('euro','nis')]

    def __repr__(self):
        return "Euro({})".format(self.euro)

    def __str__(self):
        return "{}€".format(self.euro)

    def __add__(self, other):
        return add_ShekelsAndOther(self,other)


'functions that return True if the object is the real object'
def isShekel(obj):
    return True if type(obj) == Shekel else False

def isDollar(obj):
    return True if type(obj) == Dollar else False

def isEuro(obj):
    return True if type(obj) == Euro else False



def getRate(obj1,obj2):
    ':returns the rate number between two objects'
    return rates[(type_tag(obj1) , type_tag(obj2))]




def add_ShekelsAndOther(x,y):
    return Shekel(x.amount() + y.amount())








print("#--------------------  Task 3 --------------------------#")

rates ={('dollar','nis'): 3.22,('euro','nis'): 3.81}

s = Shekel(50)
d = Dollar(50)
e = Euro(50)

print("getRate function test :")


print("amount() method :")
print(s.amount() , d.amount() , e.amount())

print("print test :")
print(s,d,e)

print("d + s tests :")
print(repr(d + s))
print(d + s)

print("eval tests :")
z = eval(repr(d))
print(z)
print(type(z))
#
#




#--------------------  Task 4 --------------------------

'''add  to all the types'''


def type_tag(obj):
    ':returns the type of the object according to the type_tag.tags list'
    return type_tag.tags[type(obj)]

type_tag.tags = {Shekel : 'nis' , Dollar : 'dollar' , Euro : 'euro'}

'add functions :'
def add_Dollars(x,y):
    return Dollar(x.dollar + y.dollar)

def add_DollarAndShekel(x,y):
    if getRate(x,y):
        return Dollar(x.dollar + y.shekel * getRate(x,y))
    else:
        return Dollar(x.dollar)

def add_DollarAndEuro(x,y):
    if getRate(y,x):
        return Dollar(x.dollar + y.euro * getRate(y,x))
    else:
        return Dollar( (x.amount() + y.amount()) * getRate(x,Shekel))


def add_Euros(x,y):
    return Euro(x.euro + y.euro)

def add_EuroAndShekel(x,y):
    if getRate(x,y):
        return Euro(x.euro + y.shekel * getRate(x,y))
    else:
        return Euro((x.amount + y.amount) * getRate(x,y))

def add_EuroAndDollar(x,y):
    if getRate(x,y) :
        return Euro(x.euro + y.dollar * getRate(x,y) )
    else:
        return Euro( (x.amount() + y.amount()) * getRate(x,Shekel) )




def add(z1,z2):
    'get two types and make a ad betewwn , return type of z1'

    tags = (type_tag(z1) , type_tag(z2))
    return add.implementation[tags](z1,z2)

    print("Error ' the first object dont have function to do add operation")

add.implementation = {}
add.implementation[('nis' , 'dollar')] = add_ShekelsAndOther
add.implementation[('nis' , 'euro')] = add_ShekelsAndOther
add.implementation[('nis' , 'nis')] = add_ShekelsAndOther

add.implementation[('dollar' , 'nis')] = add_DollarAndShekel
add.implementation[('dollar' , 'euro')] = add_DollarAndEuro
add.implementation[('dollar' , 'dollar')] = add_Dollars

add.implementation[('euro' , 'nis')] = add_EuroAndShekel
add.implementation[('euro' , 'dollar')] = add_EuroAndDollar
add.implementation[('euro' , 'euro')] = add_Euros






'''sub functions : '''

def sub_ShekelAndOther(x,y):
    return Shekel(float(x.amount() - y.amount()))

def sub_Dollars(x,y):
    return Dollar(x.dollar - y.dollar)

def sub_DollarAndShekel(x,y):
    if getRate(x,y):
        return Dollar(x.dollar - y.shekel * getRate(x,y))
    else:
        return Dollar((x.amount() - y.amount() * getRate(x,Shekel)))

def sub_DollarAndEuro(x,y):
    if getRate(y,x):
        return Dollar(x.dollar - y.euro * getRate(y,x))
    else:
        return Dollar( (x.amount() - y.amount() ) * getRate(x,Shekel))

def sub_Euros(x,y):
    return Euro(x.euro - y.euro)

def sub_EuroAndShekel(x,y):
    if getRate(x,y):
        return Euro(x.euro - y.shekel * getRate(x,y))
    else:
        return Euro( (x.amount() - y.amount()) * getRate(x,Shekel) )

def sub_EuroAndDollar(x,y):
    if getRate(x,y):
        return Euro(x.euro - y.dollar * getRate(x,y))
    else:
        return Euro( (x.amount() - y.amount() ) *getRate(x,Shekel) )

def sub(z1,z2):
    'get two types and make a sub betewwn , return type of z1'
    tags = (type_tag(z1), type_tag(z2))
    # print(tags)
    return sub.implementation[tags](z1, z2)

sub.implementation = {}
sub.implementation[('nis' , 'dollar')] = sub_ShekelAndOther
sub.implementation[('nis' , 'euro')] = sub_ShekelAndOther
sub.implementation[('nis' , 'nis')] = sub_ShekelAndOther

sub.implementation[('dollar' , 'nis')] = sub_DollarAndShekel
sub.implementation[('dollar' , 'euro')] = sub_DollarAndEuro
sub.implementation[('dollar' , 'dollar')] = sub_Dollars

sub.implementation[('euro' , 'nis')] = sub_EuroAndShekel
sub.implementation[('euro' , 'dollar')] = sub_EuroAndDollar
sub.implementation[('euro' , 'euro')] = sub_Euros




def apply(opName , x, y ):
    'gets operatin by string and meke the operation on x and y'
    return apply.implementations[opName](x,y)

apply.implementations = {'add' : add , 'sub':sub}




print("#--------------------  Task 4 --------------------------#")



print(apply('add',Shekel(50) , Dollar(20)))
rates[('euro','dollar')] = 1.83
print( apply('add',Dollar(50) , Euro(20)) )
#print(apply('sub',Dollar(50) , Euro(20)))


print("apply shekel tests:")
print(apply('add',Shekel(50) , Shekel(20)))
print(apply('add',Shekel(50) , Dollar(20)))
print(apply('add',Shekel(50) , Euro(20)))

print("apply Dollar tests:")
print(apply('add',Dollar(50) , Shekel(20)))
print(apply('add',Dollar(50) , Dollar(20)))
print(apply('add',Dollar(50) , Euro(20)))

print("apply Euro tests:")
print(apply('add',Euro(50) , Shekel(20)))
print(apply('add',Euro(50) , Dollar(20)))
print(apply('add',Euro(50) , Euro(20)))



print(apply('add',Shekel(50) , Dollar(20)))
rates[('euro','dollar')] = 1.183

print(apply('add',Dollar(50) , Euro(20)))

print(apply('sub',Dollar(50) , Euro(20)))










#--------------------  Task 4 --------------------------

'''Dollar class coercions'''
def Dollar_to_shekel(dollar):
    return Shekel(dollar.amount())


def Dollar_to_euro(dollar):
    return Euro(dollar.dollar / getRate(Euro() , Dollar()))


'''Shekel class coercions'''
def Shekel_to_dollar(shekel):
    return Dollar(shekel.shekel / getRate(Dollar(),Shekel()))

def Shekel_to_Euro(shekel):
    return Euro(shekel.shekel / getRate(Euro() , Shekel()))


'''Euro class coercions'''
def Euro_to_Shekel(euro):
    return Shekel(euro.amount())

def Euro_to_dollar(euro):
    return Dollar(euro.euro * getRate(Euro(),Dollar()))

coerions = {("dollar" , "nis") : Dollar_to_shekel ,
            ( "dollar" , "euro") : Dollar_to_euro ,
             ("shekel", "euro"): Shekel_to_Euro,
                ("shekel", "dollar"): Shekel_to_dollar,
               ("euro", "nis"): Euro_to_Shekel ,
                ("euro", "dollar"): Euro_to_dollar
            }


def coerce_apply(operator , obj1 , obj2):
    res = apply(operator,obj1,obj2)
    if isShekel(res):
        return res
    else:
        return coerions[(type_tag(res) , 'nis')](res)




print("#--------------------  Task 5 --------------------------#")

print((Dollar_to_shekel(Dollar())))
print(Dollar_to_euro(Dollar()))

print(Shekel_to_dollar(Shekel(100)))
print(Shekel_to_Euro(Shekel(100)))

print(Euro_to_Shekel(Euro(100)))
print(Euro_to_dollar(Euro(100)))

print(coerions[(("dollar" , "nis"))](Dollar(50)))

print(coerce_apply('add',Shekel(50) , Dollar(20)))

print(coerce_apply('sub' ,Dollar(50),Euro(20)))


#--------------------  Task 6 --------------------------

'''function that create a parking place with hour payment + how many places in each parking type , return dict with message passig to functions'''
def parking(payment,f1,f2,f3):

    '''exeptions section : '''
    try:
        if payment <= 0 :
            raise ValueError("Error , the payment cant be negative or 0 , value given : {}".format(payment))

        if f1 <= 0 or f2 <= 0 or f3 <= 0:
            raise ValueError("Error , one of the parking type have no space to park , value given : {}".format(min(f1,f2,f3)))

    except ValueError as e:
        print(e)

    else:
        '''all the rest of parking()'''


        print("parking :: payment :{} ,Regular places :{} , Priority places :{} , VIP places :{} :: is created )".format(payment,f1,f2,f3))
        cars = {}
        space = {"Regular" : [0,f1] , "Priority" : [0,f2] , "VIP" : [0,f3]}


        '''boolean function that check if there is a place to park in given type parking '''
        def check_space(ptype):
            if space[ptype][0] < space[ptype][1] :
                #print(space[ptype][0] , space[ptype][1])
                return True
            else:
                return False


        '''function that print all the cars that belong to type parking that given'''
        def print_parking(ptype):
             if ptype in space :
                print("Printin all the {} type parking ... ".format(ptype))
                for car,items in cars.items():
                    if items[0] == ptype :
                        print("car : {} , type : {} , time : {}".format(car,items[0] , items[1]))
             else:
                 print("cant print {} because is not a parking type".format(ptype))

             print("Printing is Done")



        '''function that start parking to given car number in the parking type that given '''
        def start_parking(number,ptype):

            '''exeption section :'''
            try:

                if type(number) != int:
                    raise TypeError("Error , incorrect car number : {} type : {}" . format(number , type(number)))
                if not ptype in space:
                    raise TypeError("Error , {} in incorrect parking type".format(ptype))

            except TypeError as e:
                print(e)
                # exit()
            else:
                if ptype in space:
                    if number in cars:
                        print("This car : {} is already exict in the parking".format(number))
                    else:
                        if check_space(ptype):
                            cars[number] = [ptype,1]
                            space[ptype][0] += 1
                            print("Car {} is added to {} parking".format(number,ptype))
                        else:
                            print("{} parking is full car {} isnt registered to the system".format(ptype,number))

                else:
                    print("{} is not a parking type , parking registration stoped".format(ptype))


        '''function that print all the cars that exict'''
        def print_list():
            count = 0

            '''this 2 rows below print all the cars that exicst'''
            # for key , value in cars.items():
            #     print("car : {} , parking type : {} , parking time : {}".format(key , value[0], value[1]))

            def end():
                'Return False if the count is not in the end if the list'
                nonlocal count

                if count >= len(cars):
                    raise IndexError("no car")
                else:
                    return False


            def next():
                nonlocal count
                try:
                    end()
                except IndexError as e:
                    print(e)

                else:

                    temp = list(cars.items())
                    #print(temp[count])
                    print("car : {} , type : {} , time : {} ".format(temp[count][0]  , temp[count][1][0] , temp[count][1][1] ))
                    count +=1




            clsp = {"end" : end , "next" : next}
            return clsp


        '''function that end the parking of given car number , printing the payment and delete the car from car list'''
        def end_parking(number):
            if number in cars:
                if cars[number][0] == "Regular":
                    pay = cars[number][1] * payment

                if cars[number][0] == "Priority":
                    pay = cars[number][1] * payment * 2

                if cars[number][0] == "VIP":
                    pay = cars[number][1] * payment * 3


                print("car: {} , parking type : {} , parking time : {} - is ended the parking ".format(number , cars[number][0] , cars[number][1]))
                cars.pop(number)
                print("payment : {}".format(pay))

            else:
                print("car {} not found".format(number))





        '''function that increace the time to all the cars that in the parking'''
        def next_time():
            for car,items in cars.items():
                items[1] += 1







        '''this is the dicsenury '''
        cls = {"print_list" : print_list , "start_parking" : start_parking , "next_time" : next_time , "print_parking" : print_parking , "end_parking" : end_parking}

        return cls

print("#--------------------  Task 6 --------------------------#")

park1 = parking(-10,3,3,3)
park1 = parking(10,0,3,3)
park1 = parking(10,3,3,3)

park1["start_parking"]('aaa',"Regular")
park1['start_parking'](223,'VIP1')

park1['start_parking'](222,'Regular')
park1['start_parking'](223, 'Regular')
park1['next_time']()
park1['start_parking'](224,'Regular')
park1['start_parking'](225,'VIP')
prn=park1['print_list']()
print(prn)

for _ in range(6):
    prn['next']()



#--------------------  Task 7 --------------------------

class Expr():
    def __init__(self , operator , operand1,operand2):
        self.operator = operator
        self.operand1 = operand1
        self.operand2 = operand2

    # def __str__(self):
    #     return "operator : {} , operand1 : {} , operand2 : {}".format(self.operator,self.operand1 ,self.operand2)


    def __repr__(self):
        return "Expr({},{},{})".format(self.operator,self.operand1,self.operand2)

    def clean(self):
        if type(self.operand1) == int and type(self.operand2) == int:
            return True
        else:
            return False

    def getTuple(self):
        return (self.operator,self.operand1,self.operand2)



def buikdExprTree(tuple3):
    'this function get tuple and build tree of EXPR objects'
    if type(tuple3) == int:
        return tuple3

    temp = Expr(tuple3[0],tuple3[1],tuple3[2])
    if temp.clean():
        return Expr(tuple3[0],tuple3[1],tuple3[2])
    else:
        if type (tuple3[1]) == tuple or type(tuple3[2]) == tuple:
            return Expr(tuple3[0],buikdExprTree(tuple3[1]) , buikdExprTree(tuple3[2]))
        else:
            print("tupe t3",type(tuple3[1]))






print("#--------------------  Task 7 --------------------------#")

exp1 = buikdExprTree(('add',('mul',2,3),10))
exp2 = buikdExprTree(('add',10,('mul',2,3)))
exp3 = buikdExprTree(('add',('sub',23,3),('mul',2,3)))
exp3 = buikdExprTree(('add',('sub',23,3),('mul',2,3)))


print(exp1)
print(exp2)
print(exp3)

print("repr",repr(exp1))
print("type : " ,type(exp1))



#
# temp = Expr('add',Expr('sub',4,1),3)
# print(temp.clean())


#--------------------  Task 8 --------------------------

class Exp(object):
    """A call expression in Calculator.

    >>> Exp('add', [1, 2])
    Exp('add', [1, 2])
    >>> str(Exp('add', [1, Exp('mul', [2, 3])]))
    'add(1, mul(2, 3))'
    """

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)


def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return


def calc_eval(exp):
    """Evaluate a Calculator expression.

    >>> calc_eval(Exp('add', [2, Exp('mul', [4, 6])]))
    26
    """
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


def calc_apply(operator, args):
    """Apply the named operator to a list of args.

    >>> calc_apply('+', [1, 2, 3])
    6
    >>> calc_apply('-', [10, 1, 2, 3])
    4
    >>> calc_apply('*', [])
    1
    >>> calc_apply('/', [40, 5])
    8.0
    """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer / denom

    if operator in ('compl' , '!'):
        # print(operator)
        if len(args) != 1:
            raise TypeError(operator + 'compl requires exactly 1 arguments')
        elif type(args[0]) != int:
            raise TypeError(str(args[0])+ "is not <class int>")
            print("NOTT")
        # print("args yo: " , list(args))
        else:
            return int("".join( ( map( lambda x: str (9 - int(x)), list(str(args[0]))) ) ) )


# Parsing

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree


def tokenize(line):
    """Convert a string into a list of tokens.

    >>> tokenize('add(2, mul(4, 6))')
   return : ['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
    """
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.strip().split()


known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/','compl','!']


def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens.

    Operand expressions can be separated by commas, spaces, or both.

    >>> analyze(tokenize('add(2, mul(4, 6))'))
    Exp('add', [2, Exp('mul', [4, 6])])
    >>> analyze(tokenize('mul(add(2, mul(4, 6)), add(3, 5))'))
    Exp('mul', [Exp('add', [2, Exp('mul', [4, 6])]), Exp('add', [3, 5])])
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    elif token[-1] in ('h' , 'b' , 'q'):
        base = token[-1]
        if base == 'h':
            intbase = 16

        elif base == 'b':
            intbase = 2

        else:
            intbase = 8

        # print("newbase : ",intbase , "token : " , token)
        newtoken = token[:len(token) - 1]

        return int(newtoken,intbase)


    else:
        raise SyntaxError('unexpected ' + token)


def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands


def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token.

    >>> analyze_token('12')
    12
    >>> analyze_token('7.5')
    7.5
    >>> analyze_token('add')
    'add'
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


def run():
    read_eval_print_loop()


run()

print("#--------------------  Task 8--------------------------#")

# print(int('1af',16))

# test = "toli"
# print(test[-1])
# test = test[:len(test) - 1]
# print(test)



# num = 12083
# print(num)
# print(list(str(num)))
#
# name="toli"
#
# temp = "-".join(name)
# print(temp)

# compzl =   int("".join( ( map( lambda x: str (9 - int(x)), list(str(num))) ) ) )
# print(compzl)

# compzl = int ("".join())
# print(compzl)


# def test():
#     thelist = {"1":"1"}
#     def test2():
#
#         thelist['1']='2'
#     test2()
#     print(thelist)
#
#
# test()
#
# def test3():
#     num = 1
#     def test4():
#         nonlocal num
#         for i in range(4):
#             num +=1
#     test4()
#     print(num)
#
#
# test3()