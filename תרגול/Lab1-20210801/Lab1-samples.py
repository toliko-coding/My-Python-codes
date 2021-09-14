# ----------------------------------------------------------
# Sample 1 

# 2 3.14159265359 abcd!@#$
# 5.14159265359 15.93480220054533 1 3
# a=2, b=3.14159265359, c=abcd!@#$ next b=3.14 end
#     2,3.1416    ,abcd!@#$
"""
a,b,c = 2, 3.14159265359, 'abcd!@#$'
print(a,b,c)

n1,n2 = a+b, (b**a)/2.0+11
print(n1, n2, int(b//a), 15%4)

print('a={0}, b={1}, c={2} next'.format(a,b,c),'b={0:.2f} end'.format(b))
print('{0:>5d},{1:<10.4f},{2}'.format(a,b,c))
"""

# ----------------------------------------------------------
# Sample 2 - IF Sample

# Enter Number: -7
# Negative number
# Enter a One-Digit number: 89
# It's not a one-digit number
"""
num=int(input('Enter Number: '))

if num > 0:
    print('Positive number')

if num==0:
    print('Zero')
elif num>0:
    print('Positive number')
else:
    print('Negative number')

num=int(input('Enter a One-Digit number: '))

# num >= 0 and num < 10
if 0 <= num < 10:
    print('This one-digit number')
else:
    print("It's not a one-digit number")
"""

# ----------------------------------------------------------
# Sample 3 - Loop Sample

# Enter number[1-9]: 7
#
# 0123456
# -------
#       1
#      12
#     123
#    1234
#   12345
#  123456
# 1234567
# -------
# 7654321
# 1|2|3|4|5|6|7|
#

"""
# input number
n = int(input('Enter number[1-9]: '))
print()

# range(n) from 0 to n-1, step 1
for i in range(n):
    print(i,end='')
print()

# range(n) from 0 to n-1, step 1
for i in range(n):
    print('-',end='')
print()

# range(n+1) from 1 to n, step 1 
for i in range(1,n+1):

    # range(i) from 0 to n-i-1, step 1
    for j in range(n-i):
        print(end=' ')

    # range(i) from 1 to i-1, step 1
    for j in range(i):
        print(j+1,end='')
    print()

# range(n) from 0 to n-1, step 1
for i in range(n):
    print('-',end='')
print()

# range(n,0,-1) from n to 1, step -1
for i in range(n,0,-1):
    print(i,end='')

print()
i=1
while i <= n:
    print(i,end='|')
    i+=1
"""
