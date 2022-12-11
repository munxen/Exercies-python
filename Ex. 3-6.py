#More guests: you have decided to buy a larger dining table. Additional 
#places allow you to invite three more guests to lunch.
#Start with a program from exercise 3-4 or 3-5. Add the print command to the end of the program, which 
#displays a message about expanding the guest list.
#Add an insert() call to add one guest to the top of the list.
#Add an insert() call to add one guest to the middle of the list.
#Add an append() call to add one guest to the end of the list.
#Output a new set of invitation messages – one for each participant included in the list.
guests=['Tom','Alex','Bob','Marry']
print("Hi "+guests[0].title()+" , do you come to me?")
print("Hi "+guests[1].title()+" , do you come to me?")
print("Hi "+guests[2].title()+" , do you come to me?")
print("Hi "+guests[3].title()+" , do you come to me?")
guests[2]='Shon'
print("Hi "+guests[0].title()+" , do you come to me?")
print("Hi "+guests[1].title()+" , do you come to me?")
print("Hi "+guests[2].title()+" , do you come to me?")
print("Hi "+guests[3].title()+" , do you come to me?")
guests.insert(0,'Charlie')
guests.insert(3,'Siana')
guests.append('Karrontas')
print('We a need more guests!')
print("Hi "+guests[0].title()+" , do you come to me?")
print("Hi "+guests[1].title()+" , do you come to me?")
print("Hi "+guests[2].title()+" , do you come to me?")
print("Hi "+guests[3].title()+" , do you come to me?")
print("Hi "+guests[4].title()+" , do you come to me?")
print("Hi "+guests[5].title()+" , do you come to me?")
print("Hi "+guests[6].title()+" , do you come to me?")

