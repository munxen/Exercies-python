#4-11. My pizza, your pizza: Start with the program from exercise 4-1. Create a copy of the list with pizza types, 
# name it friend_pizzas. Then do the following.
# Add a new pizza to the original list.
# Add another pizza to the friend_pizzas list.
# Prove that there are two different lists in the program. Print the message "My favorite pizzas are:", 
# and then the first list in the for loop. Print the message "My friend's favorite pizzas are:" and then 
# the second list in the for loop. Make sure that each new pizza is in the appropriate list

pizza = ['pepperoni','cheese','margarita']
for piz in pizza:
    print ("I like " + piz + " pizza")
print ("I really love pizza!")
friend_pizzas=pizza[:]
pizza.append('banana')
friend_pizzas.append('chocolate')
print("My favorite pizzas are: ")
for my in pizza:
    print (my.title())
print("My friend favorite pizzas are: ")
for friend in friend_pizzas:
    print(friend.title())