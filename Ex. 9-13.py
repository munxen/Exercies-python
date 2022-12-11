#Processing with OrderedDict Rewrite: Start with Exercise 6-4 (p. 113), in which the standard dictionary 
# is used to represent the glossary. Rewrite the program using the OrderedDict class and 
# make sure that the order of output matches the order in which key—value pairs are added to the dictionary.

from collections import OrderedDict
users=OrderedDict()
users['marty']='bird'
users['john']='week'
users['spyder']='man'
users['tolik']='robinson'
for name,last_name in users.items():
    print(name.title() + last_name.title() + " liked chips.")

terms={}
terms['car']='bmw'
terms['notebook']='lenovo'
terms['cup']='ikea'
terms['phone']='samsung'
for thing , brand in terms.items():
    print(thing.title() + ", his brand is " + brand + ".")