#Create a Die class with one attribute named sides, which contains a default value of 6.
# Write the roll_die() method to output a random number from 1 to the number of sides of the cube. Create an instance, 
# simulate a 6-sided cube, and simulate 10 throws. Create models of a 10- and 20-sided cube. 
#Simulate 10 rolls of each die.

from random import randint

class Die():
    def __init__(self,sides=6):
        """How many faces does a cube have"""
        self.sides=sides
    def roll_sides(self,):
        """Generates a die roll"""
        self.sides=randint(1,self.sides)
        print(str(self.sides) + " tell on the table!")
my_cube=Die(6)
my_cube.roll_sides()
my_cube=Die(10)
my_cube.roll_sides()
my_cube=Die(20)
my_cube.roll_sides()