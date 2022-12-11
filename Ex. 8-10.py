#Great Magicians: Start with a copy of your program from Exercise 8-9. Write 
# the make_great() function, which modifies the list of magicians by adding to the name of each 
# magician prefix "Great". Call the show_magicians() function and make sure that 
# the list has been successfully modified.

def show_magicians(name):
    for names in name:
        show="Hello "+names.title()
        print(show)
def make_great(name):
    for names in name:
        great="Great "+users.pop(0)
        name.append(great)
users=["tom","bob","sam"]
show_magicians(users)
make_great(users)
show_magicians(users)