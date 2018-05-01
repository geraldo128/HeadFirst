
# datetime is the module,2nd datetime is the function/attribute imported from the module. the module is imported from the std lib

#from datetime import datetime
from os import getcwd

import datetime
import os


 #from sys import platform

import sys
#sys.platform





odds = [ 1, 3, 5, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35,
        37, 39, 41, 43, 45, 47, 49, 50,
        51, 53, 55, 57, 59 ]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("this minute seems a litte odd")
else:
    print("not an odd minute")

    where_am_I = getcwd()

    print(where_am_I)

    #whats_my_platform = platform()

print(sys.platform)
print(sys.version)
#print(os.getenv('Home'))

name = sys.version

print(name)

print(datetime.date.today())

print(datetime.date.today())


























