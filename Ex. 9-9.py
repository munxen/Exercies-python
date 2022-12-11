#Battery upgrade: Use the final version of the program electric_car.py from this section. 
#Add a method named upgrade_battery() to the Battery class.This method should check the size of the battery 
# and set the power to 85 if it has a different value. Create an instance of an electric vehicle with 
# with the default accumulator, call get_range(), and then call get_range() a second time after calling 
# upgrade_battery(). Make sure that the power reserve has increased.

class Car():
    """Simple models of car"""
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
class ElectricCar(Car):
    """Aspects electrocar's based on a original Car"""
    def __init__ (self,make,model,year):
        """Initializes aspects of the Car class"""
        super().__init__(make,model,year)
        self.battery_size=Battery()
    def describe_battery_size(self):
        """Displays information about the battery charge"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def full_gas_tank(self):
        print("This car doesn't need gas tank!")
class Battery():
    """Electric car battery model"""
    def __init__(self,battery_size=70):
        """Battery Attributes"""
        self.battery_size = battery_size
    def describe_vattery_size(self):
        """Displays information about the battery charge"""
        print("This car has a " + str(self.battery_size) + "-kWh battery")
    def get_range(self):
        """Displays the power reserve"""
        if self.battery_size == 70:
            range=240
        elif self.battery_size == 85:
            range=270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        """Battery upgrade"""
        if self.battery_size <85:
            self.battery_size = 85

my_car=ElectricCar("tesla","model S",2018)
print(my_car.get_descriptive_name())
my_car.battery_size.describe_vattery_size()
my_car.battery_size.get_range()
my_car.battery_size.upgrade_battery()
my_car.battery_size.get_range()