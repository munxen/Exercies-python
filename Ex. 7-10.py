#Dream Vacation: Write a program that polls users wherever they are 
# wanted to spend a vacation. Turn on the code block to display the survey results.

tells={}
active=True
while active:
    name=input("Whats you name? ")
    tell=input("Where would you like to rest? ")
    tells[name]=tell
    repeat=input("Would you like to let another peoples?(yes\no) ")
    if repeat=='no':
        active=False
print("\n---Poll Results---")
for names, places in tells.items():
    print(names.title()+" like rest in "+places+" place.")