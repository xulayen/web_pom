from datetime import datetime,date,time
import random
import os
import sys
import math
class Box1():
    def  __init__(self):
        self.lenght = 0
        self.width = 0
        self.height = 0

tt=datetime.now()
print(datetime.date(datetime.now()))
print(datetime.time(datetime.now()))
print(datetime.strftime(tt,"%Y-%m-%d %H/%M/%S"))


print(random.random())
print(random.uniform(2,5))
print(os.environ)
print(os.getcwd())
print(os.system('cd ..'))
if sys.platform.startswith('win32'):
    print()
elif sys.platform.startswith('linux'):
    print()
else:
    pass

r=-5.5
print(math.trunc(r))
print(math.fabs(r))
print(round(r))

