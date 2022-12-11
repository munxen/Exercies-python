#Learning C: The replace() method can be used to replace any word in a string with another word. 
# In the following example, the word ‘dog’ is replaced by the word ‘cat’:
#>>> message = "I really like dogs."
#>>> message.replace('dog', 'cat')
#'I really like cats.'
#Read each line from the newly created file learning_python.txt and replace 
#the word Python is the name of another language, for example C. Print each modified line to the screen.

with open ("C:/Users/proro/Desktop/python/Delete/python_text.txt") as object:
    text = object.readlines()
for line in text:
    line_2=line.replace('Python', 'C')
    print (line_2.rstrip())