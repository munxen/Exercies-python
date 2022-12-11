#Sandwiches: Write a function that gets a list of sandwich components. 
# The function must have one parameter for any number of values passed during the call 
# functions, and output a description of the ordered sandwich. Call the function three times with different 
# by the number of arguments.

def sandwiches(*toppings):
    print(toppings)
sandwiches("potato")
sandwiches("meat","peppers")
sandwiches("apples","bananas","chesse")