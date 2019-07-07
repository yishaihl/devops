#A.1-3
x = 80
y = 120
if x > y:
    print("BIG")
else:
    print("SMALL")

#B.1-2
for x in range(5):
   print(x)

#C.1-3
season = 1
if season == 1:
    print("SUMMER")
elif season == 2:
    print("WINTER ")
elif season == 3:
    print("FALL")
elif season == 4:
    print("SPRING")

#D
# 10.

#E.1-5
Age = 32
Letter = "H"
Currency = 3.60
Flew = True
Apartment_Number = 10
print(Age)
print(Currency)
print(Flew)
print(Apartment_Number)
print(Currency + Age)

#F.1-2
A = input ("Please Enter Your Phone Number:")
print("The Phone Number Entered is :", A)

#G.1-2
def printHello():
    print("hello")
def calculate():
    print(5 + 3.2)

#H.1-2
def print_name(name):
    print(name)
def devide_number(number):
    print(number/2)

#I.1-2
def return_number(x,y):
    return x + y
def add_space(yishai, halpert):
    return yishai + " " + halpert

#J.1-2
import array as arr
a = arr.array("i",[3,6,9])
print(a)

#Challenges

#Pyramid shape

rows = 5
for i in range (0, rows):
    for j in range(0, i + 1):
        print("#", end=' ')
    print("\r")

# X Shape

N = 7
for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j -1) == i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')

#M.1-2

# I tried to do it with using nested function without success.

#def inputNumber():
#    n = int (input("Please Choose Number:"))
#    def sum():
#        nonlocal n
#        tot = 0
#        while (n > 0):
#            dig = n % 10
#            tot = tot + dig
#            n = n // 10
#    return sum()
#    print("The total sum of digits is:", tot)
#    sum()
#inputNumber()