
#-----------------------------------------------------------------------
#                                                                       #
# ----- # ----- # ----- KOT ANATOLI --- 324413756 ---- # ----- # ------ #
#                                                                       #
#-----------------------------------------------------------------------

from functools import reduce


"dispatch fucntion that make numeber : base^pwr"
def make_power(base,pwr):
    def dis(choose):
        if choose == 0 :
            return base
        elif choose == 1:
            return pwr
        else:
            return 'ERROR'

    return dis

"return the base of the make_power number"
def base(num):
    return num(0)

"return the power of the make_power number"
def power(num):
    return num(1)

"printing the power of the make_power number"
def print_power(num):
    if power(num) == 1:
        print(base(num))
    elif power(num) == 0:
        print(1)
    else:
        print(str(base(num)) + "^" + str(power(num)))

"function that calculating the result of the base^power"
def calc_power(num):
    return  base(num)**power(num)

"function that try to improve the base of the make_power number by trying to decrease the base and increase the power"
def improve_pwr(num):


    """Recursicve way to solve imporve_power ( not alyaws works) """
    # newb = 1
    # newp = 1
    # for i in range (base(num)):
    #     if i * i == base(num):
    #         newb = i
    #         newp = power(num) * 2
    #         temp = make_power(newb,newp)
    #         return improve_pwr(temp)
    #
    # return num

    """better way that works alyaws"""
    n = calc_power(num) # 81
    newbase = 2
    pwr = 2 #3 # 4


    while True :
        if newbase ** pwr == n:
            return make_power(newbase,pwr)

        else:

            if newbase ** pwr > n:
                newbase +=1
                pwr = 2

            if newbase ** pwr < n:
                pwr += 1

            if newbase >= base(num)  or newbase > n//3:
                False


    return num


"function that return new make_power number that is the mix of two numbers"
def mul_power(x,y):
    if base(x) == base(y):
        return make_power(base(x) , power(x) + power(y))

    else:
        return make_power(calc_power(x) * calc_power(y),1)

"function that returns the division of two make_power numbers"
def div_power(x,y):
    if base(x) == base(y):
        return make_power(base(x),power(x) - power(y))

    else:
        return improve_pwr(make_power(calc_power(x) // calc_power(y) , 1))



print("-------------- #### TASK 1 ### ----------------")
x = make_power(4,5)
print('x :',x)
print('base x :' ,base(x))
print('pwr x :' ,power(x))
print("print_power(x): ")
print_power(x)
print("improved : ")
print_power(improve_pwr(x))
print("print_power(mul_power(improve_pwr(x),make_power(2,5))) : ")
print_power(mul_power(improve_pwr(x),make_power(2,5)))
y = make_power(9,2)
print_power(improve_pwr(y))
print_power(mul_power(x,y))
print_power(mul_power(improve_pwr(y),make_power(3,5)))
print_power(div_power(improve_pwr(y), make_power(3, 5)))
print_power(div_power(mul_power(make_power(2,3),make_power(2,8)),make_power(2,4)))
print_power(div_power(mul_power(improve_pwr(make_power(8,1)),improve_pwr(make_power(256,1))),improve_pwr(make_power(16,1))))
print_power(make_power(12,1))
print_power(make_power(12,0))


# x = make_power(4,5)
# print_power(improve_pwr(x))

# y = make_power(9,2)
# print_power(improve_pwr(y))


# z = make_power(1024,1)
# print_power(improve_pwr(z))








#------------------- 2 -----------------

"dispatch function that create a node in a tree with two sons "
def make_tree(value,l=None,r=None):
    def dispatch(v):
        if v == 0 :
            return value
        if v == 1 :
            return l
        if v == 2:
            return r

    return dispatch

'''function that return the value of the node'''
def value(t):
    return t(0)

'''function that return the left node of the node'''
def left(t):
    return t(1)

'''function that return the right node of the node'''
def right(t):
    return t(2)

'''function that print the tree in inorder '''
def print_tree(t):
    if t is None:
        return

    else:
        print_tree(left(t))
        print(value(t),end='-')
        print_tree(right(t))
        return


'''function that return the amount of the appirence of the value'''
def count_value(t,val):
    if t is None :
        return 0

    elif value(t) == val:
        return 1

    else:
        return count_value(left(t),val) + count_value(right(t),val)

'''boolean function that return True if the tree is BST'''
def tree_BST(t):
    if t is None:
        return True

    if left(t) is not None:
        if value(left(t)) > value(t):
            return False

    if right(t) is not None:
        if value(right(t)) < value(t):
            return False

    if False in (tree_BST(left(t)) , tree_BST(right(t))):
        return False
    else:
        return tree_BST(left(t)) and tree_BST(right(t))



'''fucntio that return the depth of thre tree'''
def tree_depth(t):
    if t is None :
        return 0
    elif right(t) is None and left(t) is None:
        return 0
    else:
        l = tree_depth(left(t))
        r = tree_depth(right(t))

        return max(r,l) + 1


'''boolean fucntion that return True if in all the nodes , the left son is not bigger or smaller by 2 or more  in depth '''
def tree_balance(t):
    if t is None:
        return True

    if abs(tree_depth(left(t)) - tree_depth(right(t))) >= 1:
        return False

    else:
        return tree_balance(left(t)) and tree_balance(right(t))

    return False

print("-------------- #### TASK 2 ### ----------------")
tree1=make_tree(12,make_tree(6,make_tree(8,None,None),None),make_tree(7,make_tree(8,None,None),make_tree(15,None,None)))
print("TREE number 1 : ")
print(tree1)
print(value(tree1))
print(value(left(tree1)))

tree2=make_tree(12,make_tree(6,make_tree(3,make_tree(1,None,None),None),make_tree(8,make_tree(7,None,None),None)),make_tree(15,None,make_tree(20,make_tree(17,None,
None),None)))
print("TREE number 2 : ")
print(tree2)
print(value(right(left(tree2))))

print('print_tree(tree1) : ')

print_tree(tree1)
print()
print("print_tree(tree2) : ")
print_tree(tree2)
print()

print("Count Value 8 in tree1:")
print(count_value(tree1,8))


print("tree_BST :")
print(tree_BST(tree1))
print(tree_BST(tree2))

print("tree_depth :")
print(tree_depth(tree1))
print(tree_depth(tree2))

print("tree_balance :")
print(tree_balance(tree1))
print(tree_balance(tree2))






# -------------- 3 ----------------


#A
print("-------------- #### TASK 3 ### ----------------")

products = (('p1',1000),('p2',2000),('p3',5000),('p4',100))
sales = (('s1',0.2),('s2',0.3),('s3',0.1))

'''function that return dict of all the product after the sale according to the sale in the store list'''
def get_prices(sName,prod,sale):

    return tuple(map(lambda x : (x[0] , x[1] - (x[1] *  dict(sale)[sName])),prod))
print("A:")
print(get_prices('s1',products,sales))




#B
prod_dict = dict(products)
sale_dict = dict(sales)
'''function that return dict of all the product after the sale according to the sale in the store list'''
def get_prices_dict(sName,prod_dict,sale_dict):


    return dict(map(lambda x : (x[0] , x[1] - ( x[1] * sale_dict[sName])) , tuple(map(lambda x : x , prod_dict.items()  )) ) )

print("B:")
print(get_prices_dict('s1',prod_dict,sale_dict))




#C
sales = {'s1':{'t1':0.2, 't2':0.1}, 's2':{'t1':0.1, 't2':0.2},'s3':{'t1':0.3, 't2':0.5}}
types = {'t1':('p2', 'p4'), 't2':('p1', 'p3')}


def get_prices_by_type(sName, prod_l , sale , type):
        pass
        #i didnt manage to make it
        #print(sale[sName])
        #return list(map(lambda x :x , prod_l.items()))
        return tuple(map(lambda x:(x[0] , x[1]) , type.items()))



print("C:")
print(get_prices_by_type('s1', prod_dict, sales, types))


#D
def add(a,b):
    return a+b
'''function that return the total price of all the product with the sale according to the store and the type '''
def accumulate_prices(sName,prod_l,sale,type,func):
    return reduce(func , get_prices_by_type(sName,prod_l,sale,type).values())

# print("D:")
# print(accumulate_prices('s1', prod_dict, sales, types, add))







# ---------------- 4 --------------------------
"function that increade or decreace char by 1"
def inc_dec_char(char,num):
    start = 'a'
    end = 'z'
    if num < 0 :
        if char == end:
            return start
        else:
            temp = bytes(char , 'utf-8')
            temp = temp[0] + 1
            return chr(temp)

    else :
        if char == start:
            return end
        else:
            temp =bytes(char,'utf-8')
            temp = temp[0] - 1
            return chr(temp)



"function that increace or decreace the char num times"
def change_char(char,num):
    c = char
    if num < 0 :
        num = num * -1
        for _ in range(num):
            c = inc_dec_char(c , num)

    else:
        for _ in range(num):
            c = inc_dec_char(c , num)

    return c


"dispatch function with message passing to make encoding or decoding according to given keys "
def coding():
    theDic = {'reverse_word' : False, 'reverse_string' : False}
    theKey = theDic


    def dis(msg,args=None):

        '''message passing key to export the current encoding key'''
        if msg == 'export_key':
            nonlocal theKey
            if len(theKey) == 2:
                return "empty key"

            return theKey

        '''message passing key to set the given encoding key'''
        if msg == 'set_key':
            f1 = False
            f2 = False
            if args[1] == 'yes':
                f1 = True
            if args[2] == 'yes':
                f2 = True

            theKey = theDic
            theKey['reverse_word'] = f1
            theKey['reverse_string'] = f2

            if args[0] != 0 :
                temp = {'a' : 'a',
                      'b' : 'b',
                      'c' : 'c',
                      'd' : 'd',
                      'e' : 'e',
                      'f' : 'f',
                      'g' : 'g',
                      'h' : 'h',
                      'i' : 'i',
                      'j': 'j',
                      'k': 'k',
                      'l': 'l',
                      'm': 'm',
                      'n': 'n',
                      'o': 'o',
                      'p': 'p',
                      'q': 'q',
                      'r': 'r',
                      's': 's',
                      't': 't',
                      'u': 'u',
                      'v': 'v',
                      'w': 'w',
                      'x': 'x',
                      'y': 'y',
                      'z': 'z',}

                temp = dict(map(lambda x : (x[0] , change_char(x[1] , args[0]) ), temp.items()))
                theKey.update(temp)
                print('DONE - set of new key')

            else:

                import random
                myrandom = random.randint(-26,26)
                dis('set_key',(myrandom,args[1] , args[2]))


        '''message passing key to make the key empty'''
        if msg == 'empty_key' :
            theKey = 'empty key'
            print("Done - the key now is empty")


        '''message passing key to update the current key to new key that given as arrgument'''
        if msg == 'import_key':
            if type(args) == type(theKey):
                theKey = args
                print('DONE - new key is imported and updated')
            else:
                print("Error : The key must be a Dict type value ")


        '''message passing key to encode the value that given according to the key'''
        if msg == 'encoding':
            if len(theKey) == 2 :
                return "The key is empty , please set key"

            print("Encoding the Message ..")
            temp =[]
            temp2=[]
            for char in args:
                temp.append(char)

            for char in temp:
                if char == ' ':
                    temp2.append(' ')
                else:
                    temp2.append(theKey[char])

            newstr =  reduce(lambda x,y:x+y , temp2)

            if theKey["reverse_word"] == True:
                rtemp = newstr.split()
                rtemp.reverse()
                newstr = reduce(lambda x,y : x + ' ' + y , rtemp)


            if theKey["reverse_string"] == True:
                rtemp = newstr.split()
                rt = []
                for word in rtemp:
                    rt.append(word[::-1])

                newstr = reduce(lambda x, y: x + ' ' + y, rt)

            return newstr


        '''message passing key to decode the arrgument that given according to current key'''
        if msg == 'decoding':

            print("decoding...")
            oldstr = args
            if len(theKey) == 2:
                return 'key empty'

            if theKey["reverse_string"] == True:
                rtemp = oldstr.split()
                rt = []
                for word in rtemp:
                    rt.append(word[::-1])
                oldstr = reduce(lambda x, y: x + ' ' + y, rt)

            if theKey['reverse_word'] == True:
                rtemp = oldstr.split()
                rtemp.reverse()

                oldstr = reduce(lambda x, y: x + ' ' + y, rtemp)
                #print('After reverse words')
                #print(oldstr)

            reverseDict = {value:key for key ,value in theKey.items()}
            listo = []
            listo2 = []
            for char in oldstr:
                listo.append(char)
            for char in listo:
                if char == ' ':
                    listo2.append(' ')
                else:
                    listo2.append(reverseDict[char])

            oldstr = reduce(lambda x,y : x + y , listo2)
            return oldstr

    return dis



print("----------- 4 -------------")

code1 = coding()
code1('set_key',(0,'yes','yes'))
key = code1('export_key')
print('the key is :')
print(key)


cstr = code1('encoding','the london is the capital of great britain')
print(cstr)

dstr = code1("decoding",cstr)
print("decoding message :")
print(dstr)

code2= coding()
dstr = code2("decoding",cstr)
print(dstr)

code2("import_key" , key)
dstr = code2("decoding" , cstr)
print(dstr)

code2("empty_key")
print(code2("export_key"))





# ------------------------ 5 -----------------------
'''function that create a parking place with hour payment + how many places in each parking type , return dict with message passig to functions'''
def parking(payment,f1,f2,f3):
    print("parking is created :)")
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
            nonlocal count

            if count >= len(cars):
                count = 0

                return True
            else:
                return False


        def next():
            nonlocal count
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



print("-------------- #### TASK 5 ### ----------------")
park1 = parking(10,3,3,3)
park1["start_parking"](222,"Regular")
park1["start_parking"](223,"Regular")
park1['next_time']()
park1["start_parking"](224,"Regular")
park1["start_parking"](225,"Regular")

park1["start_parking"](225,"VIP")
prn= park1["print_list"]()
print(prn)
while not prn['end']():
    prn['next']()
park1["print_parking"]("VIP")
park1["end_parking"](100)
park1["end_parking"](223)
park1["print_parking"]("Regular")




















