#Ice cream kiosk: An ice cream kiosk is a special kind of restaurant. Write the IceCreamStand class, 
# inheriting from the Restaurant class from Exercise 9-1 (p. 165) or Exercise 9-4 (p. 169). Any one will do 
# class version; just choose the one you like best. Add an attribute named flavors for 
# storing a list of ice cream varieties. Write a method that outputs this list.
# Create an instance of IceCreamStand and call this method.

class Restaraunt():
    def __init__(self,restaraunt_name,cuisine_type):
        """A simple restaurant model"""
        self.restaraunt_name=restaraunt_name
        self.cuisine_type=cuisine_type
    def describe_restaraunt(self):
        """Whats kitchen by restaurant"""
        print("Restaraunt is " + self.cuisine_type.title() + " kitchen.")
    def open_restaraunt(self):
        """Restaurant is opened"""
        print("Restaraunt " + self.restaraunt_name.title() + ". Welcome!")
class IceCreamStand(Restaraunt):
    def __inint__(self,restaraunt_name,cuisine_type):
        super().__init__(self,restaraunt_name,cuisine_type)
    def flavours(self):
        """What kind of ice cream is available"""
        flavour=['chocolate','vanil','bluebery']
        print("This rest have a " + (', '.join(flavour)) + ' icecreams' )
my_rest=IceCreamStand('icecool','russian')
my_rest.describe_restaraunt()
my_rest.flavours()

