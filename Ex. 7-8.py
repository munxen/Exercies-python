#7-8. Sandwiches: create a list named sandwich_orders, fill it with names 
# different types of sandwiches. Create an empty list named finished_sandwiches. In the loop 
#iterate through the elements of the first list and output a message for each element 
#(for example, "I made your tuna sandwich"). 
#After that, each sandwich from the first list is moved to the finished_sandwiches list. 
#After all the elements of the first list are processed, output a message listing all 
# made sandwiches.

sandwich_orders=['pig','cocorel','vegan','cheese']
finished_sandwich=[]
while sandwich_orders:
    sandwiches=sandwich_orders.pop()
    print("I made your "+sandwiches+" sandwich.")
    finished_sandwich.append(sandwiches)
print("\nSandwiches are complete:")
for finish in finished_sandwich:
    print(finish.title())
