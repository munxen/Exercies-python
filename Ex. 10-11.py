#10-11. Favorite number: Write a program that asks the user for his favorite number. 
# Use the json.dump() function to save this number in a file.Write another program, 
# which reads this value and outputs the message: "I know your favorite number! It's _____."

import json
"""Requesting a favorite number"""
num = input ("Enter you liked num.\n")
filename = 'liked_num.json'
with open (filename , 'w') as f_obj:
    json.dump (num , f_obj)

"""Output a favorite number"""
filename = 'liked_num.json'
with open (filename) as number:
    liked_number = json.load (number)
print ("You liked number is " + liked_number)
