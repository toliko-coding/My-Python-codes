# ------------------------------------------------
#print(55/0)
#
#Traceback (most recent call last):
#  File "<pyshell#22>", line 1, in <module>
#    print(55/0)
#ZeroDivisionError: division by zero
# ------------------------------------------------
#a = []
#print(a[5])
#
#Traceback (most recent call last):
#  File "<pyshell#24>", line 1, in <module>
#    print(a[5])
#IndexError: list index out of range
# ------------------------------------------------
#tup = ('a', 'b', 'd', 'd')
#tup[2] = 'c'
#
#Traceback (most recent call last):
#  File "<pyshell#26>", line 1, in <module>
#    tup[2] = 'c'
#TypeError: 'tuple' object does not support item assignment
# ------------------------------------------------
def fileO():
    filename = input('Enter a file name: ')
    try:
        f = open (filename, "r")
    except:
        print('There is no file named', filename)
# ------------------------------------------------
#fileO()

# ------------------------------------------------
def get_age():
    age = int(input('Please enter your age: '))
    if age < 0:
        raise ValueError('%s is not a valid age' % age)
    return age
# ------------------------------------------------
def func():
    try:
        x=int(input('Enter number: '))
        if x%2!=0:
            raise ValueError('Not Even {}'.format(x))
        y=80//x
        a=[1,2,3,4,5,6,7,8,9,0]
        a[y]=100
    except ZeroDivisionError:
        print('Zero Division')
    except ValueError:
        print('Value Error')
    except:
        print('Other Error')
    else:
        print('No Error')
    finally:
        print('End')
# ------------------------------------------------
func()
'''
>>> func()
Enter number: 0
Zero Division
End
>>> func()
Enter number: 5
Value Error
End
>>> func()
Enter number: 4
Other Error
End
>>> func()
Enter number: 16
No Error
End
>>> 
'''
