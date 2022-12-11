#6-4. Glossary 2: Now that you know how to sort through the dictionary elements, simplify the code from Exercise 6-3, 
# replacing a series of print commands with a loop iterating over the keys and values of the dictionary. When you are sure that, 
# to make sure the loop works, add five more Python terms to the glossary. When you restart the program, the new 
# words and meanings should be automatically included in the output.

terms={}
terms['car']='bmw'
terms['notebook']='lenovo'
terms['cup']='ikea'
terms['phone']='samsung'
print (terms)
for thing , brand in terms.items():
    print(thing.title() + ", his brand is " + brand + ".")