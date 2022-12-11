#10-5. Survey: Write a while loop in which the program asks the user why he likes programming. 
#Every time a user enters another reason, save the text of his answer in a file.

"""Creating a simple loop with a lever"""
a = 1
while a == 1:
    """We ask the user for his data, we mention that if he writes stop, the program will close"""
    answer = input ("Why your like to programming?\n")
    print ("Enter 'stop' for exit\n")
    if answer == 'stop':
        a = 0
    """We write the user's data to the variable and give the command to create a text
file and write the data there"""
    name = answer
    filename = "guest_answer.txt"
    with open (filename , "a") as file_object:
        file_object.write (name +"\n")
    print ("Your name is added to book!\n")
