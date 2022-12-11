#Slices: Add to the end of one of the programs written in this chapter a fragment that does the following.
# Outputs the message "The first three items in the list are:", and then uses a slice to output the first 
# three items from the list.
# Outputs the message "Three items from the middle of the list are:" and then uses a slice to output 
# of the first three items from the middle of the list.
# Displays the message "The last three items in the list are:" and then uses a slice to output the latest 
# three items from the list.

names=['tom','bob','tim','john','mike','elizabet','antonuo','rick']
print("The first three items in the list are: " + str(names[:3]))
print("Three items from the middle of the list are: " + str(names[4:7]))
print("The last three items in the list are: " + str(names[-3:]))
