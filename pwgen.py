#!python
#cython: language_level=2
##pwgen is Repeated Password Generating tool.
##pwgen is developed by KhitMinnyo from AiO.
#=====================================================================================#
#                                                                                     #
#       __/\__  | |/ / |__ (_) |_  |  \/  (_)_ __  _ __  _   _  ___     __/\__        #
#       \    /  | ' /| '_ \| | __| | |\/| | | '_ \| '_ \| | | |/ _ \    \    /        #
#       /_  _\  | . \| | | | | |_  | |  | | | | | | | | | |_| | (_) |   /_  _\        #
#         \/    |_|\_\_| |_|_|\__| |_|  |_|_|_| |_|_| |_|\__, |\___/      \/          #
#                                                        |___/                        #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#@@@@@@@@@@@@@  Instructor  @@@@@@@@@@@@@@ All in One Hacking Training  @@@@@@@@@@@@@@#
#*************** Viber 09 976 41 3560 && Mail khitminnyo@khitminnyo.com **************#
#######################################################################################

#pwgen Version info
#Version 1.1

import sys
lstCaptial = "ABCDEFGHIJKLMNOPQRSTUVWHYZ"
lstSmall = "abcdefghijklmnopqrstuvwhyz"
lstSpecial = "!@#$%^&*,."       # for further use (may be in the new version)
lstNum = "0123456789"           

x = input('Enter number of CAPITAL LETTERS that you want to repeat.  ')
y = input('Enter number of small letters that you want to repeat.  ')
n = input('Enter number of numbers 1234567890 that you want to repeat.  ')
# spe = input ('Enter number of special characters that you want to repeat.  ')


F = open('WORDlist.txt', 'w')
f = open('wordLIST.txt', 'w')

#Form 1(AAAAaaaa)
def UpperToLower():
    for cap in lstCaptial:
        for small in lstSmall:
                with open('WORDlist.txt', 'a') as f:
                    f.write(cap*x + small*y + '\n') 

#Form 2(aaaaAAAA)
def LowerToUpper():
    for cap in lstCaptial:
        for small in lstSmall:
                with open('wordLIST.txt', 'a') as f:
                    f.write(small*y + cap*x + '\n')

#Form 3(AAAAaaaa1111)
def UpperLowerNumber():
    for cap in lstCaptial:
        for small in lstSmall:
            for num in lstNum:
                with open('WORDlist111.txt', 'a') as f:
                    f.write(cap*x + small*y + num*n + '\n')

#Form 4(AAAA1111aaaa)
def UpperNumberLower():
    for cap in lstCaptial:
        for small in lstSmall:
            for num in lstNum:
                with open('WORD111list.txt', 'a') as f:
                    f.write(cap*x + num*n + small*y + '\n')

#Form 5(aaaa1111AAAA)
def LowerNumberUpper():
    for cap in lstCaptial:
        for small in lstSmall:
            for num in lstNum:
                with open('word111LIST.txt', 'a') as f:
                    f.write(small*y + num*n + cap*x + '\n') 


#Form 6(aaaaAAAA1111)
def LowerUpperNumber():
    for cap in lstCaptial:
        for small in lstSmall:
            for num in lstNum:
                with open('wordLIST111.txt', 'a') as f:
                    f.write(small*y + cap*x + num*n + '\n')

#Form 7(1111AAAAaaaa)
def NumberUpperLower():
    for cap in lstCaptial:
        for small in lstSmall:
            for num in lstNum:
                with open('111WORDlist.txt', 'a') as f:
                    f.write(num*n + cap*x + small*y + '\n')

#Form 8(1111aaaaAAAA)
def NumberLowerUpper():
    for cap in lstCaptial:
        for small in lstSmall:
            for num in lstNum:
                with open('111wordLIST.txt', 'a') as f:
                    f.write( num*n + small*y + cap*x  + '\n')                    


flag = True
while flag:
    zz = input('Which order do you want? 1(AAAAaaaa) 2(aaaaAAAA) 3(AAAAaaaa1111) 4(AAAA1111aaaa) 5(aaaa1111AAAA) 6(aaaaAAAA1111) 7(1111AAAAaaaa) 8(1111aaaaAAAA)   :  ')
    if zz == 1:
        flag = True
        UpperToLower()
        break
    elif zz == 2:
        flag = True
        LowerToUpper()
        break
    elif zz == 3:
        flag = True
        UpperLowerNumber()
        break
    elif zz == 4:
        flag = True
        UpperNumberLower()
        break
    elif zz == 5:
        flag = True
        LowerNumberUpper()
        break
    elif zz == 6:
        flag = True
        LowerUpperNumber()
        break
    elif zz == 7:
        flag = True
        NumberUpperLower()
        break
    elif zz == 8:
        flag = True
        NumberLowerUpper()
        break
    else:
        print("Please, type one number from 1 to 8 only. ")
