#Shortening the guest list: it just turned out that the new dining table will not be delivered in time, 
# and there's only enough room for two guests.
#Start with the program from Exercise 3-6. Add a command to output the message 
# that only two guests are invited to lunch.
#Use the pop() method to sequentially remove guests from the list until 
#until only two people remain on the list. Every time from the list 
#the next name is deleted, output a message for this person that you regret canceling the invitation.
#Output a message for each of the two people remaining in the list. Message 
#must confirm that the earlier invitation remains valid.
#Use the del command to delete the last two names so that the list remains 
#empty. Print the list to make sure that at the end of the program 
#the list doesn't really contain any elements.
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
print("I'm sorry, a can send me only 2 guests")
last_guest1=guests.pop()
print(last_guest1.title()+" ,im sorry fot that")
last_guest2=guests.pop()
print(last_guest2.title()+" ,im sorry fot that")
last_guest3=guests.pop()
print(last_guest3.title()+" ,im sorry fot that")
last_guest4=guests.pop()
print(last_guest4.title()+" ,im sorry fot that")
last_guest5=guests.pop()
print(last_guest5.title()+" ,im sorry fot that")
print(guests[0].title()+" ,you can come to me")
print(guests[1].title()+" ,you can come to me")
del guests
print(guests)
      
