#Without pastrami: Using the list of sandwich_orders from Exercise 7-8, follow the 
# so that the value ‘pastrami’ occurs in the list at least three times. 
# Add the code to the beginning of the program to output a message that pastrami is no more, and write 
# while loop to remove all occurrences of ‘pastrami’ from sandwich_orders. Make sure that 
# in finished_sandwiches, the value ‘pastrami’ does not occur once.

sandwich_orders=['pig','pastrami','cocorel','pastrami','vegan','pastrami','cheese']
print("Sorry,pastrami are nothing :(")
finished_sandwich=[]
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwiches=sandwich_orders.pop()
    print("I made your "+sandwiches+" sandwich.")
    finished_sandwich.append(sandwiches)
print("\nSandwiches are complete:")
for finish in finished_sandwich:
    print(finish.title())
