#Custom Albums: Start with the program from Exercise 8-7.
#Write a while loop in which the user enters the artist and the album name. 
#Then the make_album() function is called in the loop for the entered users and the created dictionary is output. 
#Don't forget to provide a completion sign in the while loop.

def make_album(name,titl,):
    mus={'first':name,'last':titl}
    return mus
while True:
    print("Tell name")
    print("Tell title of album")
    print("Tell 'q' for exit programm")
    name1=input("Name ")
    if name1=="q":
        break
    titl1=input("Title ")
    if titl1=="q":
        break
    form=make_album(name1,titl1)
    print(form)
print("goodbye!")

