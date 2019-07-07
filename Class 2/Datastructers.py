#Import the entire module

#import datetime
#print(datetime.datetime.now())

#Short call for class into module

#from datetime import datetime
#print(datetime.now())

#Data structures - Array

#import array as arr
#a = arr.array("i",[3,6,9])

# Change existing value in specific index

#import array as arr
#a = arr.array("i",[3,6,9])
#a[0] = 5

# Get a value from specific index

#import array as arr
#a = arr.array("i",[3,6,9])
#print(a[0])

# Adding an element

#import array as arr
#a = arr.array("i",[3,6,9])
#a.append(111)

#Removing an element

#import array as arr
#a = arr.array("i",[3,6,9])
#a.pop(0)

#Adding an element to a specific index

#import array as arr
#a = arr.array("i",[3,6,9])
#a.insert(1,7)

# Get array size (number of elements)

#import array as arr
#a = arr.array("i",[3,6,9])
#print(len(a))

#Iterating the array and getting all elements

#import array as arr
#a = arr.array("i",[3,6,9])
#for temp_num in a:
#    print(temp_num)

#Iterating the array and getting all elements with index

#import array as arr
#a = arr.array("i",[3,6,9])
#for i in range(len(a)):
#    print(a[i])

#Data structures - List

#my_list = [5,"a",True]
#print(len(my_list))

#my_list = [5,"a",True]
#for temp_num in my_list:
#    print(temp_num)
#Data structers - Tuple

#x_tuple = 1,2,3,4,5
#y_tuple = ('a','b','c','d')
#for temp_num in x_tuple:
#    print(temp_num)

#x_tuple = 1,2,3,4,5
#y_tuple = ('a','b','c','d')
#for temp_num in y_tuple:
#    print(temp_num)

#Data structures - Dictionary

my_dictionary = {'A':1, 'B':2, 'C':3, 'D':4}

#my_dictionary['A'] = 5

# Print keys

#print(my_dictionary.keys())

# Print values

#print(my_dictionary.values())

?#for key in my_dictionary.items():
#    print(key)