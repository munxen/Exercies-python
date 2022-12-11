#Guestbook: Write a while loop that asks users for names in the loop. 
# When you enter each name, display a greeting on the screen and add a line with a message to the file
# with the name guest_book.txt . Make sure that each message is placed in a separate line of the file.

"""Creating a simple loop with a lever"""
a = 1
while a == 1:
    """We ask the user for his data, we mention that if he writes stop, the program will close"""
    answer = input ("Enter you name\n")
    print ("Enter 'stop' for exit\n")
    if answer == 'stop':
        a = 0
    """We write the user's data to the variable and give the command to create a text
file and write the data there"""
    name = "There was a " + answer.title() + "."
    filename = "guest_book.txt"
    with open (filename , "a") as file_object:
        file_object.write (name +"\n")
    print ("Your name is added to book!\n")
