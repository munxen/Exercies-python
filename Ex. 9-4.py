#9-4. Visitors: Start with the program from exercise 9-1 (p. 165). Add the number_served attribute with the value 
# default is 0; it represents the number of visitors served. Create an instance named restaurant.
# Output the number_served value, then change it and output it again. Add a method named set_number_served(),
# which allows you to set the number of visitors served. Call the method with a new number, output again
# value 170. Add a method named increment_number_served(), which increases the number of serviced
# visitors by a given amount. Call this method with any number that could represent
# the number of clients served — say, in one day.

class Restaraunt():
    def __init__(self,restaraunt_name,cuisine_type):
        """A simple restaurant model"""
        self.restaraunt_name=restaraunt_name
        self.cuisine_type=cuisine_type
        self.number_served=10
    def read_number_served(self):
        print("Quantity satisfied guests are " + str(self.number_served))
    def increment_number_served(self,guests):
        self.number_served += guests
    def describe_restaraunt(self):
        """Whats kitchen by restaurant"""
        print("Restaraunt is " + self.cuisine_type.title() + " kitchen.")
    def open_restaraunt(self):
        """Restaurant is opened"""
        print("Restaraunt " + self.restaraunt_name.title() + ". Welcome!")
my_restaraunt=Restaraunt('Coffe Set', 'European')
#my_restaraunt.read_number_served()
#my_restaraunt.number_served=170
#my_restaraunt.read_number_served()
my_restaraunt.increment_number_served(200)
my_restaraunt.read_number_served()

