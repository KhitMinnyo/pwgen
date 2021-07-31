#!python
#cython: language_level=2
##pwgen is Repeated Password Generating tool.
##pwgen is developed by KhitMinnyo from AiO.

#pwgen Version info
#Version 1.0

import sys
lstCaptial = "ABCDEFGHIJKLMNOPQRSTUVWHYZ"
lstSmall = "abcdefghijklmnopqrstuvwhyz"
lstSpecial = "!@#$%^&*,."       # for further use (may be in the new version)
lstNum = "0123456789"           # for further use (may be in the new version)

x = input('Enter number of CAPITAL LETTERS that you want to repeat.  ')
y = input('Enter number of small letters that you want to repeat.  ')
def UpperToLower():
    for cap in lstCaptial:
        for small in lstSmall:
                print(cap*x + small*y )


def LowerToUpper():
    for cap in lstCaptial:
        for small in lstSmall:
                print(small*y + cap*x) 



flag = True
while flag:
    zz = input('Which order do you want? 1(AAAAaaaa) 2(aaaaAAAA) :  ')
    if zz == 1:
        flag = True
        UpperToLower()
        break
    elif zz == 2:
        flag = True
        LowerToUpper()
        break
    else:
        print("Please, type 1 or 2 only. ")



    

        
        
