
def displayNumType(num):
    print('num ',end='')
    print(num,end='')
    print(' is ',end='')
    if type(num) == type(0):
        print('an integer')
    elif type(num) == type(0):
        print ('a long')
    elif type(num) == type(0.0):
        print ('a float')
    elif type(num) == type(0+0j):
        print ('a complex number')
    else:
        print ('not a number at all!!')
def isInt(num):
    if isinstance(num,(int)):
        print('yes')
    else: 
        print('no')

import random

s='abcde'
i = -1
for i in [None]+range(-1, -len(s), -1):
    print(s[:i])

a=random.random()
print(a)
Num=2.0
isInt(Num)
displayNumType(Num)
print("end")