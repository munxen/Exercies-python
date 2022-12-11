#-1. Restaurant: Create a class named Restaurant. The __init__() method of the Restaurant class 
# must contain two attributes: restaurant_name and cuisine_type. Create the method descripe_restaurant(), 
# which outputs two attributes, and the open_restaurant() method, which outputs a message that the restaurant 
# is open.

class Restaraunt():
    def __init__(self,restaraunt_name,cuisine_type):
        """A simple restaurant model"""
        self.restaraunt_name=restaraunt_name
        self.cuisine_type=cuisine_type
    def describe_restaraunt(self):
        """What is the cuisine in the restaurant"""
        print("Restaraunt is " + self.cuisine_type.title() + " kitchen.")
    def open_restaraunt(self):
        """Restaurant is opened"""
        print("Restaraunt " + self.restaraunt_name.title() + ". Welcome!")
my_rest=Restaraunt("Coffe Set","european")
my_rest.describe_restaraunt()
my_rest.open_restaraunt()

