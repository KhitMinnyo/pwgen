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
                sys.stdout=open("WORDlist.txt","w")
                print(cap*x + small*y )
                sys.stdout.close()

def LowerToUpper():
    for cap in lstCaptial:
        for small in lstSmall:
                sys.stdout=open("wordLIST.txt","w")
                print(small*y + cap*x) 
                sys.stdout.close()


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



    

        
        
