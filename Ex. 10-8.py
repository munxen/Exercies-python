#Cats and dogs: create two files with names cats.txt and dogs.txt . Save at least three cat names 
# in the first file and three dog names in the second. Write a program that tries to read these files and 
# displays their contents on the screen. Enclose your code in a try-except block to catch an exception 
# FileNotFoundError and output a clear message about the absence of the file. Move one of the files to another 
# the location of the file system; make sure that the code of the except block is executed as expected.

"""Create two variables and assign them the name of the files"""
filename_cat = 'cats.txt'
filename_dog = 'dogs.txt'
"""We prevent an error if the file fails to be found. Along 
the way, we open and read the contents of the files"""
try:
    with open (filename_cat, 'r') as cats_obj:
        print("\nCats: \n" + cats_obj.read())
except FileNotFoundError:
    msg_1="Sorry, the file " + filename_cat + " does not exist."
    print (msg_1)
try:
    with open (filename_dog, 'r') as dogs_obj:
        print("\nDogs: \n" + dogs_obj.read()) 
except FileNotFoundError:
    msg_2="Sorry, the file " + filename_dog + " does not exist."
    print (msg_2)