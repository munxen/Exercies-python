#3-5. Changing the guest list: you just found out that one of the guests will not be able to come, 
#so you will have to send out new invitations. The absent guest needs to be replaced by someone else.
#Start with the program from exercise 3-4. Add the print command to the end of the program 
#to output the name of the guest who will not be able to come.
#Change the list and replace the name of the guest who can't come with the name of the new one 
#invited.
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
print('Bob')
