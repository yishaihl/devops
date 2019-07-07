#1

first = "Hello"
second = "Yishai Halpert"
print(first + "\n" + second)

#2

x = 1000
y = 500
z = "The Sum of x & y is:"
print(z)
print(x + y)

#3

import sys
print('The Current Python Running Ver. Is: \n {}'.format(sys.version))

#4

x = "hello"
print(x [::-1])

#5

x = "hello"
print(len(x))



#6

from datetime import datetime

now = datetime.now()

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("The Current Date and Time Is:",date_time)

#7

x = 200
y = 270

if x > y:
    print("X is Bigger Then Y")
else:
    print("Y is Bigger Then X")

#8

x = 120
if (x > 5 and x < 200):
    print('MATCH')
else:
    print('Not MATCH')