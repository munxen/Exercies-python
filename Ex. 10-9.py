#10-9. Errors without notification: change the except block from Exercise 10-8 so that if there is no file 
# the program continued to work without notifying the user about the problem.

"""Create two variables and assign them the name of the files"""
filename_cat = 'cats.txt'
filename_dog = 'dogs.txt'
"""We prevent an error if the file fails to be found. Along 
the way, we open and read the contents of the files"""
try:
    with open (filename_cat, 'r') as cats_obj:
        print("\nCats: \n" + cats_obj.read())
except FileNotFoundError:
    pass
try:
    with open (filename_dog, 'r') as dogs_obj:
        print("\nDogs: \n" + dogs_obj.read()) 
except FileNotFoundError:
    pass