#10-3. Guest: Write a program that asks the user for his name. Entered response 
# is saved in a file named guest.txt .

name = input ("What's your name?\n")
mos = "Your name is " + name.title() + "."
file = 'guest.txt'
with open (file , 'w') as name_object:
    name_object.write( mos )