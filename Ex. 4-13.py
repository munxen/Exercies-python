#Buffet: The buffet menu in the restaurant consists of only five items.Come up with five simple ones 
# of dishes and save them in the tuple.
# Use the for loop to output all the dishes offered by the restaurant.
# Try changing one of the elements and make sure that Python refuses to make changes.
# The restaurant changes the menu, replacing two items with other dishes. Add a block 
#of the code that replaces the tuple, and use the for loop to output each item of the updated menu.

eat_table=('crab','meat','sandwich','potatos','carrot')
for eat in eat_table:
    print(eat)
new_menu=('crab','meat','sandwich','bananas','apples')
for eats in new_menu:
    print(eats)