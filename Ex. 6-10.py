#Favorite numbers: change the program from exercise 6-2 (p. 107) so that for each 
#a person could store more than one favorite number. 
# Print the name of each person in the list and their favorite numbers

favorite_places={
    'paris':'bob',
    'london':['tim','simon'],
    'mexico':['dealon','heissenberg','marty']
}
for places,names in favorite_places.items():
    print("\nPlace is "+places.title()+" is liked by ")
    print(names)
