#10-12 Saved Favorite Number: Combine two programs from Exercise 10-11 into one file. 
# If the number is already saved, tell it to the user, and if not, request the user's favorite number 
# and save it to a file. Run the program twice to make sure it works.

import json

filename = 'liked_num.json'
try:
    with open (filename) as f_obj:
        number = json.load (f_obj)
except FileNotFoundError:
    print ("Sry, I didn't find your number.")
    number = input ("Enter you liked number\n")
    with open (filename,'w') as f_obj:
        json.dump (number , f_obj)
        print ("You liked number is " + number)
else:
    print ("You like number is " + number)