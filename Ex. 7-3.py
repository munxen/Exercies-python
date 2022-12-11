#Numbers that are multiples of 10: Ask the user for a number and tell them if it is a multiple of 10 or not.

num=input("Enter a number" )
num=int(num)
if num %10==0:
    print("This number is a multiple of 10")
else:
    print("This number is a not multiple of 10")
