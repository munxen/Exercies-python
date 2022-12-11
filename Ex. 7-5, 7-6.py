#Cinema tickets: the cinema has set several options for ticket prices depending on the age of the visitor. 
# For visitors under 3 years old, the ticket is free; at the age of 
# from 3 to 12, a ticket costs $10; finally, if the visitor's age is more than 12, the ticket costs $15.
# Write a loop that prompts the user to enter the age and outputs the ticket price.
# Three ways out: Write an alternative version of Exercise 7-4 or Exercise 7-5, 
# in which each item of the following list occurs at least once.
# Completion of the loop to check the condition in the while command.
# Control the duration of the cycle depending on the active variable.
# Exit the loop by the break command if the user enters the value ‘quit'.

message="\nPlease, tell you age "
age=" "
while age != "quit":
    age=input(message)
    age=int(age)
    if age <3:
        print("Price 0$")
    elif age >2 and age<12:
        print("Price 10$")
    else:
        print("Price 15$")