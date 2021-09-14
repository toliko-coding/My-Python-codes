# -------------[ 1 ]------------------------------------------------------------------------------------
'''
function that recive date and seconds , and print new date with the addition
of the seconds , in addiction the function print with conditions
like if added days , of if the date is exactly some hour
'''
def printLandingTime(hour,min,sec,time):
    #Arrguments Check
    if hour > 24 or hour < 0 or  min > 60 or min < 0 or sec > 60 or sec < 0:
        if hour > 24 or hour < 0:
            print("Error - invalid Hour Arrgiment")
        if min > 60 or min < 0:
            print("Error - invalid Minuts Arrgument")
        if sec > 60 or sec < 0:
            print("Error - invalid Seconds Arrgumet")
    else:
        #count new time
        bigTime = hour * 3600 + min * 60 + sec + time

        #days
        days = int(bigTime / 86400)

        #newtime after days count
        bigTime = bigTime - days * 86400

        #new hours

        tempHour = float(bigTime / 3600)
        hour = int(tempHour)



        #new minutes

        tempMin = float(tempHour - hour)
        tempMin2 = float(tempMin * 60)
        min = int(tempMin2)



        #new Seconds

        tempi=bigTime / 60
        x = bigTime // 60
        y = tempi - x
        sec = int(y * 60)


        #prints conditions :

        if min == 0 or sec == 0:
            if min == 0 and sec ==0:
                if days > 0:
                   if hour < 1 :
                       print("{:02d} hour exatcly + {:02d} days".format(hour, days))
                   else:
                       print("{:02d} hours exatcly + {:02d} days".format(hour, days))
                else:
                    if hour == 1:
                        print("{:02d} hour exatcly ".format(hour))
                    else:
                        print("{:02d} hours exatcly ".format(hour))

            if min != 0 and sec == 0:
                if days > 0:
                  if hour == 1 and min == 1:
                      print("{} hour , {} minute + {} days" .format(hour,min, days))
                  elif hour == 1 and min != 1:
                      print("{} hour , {} minutes + {} days".format(hour, min, days))
                  elif hour != 1 and min == 1:
                      print("{} hours , {} minute + {} days".format(hour, min, days))

                else:
                    if hour == 1 and min == 1:
                        print("{} hour , {} minute".format(hour, min))
                    elif hour == 1 and min != 1:
                        print("{} hour , {} minutes".format(hour, min))
                    elif hour != 1 and min == 1:
                        print("{} hours , {} minute".format(hour, min))

            if min == 0 and sec != 0:
                if days > 0:
                    if hour == 1 and sec == 1:
                        print("{} hour , {} second + {} days".format(hour, sec, days))
                    elif hour == 1 and sec != 1:
                        print("{} hour , {} seconds + {} days".format(hour, sec, days))
                    elif hour != 1 and sec == 1:
                        print("{} hours , {} second + {} days".format(hour, sec, days))
                else:
                    if hour == 1 and sec == 1:
                        print("{} hour , {} second".format(hour, sec))
                    elif hour == 1 and sec != 1:
                        print("{} hour , {} seconds".format(hour, sec))
                    elif hour != 1 and sec == 1:
                        print("{} hours , {} second".format(hour, sec))

        else:
            if days > 0:
                if hour == 1:
                    print(hour , " hour , " , end="")
                else:
                    print(hour , " hours , " , end="")

                if min == 1:
                    print(min , " minute , " , end="")
                else:
                    print(min , " minutes , " , end="")

                if sec == 1:
                    print(sec , " second " , end=" + ")
                else:
                    print(sec , " seconds " , end=" + ")

                print(days , "days")

            else:
                if hour == 1:
                    print(hour, "hour , ", end="")
                else:
                    print(hour, "hours , ", end="")

                if min == 1:
                    print(min, "minute , ", end="")
                else:
                    print(min, "minutes , ", end="")

                if sec == 1:
                    print(sec, "second")
                else:
                    print(sec, "seconds")











        #print("{:02d} hours , {:02d} minuts , {:02d} seconds , {:02d} days" .format(hour,min,sec , days))

#printLandingTime(2,17,54,0)

printLandingTime(23,5,0,10)
printLandingTime(0,0,0,177615)
printLandingTime(17,59,55,5)


# -------------[ 2 ]------------------------------------------------------------------------------------
'''
This function recive date and will print the previus day according to the mounth and the year '''

'''
def printPrevDay(day,mounth,year):
    def checkYear():
        if year % 400 == 0  or (year % 4 == 0 and year % 100 != 0):
            return 1

    if checkYear():
        if mounth == 3 and day == 1:
            print("{}/{}/{}".format(29, 2, year))
        else:
            if day == 1 or mounth == 1:
                if day == 1 and mounth == 1:
                    print("{}/{}/{}".format(31, 12, year-1))

                if day == 1 and mounth != 1:
                    mounth -= 1
                    print("{}/{}/{}".format(31, mounth, year))
            else:
                print("{}/{}/{}".format(day-1, mounth, year))
    else:
        if mounth == 3 and day == 1:
            print("{}/{}/{}".format(28, 2, year))
        else:
            if day == 1 or mounth == 1:
                if day == 1 and mounth == 1:
                    print("{}/{}/{}".format(31, 12, year-1))

                if day == 1 and mounth != 1:
                    mounth -= 1
                    print("{}/{}/{}".format(31, mounth, year))
            else:
                print("{}/{}/{}".format(day-1, mounth, year))



printPrevDay(11,7,2021)
printPrevDay(1,3,2012)
printPrevDay(1,3,2015)
printPrevDay(1,8,2021)
printPrevDay(1,1,2021)
'''

# -------------[ 3 ]------------------------------------------------------------------------------------
'''
Boolean function that return true if the index's of the number are in order of odd and then even or even and then odd
'''
'''
def ofOrder(num):
    if num <= 0:
        print("this number in negative !")
    else:
        flag = True
        while num != 0:
            n1 = num % 10
            num = num // 10
            n2 = num % 10

            #print(n1 , num , n2)
            if n2 == 0:
                return flag
            else:

                if n1 % 2 == 0 and n2 % 2 == 0:
                    flag = False
                if n1 % 2 != 0 and n2 % 2 != 0:
                    flag = False
        return flag
    
    #test
print(ofOrder(12345))
print(ofOrder(1573))
print(ofOrder(2785))
print(ofOrder(1))
print(ofOrder(11))

'''
# -------------[ 4 ]------------------------------------------------------------------------------------
'''
function that prints dimond shape figure of number 1 to 9 accoirding to the value that
enterd
'''
'''
def printFigure(num):
    if num > 19 or num < 1:
        print("EROOR - number must be in range of 1 to 19")
    elif num % 2 == 0:
        print("ERROR - number must be ODD")

    else:
        count = 1
        inline = -1
        rows = num // 2 + 1
        #top + mid
        for i in range(rows):

            print(' '*(rows-i-1),end='')
            inline = inline + 2
            for j in range(inline):
                print(count , end='')
                count +=1
                if count > 9:
                    count = 1
            print(end='\n')

        #bot
        inline = num - 2
        rows = num // 2
        for i in range(rows):
            print(' '*(i+1),end='')
            for j in range(inline):
                print(count , end='')
                count += 1
                if count > 9:
                    count = 1
            inline = inline - 2
            print(end='\n')



    #test

printFigure(9)
'''
# -------------[ 5 ]------------------------------------------------------------------------------------
'''
recursoin function that prints the numbers between given range accoirding to the 
"jumps"
'''
'''
def printRange(start,end= -1 ,jump=1):

    if end == -1:
        printRange(0,start,jump)

    if start < end and jump < 0:
        return 0

    if start > end and jump < 0: # 20 , 6 , -3
        print(start)
        printRange(start + jump,end,jump)
    elif start < end:
        print(start)

        printRange(start + jump, end, jump)


    else:
        return 1



    #test

printRange(6,20,3)
print("\n")
#printRange(6,20,-3)  --  0
printRange(20,6,-3)
print("\n")
printRange(6,10)
print("\n")
printRange(6)

'''


# -------------[ 6 ]------------------------------------------------------------------------------------
'''
function take 2 arrguments and return new number that
is the Appearance of the first number secend number times

'''
'''
def doRepeat(num,rNum=1):
    if rNum == 0:
        return 0
    if rNum == 1:
        return num
    else:
        return doRepeat(num,rNum-1) * 10 + num


    #test

print(doRepeat(3,5))
print(doRepeat(7,2))
print(doRepeat(7))
print(doRepeat(7,0))

'''

# -------------[ 7 ]------------------------------------------------------------------------------------

'''
funtion that return positive number bettewn 1 to 9 that is the sum of the arrgument , if the number
is not between 1 to 9 it do the sum again 
'''
'''
def sumDigits(num):
    if num == 0:
        return 0
    else:
        return sumDigits(num//10) + num % 10

#print(sumDigits(1589))

def calcNumValue(num):
    if num < 10 and num > 0:
        return num

    else:
       return calcNumValue(sumDigits(num))

    #test

print(calcNumValue(15))
print(calcNumValue(5))
print(calcNumValue(1))
print(calcNumValue(15893476987))
'''
# -------------[ 8 ]------------------------------------------------------------------------------------
'''
function that take argument and return value that is the reverse of the number
'''
'''

def pwr(base,ex):
    if ex == 0:
        return 1
    else:
        return base * pwr(base,ex-1)

def countDigits(num):
    if num == 0:
        return 0
    else:
       return countDigits(num//10) + 1

#print(countDigits(123456))

def doReverse(num):
    if num <= 0 :return 0
    if countDigits(num) == 1:
        return num
    else:
        x = num % 10 * pwr(10,countDigits(num//10))

        return doReverse(num//10) + x

    #test
print(doReverse(12345))
print(doReverse(5))
print(doReverse(726451))
print(doReverse(0))
print(doReverse(-1))

'''
