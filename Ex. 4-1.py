#Pizza: Remember at least three of your favorite varieties of pizza. Save them in the list and 
# use the for loop to output all the names.
#Change the for loop so that instead of a simple pizza name, a message is displayed that includes this name. 
# Thus, for each element, a string with a simple text like "I like pepperoni pizza" should be output.
# Add a line with the final message to the end of the program (after the for loop).Thus, the output should 
# consist of three (or more) lines with pizza names and an additional message, say, "I really love pizza!".

pizza = ['pepperoni','cheese','margarita']
for piz in pizza:
    print ("I like " + piz + " pizza")
print ("I really love pizza!")