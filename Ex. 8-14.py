# Cars: Write a function to save information about the car in the dictionary.
# The function should always return the manufacturer and the model name, but at the same time it 
# can receive any number of named arguments. Call the function 
# with the transmission of mandatory information and two more name—value pairs (for example, color 
# and equipment). Your function should work for calls of the following type:
# car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
#Output the returned dictionary and make sure that all the information has been saved 
# right.

def make_car(maker,name,**other):
    full={}
    full['maker']=maker
    full['name']=name
    for key,value in other.items():
        full[key]=value
    return full
car=make_car('bmw','M3',color='black',tow_package=True)
print (car)