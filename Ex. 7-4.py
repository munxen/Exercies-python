#7-4. Pizza add-ons: Write a loop that prompts the user to enter 
# pizza add-ons until the 'quit’ value is entered. 
# When entering each supplement, print a message stating that this supplement is included in the order.

message="\nDo you take in pizza? "
take=" "
while take != "quit":
    take=input(message)
    if take=="quit":
        print("goodbye!")
    else:
        print("OK, "+take+" taked in you pizza!")
  
    

