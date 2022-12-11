#Table order: write a program that asks the user how much 
#places he wants to book a table in a restaurant. If the entered number is greater than 8, output 
#a message that the user will have to wait. Otherwise, let us know, 
# that the table is ready.

table=input("How many tables you want a buy? ")
table=int(table)
if table>8:
    print("Sorry you have to wait.")
else:
    print("So good, come to me.")
