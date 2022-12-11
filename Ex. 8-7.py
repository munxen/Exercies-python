#Album: Write a make_album() function that builds a dictionary with a description of a music album.
#The function should get the artist's name and the album name and return a dictionary containing these two types
# information.
#Use the function to create three dictionaries representing different albums.
#Print all the returned values to show that the information is correctly stored in all three dictionaries.
#Add an additional parameter to make_album() to save the number of tracks in the album.
#If the number of tracks is included in the call string, add this value to the album dictionary.
#Create at least one new function call with the transfer of the number of tracks in the album.

def make_album(name,titl,nums=" "):
    mus={'first':name,'last':titl}
    if nums:
        mus['nums']=nums
    return mus
mus1=make_album('genry','rangers',nums=13)
mus2=make_album('ron','silent dogs')
mus3=make_album('bill','foxes')
print(mus1)
print(mus2)
print(mus3)