#User verification: latest version remember_me.py assumes that the user has either already entered his name, 
#or the program is running for the first time. It needs to be changed in case the current user is not 
# by the person who last used the program.Before outputting the greeting to greet_user(), 
# ask the user if the username is correctly defined. If the answer is negative, 
# call get_new_username() to get the correct username.

import json
def get_stored_username():
    """Retrieves the stored username, if it exists"""
    filename = 'username.json'
    try:
        with open (filename) as f_obj:
            username = json.load (f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Requests a new username"""
    username = input ("Enter your username\n")
    filename = 'username.json'
    with open (filename , 'w') as f_obj:
        json.dump (username, f_obj)
        return username

def greet_user():
    """Greets the user by name"""
    username = get_stored_username()
    if username:
        print ("Welcome back, " + username + ".")
    else:
        username = get_new_username()
        print ("We'll, you come back, " + username + ".")

def user_verification():
    """Checks whether the extreme user used the program the last time"""
    filename = 'username.json'
    with open (filename) as f_obj:
        username = json.load(f_obj)
        answer = input ( username + " - it's your username? (Enter yes/no)\n")
        if answer == 'yes':
            greet_user()
        else:
            get_new_username()

user_verification()