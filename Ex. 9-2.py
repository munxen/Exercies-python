#9-2. Three restaurants: Start with the class from Exercise 9-1. Create three different instances, 
# call the descripe_restaurant() method for each instance.

class Restaraunt():
    def __init__(self,restaraunt_name,cuisine_type):
        """A simple restaurant model """
        self.restaraunt_name=restaraunt_name
        self.cuisine_type=cuisine_type
    def describe_restaraunt(self):
        """Whats kitchen by restaurant"""
        print("Restaraunt is " + self.cuisine_type.title() + " kitchen.")
    def open_restaraunt(self):
        """Restaurant is opened"""
        print("Restaraunt " + self.restaraunt_name.title() + ". Welcome!")

rest1=Restaraunt("kimono","asian")
rest2=Restaraunt("coffe set", "european")
rest3=Restaraunt("groove","francian")
rest1.describe_restaraunt()
rest2.describe_restaraunt()
rest3.describe_restaraunt()