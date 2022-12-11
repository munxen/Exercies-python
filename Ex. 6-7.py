#People: Start with the program written for exercise 6-1 (p. 107). Create two 
#new dictionaries representing different people, and save all three dictionaries in the list 
#with the name people. Go through the elements of the list of people. In the process of iterating , output the entire 
#available information about each person.

user_0={
    'first_name':'marty',
    'last_name':'bird',
    'age':48,
    'city':'ozark'
    }
user_1={
    'first_name':'john',
    'last_name':'stetham',
    'age':39,
    'city':'manhetten'
    }
user_2={
    'first_name':'heissenberg',
    'last_name':'helensdor',
    'age':55,
    'city':'cicago'
    }
users=[user_0,user_1,user_2]
for user in users:
    print(user)