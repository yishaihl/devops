#open() Parameters
#'r'	Open a file for reading. (default)
#'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
#'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
#'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
#'t'	Open in text mode. (default)
#'b'	Open in binary mode.
#'+'	Open a file for updating (reading and writing)

#Write to file function
#My_File = open("/Users/yishaihalpert/Desktop/test.txt", 'r+')
#My_File.write('abc')
#Add the content to vairable file
#Content = My_File.read()
#print(Content)

#Close the file after using it
#My_File.close()

#Select encoding
#f = open("/Users/yishaihalpert/Desktop/test.txt", mode = 'r', encoding='utf-8')

#Exceptions Handling
#try:
#    My_File = open("/Users/yishaihalpert/Desktop/test2.txt", 'r+')
#    Content = My_File.read()
#except IOError:
#    print("Error")
#print("123")

#Additional exception print data - the exception + more clear error for the user
#try:
#    My_File = open("/Users/yishaihalpert/Desktop/test2.txt", 'r+')
#    Content = My_File.read()
#except IOError as x:
#    print("Error")
#    print(x)
#print("123")

#Finaly - when you want to crash the proram after error handling

#try:
#    My_File = open("/Users/yishaihalpert/Desktop/test2.txt", 'r+')
#    Content = My_File.read()
#except IOError as x:
#    print("Error")
#    print(x)
#print("123")
#finally:
#    print("Finally")
