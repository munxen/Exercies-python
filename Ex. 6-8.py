#6-8. Pets: Create several dictionaries whose names represent 
#pet names. In each dictionary, save information about the type of animal and the name of the owner. 
#Save the dictionaries in a list named pets. Sort through the squeak elements. In the process of iterating , output the entire 
# available information about each animal.

simon={
    'type':'dog',
    'owner':'robert'
}
poomba={
    'type':'cat',
    'owner':'marty'
}
rembo={
    'type':'snake',
    'owner':'bob'
}
pets=[simon,poomba,rembo]
for pet in pets:
    print(pet)
    
