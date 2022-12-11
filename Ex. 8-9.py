#Magicians: Create a list with the names of magicians. Pass the list to the show function_
# magicians(), which outputs the name of each magician in the list.

def show_magicians(names):
    for name in names:
        x="Hello "+name.title()+"."
        print(x)
usernames=["tom","bob","karl"]
show_magicians(usernames)